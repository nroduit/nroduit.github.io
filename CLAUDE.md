# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Source for **https://weasis.org/** — the documentation site for the Weasis DICOM viewer. It is a Hugo static site using the [Relearn theme](https://github.com/McShelby/hugo-theme-relearn), pulled in as a git submodule at `themes/hugo-theme-relearn`. Content is authored in Markdown; there is no application code.

## Common commands

```shell
# First-time setup (theme is a submodule — required for the site to build)
git submodule update --init --recursive

# Local dev server with live reload at http://localhost:1313
hugo serve

# Production build (matches the CI build)
hugo --gc --minify

# Conformity checks on the build output — canonicals, robots, sitemaps, JSON-LD,
# llms.txt (CI runs this on every deploy; needs a build in public/ first)
python3 .github/scripts/seo-conformity.py

# Update the theme to its latest upstream
cd themes/hugo-theme-relearn && git pull origin main && cd ../..
```

Hugo **extended** is required (Dart Sass). CI pins `HUGO_VERSION=0.165.0` in `.github/workflows/hugo.yaml` — prefer matching that locally when reproducing CI behavior.

### HUGO_GH_TOKEN

Two pieces of the site call the GitHub Releases API at build time and require a GitHub token in the `HUGO_GH_TOKEN` env var:

- `layouts/shortcodes/latest-download.html` — the download table on the site (`{{< latest-download >}}`).
- `layouts/api/single.api.json` — the `/api/release/api.json` endpoint consumed by the live download widget.

Without the token both render an inline error. CI injects it from the `HUGO_GH_TOKEN` secret. For local dev, either export a personal access token or expect those two areas to show the error message.

## Architecture

- **Content** lives under `content/`. Files are language-suffixed: `*.en.md` (English, default), `*.fr.md` (French). `defaultContentLanguageInSubdir=true` in `config.toml` means English is served under `/en/`, not the root. When adding a page, mirror the existing `.en.md` convention; section landing pages are `_index.en.md`.
- **Top-level sections** map directly to the site nav: `basics/`, `getting-started/`, `tutorials/`, `viewer-hub/`, `stories/`, `api/`.
- **Static assets** under `static/` are served at the site root. Images referenced from Markdown live in `static/images/...` and are linked as `/images/...`.
- **Theme overrides** sit in `layouts/` and shadow files of the same path in `themes/hugo-theme-relearn/layouts/`. Custom shortcodes (used heavily across content) are in `layouts/shortcodes/`:
  - `latest-download.html`, `old-download.html` — GitHub-release-driven download tables.
  - `launch.html` — buttons that launch Weasis with JNLP-style parameters.
  - `image-gallery.html` — galleries used on the home page (`gallery_dir` points into `static/images/`).
  - `mkd.html` — includes another Markdown file inline (used on the home page).
  - `version-compatibility.html`, `badgeC.html`, `svg.html`, `svg-inline.html`, `render-preferences.html`.
- **JSON output** — `content/api/release.md` declares `outputs = ["API"]`, which selects `layouts/api/single.api.json` (the `API` output format is defined in `config.toml`) to emit `/api/release/api.json` for external consumers.
- **Deployment** — pushes to `main` trigger `.github/workflows/hugo.yaml`, which builds with Hugo extended and deploys `public/` to GitHub Pages. `static/CNAME` pins the custom domain (`weasis.org`) in version control rather than leaving it in a repository setting: the `nroduit.github.io` → `weasis.org` redirect depends on it, and `weasis.help.online` — the in-app Help base URL, baked into shipped installers — depends on that redirect. Do not delete it. There is no test suite for the content; the gate is the build plus `.github/scripts/seo-conformity.py`, which inspects the generated site (see *Discoverability* below).

## Content audience & style

Different top-level sections target different readers — match the tone to the section you are editing:

