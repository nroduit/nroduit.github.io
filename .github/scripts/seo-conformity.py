#!/usr/bin/env python3
"""Check the generated site for the things search engines and AI crawlers read.

Run it on the output of a Hugo build, not on the sources:

    hugo --gc --minify
    python3 .github/scripts/seo-conformity.py

Exit status is 0 when every invariant holds and 1 otherwise; warnings never fail
the run. Under GitHub Actions the findings are also emitted as annotations.

Why this exists as a build artifact check. Most of what makes a documentation
site findable is emergent: it comes out of a theme, a handful of config flags and
a few template overrides, and it breaks silently. A single flag once made the four
best landing pages `noindex` while the sitemap kept advertising them; the theme
appends `index.html` to internal links, which quietly disagreed with every
canonical; /llms.txt reaches the site root through a `../` in an output format's
baseName, which is a property of how Hugo cleans a path and could change with any
upgrade. None of that fails a build, and none of it is visible in a diff — but all
of it is checkable in public/ in about two seconds, which is what this does.

The invariants, roughly in order of how likely each is to break:

  * nothing in a sitemap is noindex, and nothing in a sitemap is blocked by
    robots.txt — the two ways to ask a crawler to fetch a page and then ignore it
  * a page that is in no sitemap is either noindex or robots-blocked, so it can
    never compete with the page it duplicates
  * canonical is self-referential and og:url agrees with it
  * exactly one canonical link and at most one robots meta per page
  * print renderings are noindex and never canonicalise to themselves
  * every indexable page has a title, a description and an og:image that exists
  * every JSON-LD block parses, carries @context and @type, and every @id it
    references is defined somewhere on the site
  * sitemaps: W3C datetime lastmod, hreflang sets that include x-default, every
    <loc> and every alternate actually built
  * robots.txt grammar, a Sitemap: line that resolves to a built file, and the
    same rules in every group — a named crawler ignores the '*' group, so rules
    that live in only one of them apply to some crawlers and not others
  * llms.txt structure (llmstxt.org), no dead links, coverage against the sitemap
  * alias redirects point at pages that exist
  * the four pages that live in the shortcut menu are indexable and listed

Adding a check is usually a few lines; prefer failing on what is unambiguous and
warning on what is a judgement call.
"""

import argparse
import json
import os
import re
import sys
import xml.dom.minidom as dom
from collections import defaultdict
from urllib.parse import urlsplit

# Pages that are deliberately kept out of the sidebar tree with `hidden: true`
# and reachable from the shortcut menu instead. They have been silently
# de-indexed once; this names them so it cannot happen unnoticed again.
SHORTCUT_PAGES = ("features", "faq", "demo", "get-involved")

# llms.txt maps the English tree only, and /en/api/ is a hidden stub whose one
# child — the release JSON — is listed under its "Optional" heading instead.
LLMS_COVERAGE_EXEMPT = ("/en/api/",)


class Report:
    def __init__(self):
        self.fails, self.warns, self.notes = [], [], []
        self.gha = os.environ.get("GITHUB_ACTIONS") == "true"

    def fail(self, check, msg):
        self.fails.append((check, msg))

    def warn(self, check, msg):
        self.warns.append((check, msg))

    def note(self, msg):
        self.notes.append(msg)

    def print(self):
        print("== site")
        for n in self.notes:
            print("   %s" % n)
        if self.warns:
            print("\n== warnings (%d)" % len(self.warns))
            for c, m in self.warns:
                print("   %-22s %s" % (c, m))
                if self.gha:
                    print("::warning title=%s::%s" % (c, m))
        print("\n== failures (%d)" % len(self.fails))
        for c, m in self.fails:
            print("   %-22s %s" % (c, m))
            if self.gha:
                print("::error title=%s::%s" % (c, m))
        if not self.fails:
            print("   none")
        return 1 if self.fails else 0


def read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def detect_base(root, rep):
    """The site's base URL, taken from the Sitemap: line in robots.txt.

    Hugo is told the base URL on the command line (CI passes the GitHub Pages
    one), so hardcoding it here would make this script pass or fail for the wrong
    reason. robots.txt names it, including any path prefix a project site has.
    """
    rf = os.path.join(root, "robots.txt")
    if not os.path.exists(rf):
        rep.fail("robots.txt", "missing — cannot determine the site's base URL")
        return None
    m = re.search(r"(?mi)^Sitemap:\s*(\S+)/sitemap\.xml\s*$", read(rf))
    if not m:
        rep.fail("robots/sitemap", "no absolute 'Sitemap: .../sitemap.xml' line")
        return None
    return m.group(1)


