# Weasis Documentation Website

[![Hugo](https://img.shields.io/badge/Built%20with-Hugo-FF4088?logo=hugo)](https://gohugo.io/)
[![Theme](https://img.shields.io/badge/Theme-Relearn-blue)](https://github.com/McShelby/hugo-theme-relearn)
[![License](https://img.shields.io/github/license/nroduit/nroduit.github.io)](LICENSE)

Source repository for the **[Weasis documentation website](https://weasis.org/)** — covering installation, configuration, tutorials, and more for the [Weasis DICOM viewer](https://github.com/nroduit/Weasis).

---

## 🚀 Getting Started

### Prerequisites

Before getting started, make sure the following tools are installed:

- [Git](https://git-scm.com/)
- [Hugo](https://gohugo.io/installation/) (extended version recommended)

### 1. Clone the repository

Clone the repository **with its submodules** (the Relearn theme):

```shell
git clone --recurse-submodules https://github.com/nroduit/nroduit.github.io.git
cd nroduit.github.io
```

> **Note:** If you already cloned the repository without submodules, initialize them with:
> ```shell
> git submodule update --init --recursive
> ```

### 2. Update the theme

```shell
cd themes/hugo-theme-relearn
git pull origin main
cd ../..
```

### 3. Start the local development server

```shell
hugo serve
```

The site will be available at [http://localhost:1313](http://localhost:1313). Hugo automatically reloads the browser on file changes.

Refer to the [official Hugo documentation](https://gohugo.io/documentation/) for advanced usage.

---

## 📁 Project Structure

| Path | Description |
|------|-------------|
| `content/` | Markdown source files for all documentation pages |
| `static/` | Static assets (images, JS, CSS, attachments) |
| `layouts/` | Custom Hugo layout overrides and shortcodes |
| `data/` | Site data — notably `versions.toml`, the documented version window |
| `themes/` | Hugo Relearn theme (git submodule) |
| `config.toml` | Site configuration |


---

## 🏷️ Documenting Weasis versions

The site documents **several Weasis releases from one set of pages**. There is no
copy of `content/` per version: pages state which release a given behavior belongs
to, and readers filter the page to their own version.

### What the reader gets

A **version selector** sits in the sidebar, under the search box. It defaults to the
current stable release. Pick an older one and the page adapts:

- facts that arrived later are flagged **"not in your version"** in red;
- passages and pages describing features that do not exist in that release are hidden,
  and a page opened directly still shows its content, with a banner explaining it;
- the choice is remembered, and `?v=4.6` in a URL preselects a version — which is how
  an in-app **Help** link can land a reader on the right variant.

Filtering happens **in the browser only**. Every version's content is always present in
the HTML, so search engines, printouts and readers without JavaScript see the complete
page. Never use these markers to keep something unpublished.

### The version window

`data/versions.toml` lists the releases the site documents — currently three older
releases, the current one, and the next. Versions are tracked at **minor** granularity
(`4.7`, not `4.7.3`); patch-level detail lives in the badge text.

| state | meaning |
|-------|---------|
| `supported` | an older release still documented |
| `current` | the latest stable release — the selector's default |
| `next` | the upcoming release, documented ahead of time |
| `maintained` / `archived` | a separate documentation line, published at its own URL |

### Marking a version in a page

Pick the mode that matches the *scope* of what changed:

| What is version-specific | Mode |
|--------------------------|------|
| a fact inside a sentence | an inline `since` / `until` badge |
| a passage — paragraphs, lists, tables, images | a `version` block |
| an entire page | `since:` / `until:` in the front matter |

```markdown
Most keyboard shortcuts can be customized {{< since "4.7.0" >}} in **Preferences**.

{{% version until="4.6" %}}
In 4.6 and earlier this was a standalone window instead.
{{% /version %}}
```

### What each mode does

The two inline badges always stay visible and change appearance; the block and the
front matter hide content instead. In every case the filtering is client-side — the
HTML always contains everything.

| Mode | Written as | Reader's version is in range | Reader's version is out of range |
|------|------------|------------------------------|----------------------------------|
| `since` — inline | `customizable {{< since "4.7.0" >}}` | reads *since v4.7.0*, in a quiet blue badge | red dashed badge prefixed with **×** |
| `until` — inline | `available {{< until "4.6.6" >}}` | reads *until v4.6.6*, in an amber badge | red dashed badge prefixed with **×** |
| `version` — block | `{{% version since="4.8" %}}` … `{{% /version %}}` | the passage is shown | the passage is hidden |
| | `{{% version until="4.6" %}}` … `{{% /version %}}` | shown | hidden |
| front matter | `since: "4.5.0"` &nbsp;/&nbsp; `until: "4.6.6"` | the page behaves normally | the page drops out of the sidebar; opened directly it still shows its content, above a banner naming the release it needs |

Both `since` and `until` accept a version older than the whole window. The badge then
renders permanently in its in-range appearance — the statement is true for every release
the site documents — and never turns red.

### Rules worth knowing

1. **A badge is a whole phrase, not a word.** `{{< since "4.7.0" >}}` renders
   *"since v4.7.0"*, so write `customizable {{< since "4.7.0" >}}` — never
   `customizable since {{< since "4.7.0" >}}`. This also means the marker can be
   deleted later without leaving a broken sentence behind.
2. **Patch versions are fine in the text.** `{{< since "4.7.2" >}}` displays the full
   version but filters as `4.7`.
3. **A version older than the window still renders**, it simply never turns red — the
   feature is present in every documented release. Keep it where the version *is* the
   information (a deployment requirement, build history); drop it where it is a
   changelog note nobody can act on.
4. **A `version` block must not contain headings.** Hugo does not register headings
   inside a shortcode, so their anchors and table-of-contents entries disappear and
   internal links to them break. Mark such a section with an inline badge instead.
5. **Shortcodes do not run inside code blocks.** Put the note on a line below the
   block: ``The `-m` option is available {{< since "4.6.0" >}}.``
6. **Watch the build.** A `since` newer than the window, or an `until` older than it,
   is reported as a warning — the first means `versions.toml` is stale, the second
   that the sentence applies to no documented release.

### When a release ships

Roll the window forward in `data/versions.toml`: `next` becomes `current`, the old
`current` becomes `supported`, add the new `next`, and drop the oldest entry. The file's
own comments spell this out, including how to keep an old release online as an archived
line. At a **major** release the whole line is branched instead — see the notes in
`data/versions.toml` and `CLAUDE.md`.

---

## ✍️ Contributing

Contributions are welcome! To propose a change:

1. Fork the repository and create a new branch.
2. Add or edit Markdown files under `content/`.
    - Use the `*.en.md` suffix for English content.
    - Place shared images in `static/` (referenced via `/images/...`).
    - Mark anything that is specific to a Weasis release — see the
      **Documenting Weasis versions** section above.
3. Preview your changes locally with `hugo serve`.
4. Open a Pull Request against the `main` branch.

Each published page exposes an **Edit this page** link that points directly to the corresponding file on GitHub, making small fixes easy.

## 📚 Useful links

- [Weasis project](https://github.com/nroduit/Weasis)
- [Hugo documentation](https://gohugo.io/documentation/)
- [Relearn theme documentation](https://mcshelby.github.io/hugo-theme-relearn/)