- **`tutorials/`** — written for **end users** of the Weasis viewer (clinicians, technologists, students). Keep the language accessible: avoid unnecessary jargon, explain DICOM-specific terms briefly the first time they appear, and lead with what the user sees and does. The page should still be **comprehensive** — cover all relevant options and edge cases — but defer deep technical detail to references (link to other pages, the DICOM standard, GitHub issues, external resources) rather than inlining it. Short clinical/background framings are welcome where they help interpretation (e.g. what a DVH is, what fractional segmentation means).
- **`basics/`, `getting-started/`, `viewer-hub/`, `api/`** — written for **integrators, administrators, and configurators** deploying Weasis or wiring it into a PACS / portal. Here a more technical register is appropriate: configuration keys, properties files, command-line flags, protocol details, code snippets.
- **`stories/`** — testimonials / case studies; follow the existing pages' narrative tone.

**Language:** all English content (`*.en.md`) is written in **American English** (e.g. _color_, _organization_, _customize_, _gray_, _-ize_ endings). When polishing a page, normalize British spellings to American.

## Version-aware content

The site documents a rolling window of Weasis versions (three older releases, the
current one, and the next one) from a **single content tree** — there is no
per-version copy of `content/`. `data/versions.toml` is the only place the window
is declared; the sidebar selector, the badges and the block filter all derive
from it. Rolling it forward at release time is a two-line edit (the comments in
that file spell out the steps).

Mark version differences in Markdown with:

```markdown
Most shortcuts are customizable {{< since "4.7.0" >}}.
The legacy applet launcher is available {{< until "4.6.6" >}}.

{{% version since="4.8" %}}
A whole section — headings, images, tables — that only exists from 4.8 on.
{{% /version %}}
```

- `since` / `until` are **self-contained phrases** ("since v4.7.0"), so write the
  sentence around them without repeating the word: `customizable {{< since "4.7.0" >}}`,
  not `customizable since {{< since "4.7.0" >}}`. That way the call can later be
  deleted without breaking the sentence. They are the **only** way to mark a
  version: the two conventions they replaced — `badgeC`, and the theme's
  `{{% badge title="Version" %}}` — are gone from `content/` and must not come
  back, since neither is filtered. The theme's `badge` shortcode is still fine
  for non-version labels such as `style="info"`.
- A `since` version older than the whole window still renders, but without a
  filter index: the feature is present in every documented version, so the badge
  stays in its ordinary state whatever the reader selects. Nothing is dropped
  when the window rolls forward — pruning a marker that has stopped being
  interesting is an editorial call. Keep it where the version is the
  information (a deployment requirement, build history); drop it where it is
  just a changelog note with no action attached.
- A `since` version *newer* than the window, and an `until` version older than
  it, are both reported as build warnings: the first means `versions.toml` is
  stale, the second means the sentence applies to no documented version at all.
- Versions are tracked at **minor** granularity (`4.7`); a patch-level argument
  such as `4.7.2` is displayed in full but filters as `4.7`.
- Everything is always rendered into the HTML; the reader's choice only hides
  content client-side (generated CSS keyed on `<html data-docv>`). So there is
  one canonical URL per topic, one search index, and full content with
  JavaScript off. Never use these shortcodes to hide something that must not be
  published.
- A `{{% version %}}` block must **not** contain headings. Hugo does not register
  headings that live inside a shortcode's inner content, so their anchors drop
  out of the fragment registry (breaking internal links, with a build warning)
  and out of the page TOC. Gate a section with an inline `since` badge on its
  first paragraph instead, and keep blocks to prose, lists, tables and images.
- `?v=4.6` in a URL preselects a version — that is how the app's
  `weasis.help.online` property can send readers to the right variant.

When a **whole page** only applies to part of the window, gate it in front
matter instead of wrapping the body:

```toml
since: "4.7.1"   # or: until: "4.6.6"
```

The page then hides its own sidebar entry outside that range and shows a banner
above the title. The page itself is never hidden — someone arriving from a
search engine or an in-app help link must still be able to read it. Use this
only when the whole page is version-specific; a page that merely gained a
section wants a `version` block.