class Site:
    def __init__(self, root, base, rep):
        self.root, self.base, self.rep = root, base, rep
        self.prefix = urlsplit(base).path.rstrip("/")   # "" unless served from a subpath
        self.pages, self.aliases = {}, {}
        for dirpath, _, files in os.walk(root):
            for f in files:
                if not f.endswith(".html"):
                    continue
                fp = os.path.join(dirpath, f)
                html = read(fp)
                if re.search(r'http-equiv="?refresh', html):
                    self.aliases[fp] = html
                elif 'id="R-html"' in html:
                    self.pages[fp] = html
                else:
                    # hand-written static HTML, e.g. a search-engine ownership
                    # file: not rendered by Hugo, so none of this applies
                    rep.note("skipped non-Hugo HTML: %s" % self.rel(fp))

    def rel(self, path):
        return path[len(self.root):]

    def file_for(self, url):
        """Local file a site URL should have been written to, or None if off-site."""
        parts = urlsplit(url)
        if parts.scheme and not url.startswith(self.base):
            return None
        path = parts.path
        if self.prefix and path.startswith(self.prefix):
            path = path[len(self.prefix):]
        if path.endswith("/") or not os.path.splitext(path)[1]:
            path = path.rstrip("/") + "/index.html"
        return os.path.join(self.root, path.lstrip("/"))

    def built(self, url):
        f = self.file_for(url)
        return f is not None and os.path.exists(f)

    def url_for(self, path):
        """The URL a local page file is published at."""
        return self.base + self.rel(path).replace("/index.html", "/")


def meta(html, name, prop=False):
    key = "property" if prop else "name"
    pat = r'<meta\s+%s="%s"\s+content="([^"]*)"' % (key, re.escape(name))
    m = re.search(pat, html) or re.search(
        r'<meta\s+content="([^"]*)"\s+%s="%s"' % (key, re.escape(name)), html)
    return m.group(1) if m else None


def check_sitemaps(site, rep):
    """Returns the list of URLs the site offers to search engines."""
    urls, alternates = [], defaultdict(list)
    index = os.path.join(site.root, "sitemap.xml")
    files = []
    if not os.path.exists(index):
        rep.fail("sitemapindex", "sitemap.xml is missing from the site root")
        return urls
    try:
        dom.parse(index)
    except Exception as exc:
        rep.fail("sitemapindex/xml", "not well-formed: %s" % exc)
    for loc in re.findall(r"<loc>([^<]+)</loc>", read(index)):
        f = site.file_for(loc)
        if f is None or not os.path.exists(f):
            rep.fail("sitemapindex", "references a sitemap that is not built: %s" % loc)
        else:
            files.append(f)
    if not files:
        rep.fail("sitemap", "the sitemap index lists no usable sitemap")

    for f in files:
        try:
            dom.parse(f)
        except Exception as exc:
            rep.fail("sitemap/xml", "%s not well-formed: %s" % (site.rel(f), exc))
            continue
        for block in re.findall(r"<url>(.*?)</url>", read(f), re.S):
            loc = re.search(r"<loc>([^<]+)</loc>", block).group(1)
            urls.append(loc)
            lastmod = re.search(r"<lastmod>([^<]+)</lastmod>", block)
            if not lastmod:
                # enableGitInfo has no commit for this file yet — normal for a
                # page added in the working tree, wrong for a committed one
                rep.warn("sitemap/lastmod", "no <lastmod>: %s" % loc)
            elif not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2}|Z)$",
                              lastmod.group(1)):
                rep.fail("sitemap/lastmod", "not a W3C datetime: %s in %s"
                         % (lastmod.group(1), loc))
            for _, lang, href in re.findall(
                    r'<xhtml:link rel="(\w+)" hreflang="([^"]+)" href="([^"]+)"', block):
                alternates[loc].append((lang, href))

    if len(urls) != len(set(urls)):
        rep.fail("sitemap/dupes", "the same URL is listed more than once")
    for u in urls:
        if not u.startswith(site.base + "/"):
            rep.fail("sitemap/abs", "not an absolute URL on this site: %s" % u)
        elif not site.built(u):
            rep.fail("sitemap/404", "listed but not built: %s" % u)
    for u, alts in alternates.items():
        if "x-default" not in [lang for lang, _ in alts]:
            rep.fail("sitemap/hreflang", "alternates without x-default: %s" % u)
        for lang, href in alts:
            if not site.built(href):
                rep.fail("sitemap/hreflang", "%s -> %s is not built" % (lang, href))

    rep.note("sitemaps: %d, urls: %d, with hreflang alternates: %d"
             % (len(files), len(urls), len(alternates)))
    return urls


