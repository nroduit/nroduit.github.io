# Weasis Documentation Website

[![Hugo](https://img.shields.io/badge/Built%20with-Hugo-FF4088?logo=hugo)](https://gohugo.io/)
[![Theme](https://img.shields.io/badge/Theme-Relearn-blue)](https://github.com/McShelby/hugo-theme-relearn)
[![License](https://img.shields.io/github/license/nroduit/nroduit.github.io)](LICENSE)

Source repository for the **[Weasis documentation website](https://weasis.org/)** — covering installation, configuration, tutorials, and more for the [Weasis DICOM viewer](https://github.com/nroduit/Weasis).

---

## Prerequisites

Before getting started, make sure the following tools are installed:

- [Git](https://git-scm.com/)
- [Hugo](https://gohugo.io/installation/) (extended version recommended)

---

## Getting Started

### 1. Clone the repository

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
git pull origin
cd ../..
```

### 3. Start the local development server

```shell
hugo serve
```

The site will be available at [http://localhost:1313](http://localhost:1313). Hugo automatically reloads the browser on file changes.

For a full production build (output in the `public/` directory):

```shell
hugo
```

Refer to the [official Hugo documentation](https://gohugo.io/documentation/) for advanced usage.

---

## Project Structure

| Path | Description |
|------|-------------|
| `content/` | Markdown source files for all documentation pages |
| `static/` | Static assets (images, JS, CSS, attachments) |
| `layouts/` | Custom Hugo layout overrides and shortcodes |
| `themes/` | Hugo Relearn theme (git submodule) |
| `config.toml` | Site configuration |

---

## Contributing

Contributions are welcome! To propose a change:

1. Fork the repository and create a new branch.
2. Edit or add Markdown files under `content/`.
3. Preview your changes locally with `hugo serve`.
4. Open a Pull Request against the `main` branch.

You can also use the **Edit this page** link available on every documentation page to quickly propose edits directly on GitHub.