**Other documentation lines.** A version that leaves the window can stay online
as its own build instead of being folded into this one. Add a *line entry* to
`data/versions.toml` — any entry that declares a `url` — with a `branch` and a
state of `maintained` (the previous major, still receiving fixes) or `archived`
(frozen). The "Build other documentation lines" step of
`.github/workflows/hugo.yaml` rebuilds each such branch, with its own content,
layouts and theme commit, into `public/<url>/` on every deploy; nothing is
written back to the repository and no built HTML is committed. Line entries are
never filtered — selecting one in the sidebar navigates to it.

A line build sets `params.docline` and `params.doclinestate`, which make it
`noindex`, point its canonical at the same page on the current line, and show a
banner: "still maintained" for `maintained`, "no longer updated" for `archived`,
which also drops the version selector since the build is frozen.

**At a major release**, snapshot the line rather than annotating across it —
that is the case where most screenshots change at once. Branch the current
content (e.g. `4.x`), reset `data/versions.toml` on `main` to the new major's
window, and add one line entry for the old branch at `/4.x/`. Re-shoot
screenshots **in place**, keeping the same file paths: the branch split is what
versions the images, so no Markdown changes. On the old branch add the
mirror-image entry pointing back at `/`, and set `weasis.help.online` in the
app's `base.json` to the matching path prefix — the app concatenates the help
topic straight onto that property, so routing between lines must be a path,
never a query parameter. Within each line, keep using `since` / `until`.

Moving parts: `data/versions.toml`, `layouts/partials/_weasis/*.gotmpl`,
`layouts/partials/docversion-head.html` (generated CSS + selection bootstrap),
`layouts/partials/sidebar/element/docversion.html` (selector, wired through
`sidebarheadermenus` in `config.toml`), `layouts/partials/docversion-page.html`
(page banners, via the `content-header.html` hook), `static/js/doc-version.js`,
the `since` / `until` / `version` shortcodes, and the "Build other documentation
lines" step in `.github/workflows/hugo.yaml`.

## Discoverability (search engines and AI assistants)

Most of what makes this site findable is emergent — a few config flags, a few
template overrides — and it breaks without failing a build. The moving parts:

- `layouts/partials/custom-header.html` decides, per page, which URL it is
  indexed under and whether it is indexed at all: self-referential canonical plus
  `max-snippet:-1, max-image-preview:large` for ordinary pages, `noindex` for the
  printer-friendly rendering and for a documentation-line build, and the
  `og:image` fallback for pages with no image of their own.
- `layouts/partials/seo-jsonld.html` emits schema.org JSON-LD as one entity graph:
  `#organization`, `#website` and `#weasis` are declared once on the home page and
  referenced by `isPartOf` / `about` / `publisher` from every other page, which is
  what lets a crawler merge the pages into one picture of one program. Breadcrumbs
  are deliberately left to the theme's microdata — do not add a second trail.
- `layouts/robots.txt` welcomes AI crawlers by name and withholds only the search
  page and the taxonomy stubs. Never disallow by a pattern like `/*/tags/`: it
  also matches `/en/tutorials/tags/`.
- `/llms.txt` and `/llms-full.txt` (`layouts/_default/home.llms.txt`,
  `home.llmsfull.txt`, helper `layouts/partials/_weasis/pagetree.gotmpl`) follow
  the convention at <https://llmstxt.org/>. They reach the **site root** through
  the `../` in their output format's `baseName`, and are enabled for English only
  in `[Languages.en.outputs]` — which must repeat `section` and `page`, since a
  per-language `outputs` replaces the whole table instead of merging into it.
- **Dates.** `enableGitInfo` gives every page a `lastmod` from its last commit,
  which feeds `<lastmod>` in the sitemap and `dateModified` in the JSON-LD; a page
  added in the working tree has none until committed. Readers see a different
  date: the `Updated …` line appears only where a page declares `updated:` in its
  front matter (see *Editing notes*). Nothing per-page is shown otherwise —
  `hideAuthorName`, `hideAuthorEmail` and `hideAuthorDate` are all on, the last
  because the theme's byline date is the commit date and would move on a
  metadata-only edit.