def check_pages(site, rep, sitemap_urls):
    """Head-level conformity, plus the JSON-LD entity graph. Returns noindex set."""
    indexable = {site.file_for(u) for u in sitemap_urls}
    noindex, printed = set(), set()
    defined, referenced = set(), defaultdict(set)

    for fp, html in sorted(site.pages.items()):
        rel = site.rel(fp)
        is_print = fp.endswith("index.print.html")
        is_404 = fp.endswith("404.html")
        if is_print:
            printed.add(fp)

        robots = meta(html, "robots")
        if robots and "noindex" in robots:
            noindex.add(fp)
        if len(re.findall(r'<meta\s+name="robots"', html)) > 1:
            rep.fail("robots/count", "more than one robots meta: %s" % rel)

        canonical_tags = re.findall(r'<link[^>]*rel="?canonical"?[^>]*>', html)
        if fp in indexable or is_print:
            if len(canonical_tags) != 1:
                rep.fail("canonical/count", "%d canonical links: %s"
                         % (len(canonical_tags), rel))
            else:
                href = re.search(r'href="([^"]+)"', canonical_tags[0])
                canonical = href.group(1) if href else None
                if is_print:
                    if not robots or "noindex" not in robots:
                        rep.fail("print/noindex", "print rendering is indexable: %s" % rel)
                    if canonical and canonical.rstrip("/") == (site.base + rel).rstrip("/"):
                        rep.fail("print/canonical",
                                 "print rendering canonicalises to itself: %s" % rel)
                else:
                    own = site.url_for(fp)
                    if canonical != own:
                        rep.fail("canonical/self", "canonical %s != page url %s"
                                 % (canonical, own))
                    og_url = meta(html, "og:url", prop=True)
                    if og_url and og_url != canonical:
                        rep.fail("og:url", "og:url %s != canonical %s (%s)"
                                 % (og_url, canonical, rel))

        if fp in indexable:
            title = re.search(r"<title>(.*?)</title>", html, re.S)
            if not title or not title.group(1).strip():
                rep.fail("title", "no <title>: %s" % rel)
            description = meta(html, "description")
            if not description or not description.strip():
                rep.fail("description", "empty meta description: %s" % rel)
            og_image = meta(html, "og:image", prop=True)
            if not og_image:
                rep.fail("og:image", "no og:image: %s" % rel)
            elif og_image.startswith(site.base) and not site.built(og_image):
                rep.fail("og:image/404", "og:image is not built: %s (%s)" % (og_image, rel))

        for block in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            if is_print:
                rep.fail("jsonld/print", "structured data on a noindex print page: %s" % rel)
            try:
                data = json.loads(block)
            except Exception as exc:
                rep.fail("jsonld/json", "invalid JSON in %s: %s" % (rel, exc))
                continue
            if "@context" not in data:
                rep.fail("jsonld/context", "no @context in %s" % rel)
            if "@type" not in data:
                rep.fail("jsonld/type", "no @type in %s" % rel)

            def walk(node):
                # a dict that is nothing but {"@id": ...} is a reference to an
                # entity; a dict with an @id and other keys defines one
                if isinstance(node, dict):
                    if "@id" in node:
                        if len(node) == 1:
                            referenced[node["@id"]].add(rel)
                        else:
                            defined.add(node["@id"])
                    for value in node.values():
                        walk(value)
                elif isinstance(node, list):
                    for value in node:
                        walk(value)

            walk(data)

    for ref, where in sorted(referenced.items()):
        if ref not in defined:
            rep.fail("jsonld/@id", "%s is referenced by %d page(s) but never defined"
                     % (ref, len(where)))

    for u in sitemap_urls:
        if site.file_for(u) in noindex:
            rep.fail("sitemap/noindex", "in a sitemap but served noindex: %s" % u)

    rep.note("pages: %d, alias redirects: %d, noindex: %d (print renderings: %d)"
             % (len(site.pages), len(site.aliases), len(noindex), len(printed)))
    return indexable, noindex


