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

# Update the theme to its latest upstream
cd themes/hugo-theme-relearn && git pull origin main && cd ../..
```

Hugo **extended** is required (Dart Sass). CI pins `HUGO_VERSION=0.152.2` in `.github/workflows/hugo.yaml` — prefer matching that locally when reproducing CI behavior.

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
- **Deployment** — pushes to `main` trigger `.github/workflows/hugo.yaml`, which builds with Hugo extended and deploys `public/` to GitHub Pages. There is no test suite; the build itself is the gate.

## Content audience & style

Different top-level sections target different readers — match the tone to the section you are editing:

- **`tutorials/`** — written for **end users** of the Weasis viewer (clinicians, technologists, students). Keep the language accessible: avoid unnecessary jargon, explain DICOM-specific terms briefly the first time they appear, and lead with what the user sees and does. The page should still be **comprehensive** — cover all relevant options and edge cases — but defer deep technical detail to references (link to other pages, the DICOM standard, GitHub issues, external resources) rather than inlining it. Short clinical/background framings are welcome where they help interpretation (e.g. what a DVH is, what fractional segmentation means).
- **`basics/`, `getting-started/`, `viewer-hub/`, `api/`** — written for **integrators, administrators, and configurators** deploying Weasis or wiring it into a PACS / portal. Here a more technical register is appropriate: configuration keys, properties files, command-line flags, protocol details, code snippets.
- **`stories/`** — testimonials / case studies; follow the existing pages' narrative tone.

**Language:** all English content (`*.en.md`) is written in **American English** (e.g. _color_, _organization_, _customize_, _gray_, _-ize_ endings). When polishing a page, normalize British spellings to American.

## Editing notes

- `[params.link] errorlevel = 'warning'` in `config.toml` means broken internal links surface as warnings during `hugo serve`, not failures — watch the dev server output when changing links.
- `markup.goldmark.renderer.unsafe = true` is intentional so shortcodes and inline HTML/JS render. Be mindful when adding raw HTML to content.
- The site uses the Relearn-theme front matter conventions (`title`, `weight`, `hidden`, `chapter`, etc.). Look at neighboring pages in the same section before adding new front matter keys.