- `params.disableSeoHiddenPages = false` matters: `hidden: true` keeps a page out
  of the sidebar, and with that flag set it also marked `/features/`, `/faq/`,
  `/demo/` and `/get-involved/` `noindex` while the sitemap still listed them.
- `params.disableExplicitIndexURLs = true` stops the theme appending `index.html`
  to internal links, breadcrumbs and `og:url`, which otherwise disagree with the
  canonical.

Run `python3 .github/scripts/seo-conformity.py` after a build before changing any
of this; its docstring lists every invariant and why it is there. While `hugo
serve` is running it owns `public/`, so build somewhere else for a check —
`hugo --gc --minify -d public-check` and `--root public-check` — or the two
builds interleave and the checker reports failures that are not real.

### Images

Screenshots are the content of this documentation — grey-level detail, thin
overlay text and measurement graphics — so **nothing here is ever re-encoded
lossily**. The current state was reached by measuring every candidate and
verifying it pixel-by-pixel:

- **Screenshots are lossless WebP.** For this material WebP lossless is both
  smaller *and* bit-exact: 6.99 MB of PNG became 3.04 MB with pixel-identical
  output, while WebP at q95 was *larger* (3.78 MB) and already visibly degraded
  (SSIM down to 0.85). There is no quality/size trade-off to make here — the
  lossless option wins on both counts. Two PNGs stay PNG because the encoder was
  not bit-exact on them: `images/architecture-packages.png` and `images/light.png`.
- **The 26 JPEGs are left exactly as they are.** WebP lossless would grow them
  from 4.82 MB to 13.11 MB (lossless re-encoding of already-lossy data), and WebP
  q92 would save 13% while adding a second generation of loss. Do not "optimize"
  them.
- **Never bake annotations into a screenshot.** Use the `annotate` shortcode: the
  clean image plus an SVG overlay, so labels stay crisp, selectable and
  translatable. `static/tuto/gui-overview.svg` is the older approach — a raster
  with drawn-on boxes — and its screenshot is now an external WebP referenced
  from the SVG rather than a 600 KB base64 payload, which is what made that one
  page ship 861 KB of HTML.
- To re-evaluate after adding images, measure rather than assume: encode each
  candidate, compare the decoded pixel arrays, and only accept a format change
  that is exact.

## Editing notes

- `[params.link] errorlevel = 'warning'` in `config.toml` means broken internal links surface as warnings during `hugo serve`, not failures — watch the dev server output when changing links.
- `markup.goldmark.renderer.unsafe = true` is intentional so shortcodes and inline HTML/JS render. Be mindful when adding raw HTML to content.
- The site uses the Relearn-theme front matter conventions (`title`, `weight`, `hidden`, `chapter`, etc.). Look at neighboring pages in the same section before adding new front matter keys.
- `linkTitle` keeps navigation short when `title` is written for a search result:
  the sidebar, breadcrumb and `{{% children %}}` listings use `linkTitle`, while
  `title` becomes the `<h1>` and the `<title>`. That is why the download page is
  *Download Weasis: Free DICOM Viewer for Windows, macOS and Linux* in a search
  result and just *Download Weasis* in the sidebar.
- **`updated: 2026-09-20`** is the only thing that puts a visible date on a page.
  Set it when the *content* changes in a way a returning reader should know about;
  leave it alone for a typo, a re-worded description or a metadata pass. It is
  deliberately not named `lastmod`: Hugo resolves `lastmod` for every page from
  the `[frontmatter]` chain in `config.toml`, so a template cannot tell a declared
  value from the Git fallback, whereas `updated` exists only because someone wrote
  it. A declared `updated` also takes precedence for the sitemap and the JSON-LD,
  so the editorial claim is what search engines see too.