def robots_match(pattern, path):
    """Length of `pattern` if it matches `path`, else None (robots.txt matching)."""
    if not pattern:
        return None
    anchored = pattern.endswith("$")
    body = pattern[:-1] if anchored else pattern
    regex = "^" + "".join(".*" if ch == "*" else re.escape(ch) for ch in body)
    if anchored:
        regex += "$"
    return len(body) if re.match(regex, path) else None


def check_robots(site, rep, sitemap_urls, indexable, noindex):
    path = os.path.join(site.root, "robots.txt")
    if not os.path.exists(path):
        return
    groups, current, sitemaps = [], None, []
    for line in read(path).split("\n"):
        stripped = line.split("#")[0].strip()
        if not stripped:
            continue
        if ":" not in stripped:
            rep.fail("robots/syntax", "line without a directive: %r" % line)
            continue
        key, value = (part.strip() for part in stripped.split(":", 1))
        key = key.lower()
        if key == "user-agent":
            if current is None or current["rules"]:
                current = {"agents": [], "rules": []}
                groups.append(current)
            current["agents"].append(value)
        elif key in ("allow", "disallow"):
            if current is None:
                rep.fail("robots/syntax", "rule before any User-agent: %r" % line)
            else:
                current["rules"].append((key, value))
        elif key == "sitemap":
            sitemaps.append(value)
        elif key not in ("crawl-delay", "host"):
            rep.warn("robots/unknown", "unrecognised directive: %r" % key)

    if not sitemaps:
        rep.fail("robots/sitemap", "no Sitemap: directive")
    for s in sitemaps:
        if not s.startswith("http"):
            rep.fail("robots/sitemap", "not an absolute URL: %s" % s)
        elif not site.built(s):
            rep.fail("robots/sitemap", "points at a file that is not built: %s" % s)

    star = next((g for g in groups if "*" in g["agents"]), None)
    if not star:
        rep.fail("robots/group", "no 'User-agent: *' group")
        return

    # A crawler named in its own group ignores the '*' group entirely, so a rule
    # added to one group and not the other applies to some crawlers and not
    # others. This site grants every crawler the same access, so every group must
    # carry the same rules; they are generated from one list in layouts/robots.txt.
    baseline = sorted(star["rules"])
    for group in groups:
        if group is star or sorted(group["rules"]) == baseline:
            continue
        missing = sorted(set(baseline) - set(group["rules"]))
        extra = sorted(set(group["rules"]) - set(baseline))
        rep.fail("robots/parity",
                 "group '%s%s' differs from 'User-agent: *'%s%s"
                 % (group["agents"][0],
                    " …" if len(group["agents"]) > 1 else "",
                    "; missing %s" % ", ".join("%s: %s" % r for r in missing) if missing else "",
                    "; extra %s" % ", ".join("%s: %s" % r for r in extra) if extra else ""))

    def blocked(url_path):
        worst = max([robots_match(v, url_path) or -1
                     for k, v in star["rules"] if k == "disallow"] or [-1])
        best = max([robots_match(v, url_path) or -1
                    for k, v in star["rules"] if k == "allow"] or [-1])
        return worst > best

    blocked_in_sitemap = [u for u in sitemap_urls if blocked(urlsplit(u).path)]
    for u in blocked_in_sitemap:
        rep.fail("robots/blocks", "robots.txt blocks a URL listed in a sitemap: %s" % u)

    # A page in no sitemap is only safe if it is noindex or blocked; otherwise it
    # is an orphan that can still be indexed, competing with what it duplicates.
    orphans = [fp for fp in site.pages
               if fp not in indexable and fp not in noindex
               and not fp.endswith("404.html")]
    for fp in sorted(orphans):
        url_path = urlsplit(site.url_for(fp)).path
        if not blocked(url_path):
            rep.fail("orphan", "indexable, in no sitemap, not blocked: %s" % url_path)

    rep.note("robots: %d groups, %d rules in '*', %d orphan pages checked"
             % (len(groups), len(star["rules"]), len(orphans)))


