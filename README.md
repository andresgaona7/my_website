# Andres Gaona Website

This repository contains the Hugo source for Andres Gaona's robotics portfolio and blog.

## Main Folders

- `content/`: editable Hugo pages and posts.
- `assets/`: optimized images and videos used by the site.
- `project_sources/`: source notes and project writeups used to prepare portfolio posts.
- `scripts/`: local maintenance scripts, including media conversion tools.
- `themes/LoveIt/`: vendored Hugo theme.
- `public/`: generated Hugo output currently kept in the repository.

## Editing Workflow

Edit portfolio posts in `content/posts/` and the About page in `content/about/`.

Use `project_sources/` for source material, drafts, and richer project notes. Use `assets/` for the optimized media files referenced by Hugo content.

Media processing tools live in `scripts/process_images/`. The scripts use their own folder as the base path, so they can be run from the repository root or from inside `scripts/process_images/`.

## Visualize Locally

From the repository root, run:

```sh
hugo server -D
```

Then open the local URL printed by Hugo, usually:

```text
http://localhost:1313/
```

If port `1313` is already in use, Hugo will print a different local address. Use the address it reports.

## Build

To generate the static site into `public/`, run:

```sh
hugo --minify
```

GitHub Pages is configured in `.github/workflows/hugo.yml` and builds the site on pushes to `main`.

## Public Folder Policy

`public/` is generated output, but it is currently present in this repository. If you keep this policy, rebuild with Hugo after content or asset changes so the generated site stays synchronized with the source.