def check_llms(site, rep, sitemap_urls):
    for name in ("llms.txt", "llms-full.txt"):
        path = os.path.join(site.root, name)
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            # these reach the site root through a `../` in the output format's
            # baseName; a Hugo upgrade could move them back under /en/
            rep.fail("llms", "%s is missing or empty at the site root" % name)
            continue
        text = read(path)
        if not text.startswith("# "):
            rep.fail("llms/h1", "%s does not open with an H1" % name)
        if "\n> " not in text[:2000]:
            rep.fail("llms/summary", "%s has no blockquote summary" % name)

        if name == "llms.txt":
            sections = re.findall(r"^## (.+)$", text, re.M)
            if len(sections) < 3:
                rep.fail("llms/sections", "only %d H2 sections" % len(sections))
            links = re.findall(r"\]\((https?://[^)]+)\)", text)
            internal = [l for l in links if l.startswith(site.base)]
            for link in sorted(set(internal)):
                if not site.built(link):
                    rep.fail("llms/link", "dead link: %s" % link)
            covered = {urlsplit(l).path for l in internal}
            missing = [u for u in sitemap_urls
                       if u.startswith(site.base + "/en/")
                       and urlsplit(u).path not in covered
                       and not any(u.endswith(e) for e in LLMS_COVERAGE_EXEMPT)]
            if missing:
                rep.warn("llms/coverage", "%d English page(s) absent: %s%s"
                         % (len(missing), ", ".join(missing[:4]),
                            " …" if len(missing) > 4 else ""))
            rep.note("llms.txt: %d sections, %d links (%d on-site), %d bytes"
                     % (len(sections), len(links), len(internal), len(text)))
        else:
            rep.note("llms-full.txt: %d pages, %d bytes"
                     % (text.count("\nURL: "), len(text)))


def check_aliases(site, rep):
    for fp, html in sorted(site.aliases.items()):
        target = re.search(r"url=([^\"']+)", html)
        if not target:
            rep.fail("alias", "redirect without a target: %s" % site.rel(fp))
            continue
        url = target.group(1).strip()
        if url.startswith(site.base) and not site.built(url):
            rep.fail("alias/404", "%s redirects to a page that is not built: %s"
                     % (site.rel(fp), url))


def check_shortcut_pages(site, rep, sitemap_urls, noindex):
    """The pages a single config flag has already de-indexed once."""
    for slug in SHORTCUT_PAGES:
        url = "%s/en/%s/" % (site.base, slug)
        fp = site.file_for(url)
        if not os.path.exists(fp):
            rep.fail("shortcut-page", "/en/%s/ is not built" % slug)
            continue
        if fp in noindex:
            rep.fail("shortcut-page",
                     "/en/%s/ is noindex again — check params.disableSeoHiddenPages" % slug)
        if url not in sitemap_urls:
            rep.fail("shortcut-page", "/en/%s/ is missing from the sitemap" % slug)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default="public",
                        help="directory holding the built site (default: public)")
    parser.add_argument("--base", default=None,
                        help="site base URL; read from robots.txt when omitted")
    parser.add_argument("--strict", action="store_true",
                        help="treat warnings as failures")
    args = parser.parse_args()

    rep = Report()
    if not os.path.isdir(args.root):
        print("no such directory: %s — run a Hugo build first" % args.root, file=sys.stderr)
        return 2
    base = args.base.rstrip("/") if args.base else detect_base(args.root, rep)
    if not base:
        rep.print()
        return 1

    rep.note("base url: %s" % base)
    site = Site(args.root, base, rep)
    sitemap_urls = check_sitemaps(site, rep)
    indexable, noindex = check_pages(site, rep, sitemap_urls)
    check_robots(site, rep, sitemap_urls, indexable, noindex)
    check_llms(site, rep, sitemap_urls)
    check_aliases(site, rep)
    check_shortcut_pages(site, rep, sitemap_urls, noindex)

    status = rep.print()
    if args.strict and rep.warns:
        return 1
    return status


if __name__ == "__main__":
    sys.exit(main())
