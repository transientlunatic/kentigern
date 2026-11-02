# Kentigern

A personal design system for Daniel Williams: the blog, conference talks, interactive d3 figures, matplotlib figures, social cards, a business card and the thesis. Named for St Kentigern (Mungo), Glasgow's patron saint.

The browsable reference is a Claude design-system artifact: https://claude.ai/artifact/9M7tggG4wGFwmZCHwW6C4c (private; sharing is controlled from its Share menu). This repository is its source.

## Layout

| Path | What |
|---|---|
| `tokens/` | Design tokens. `tokens.json` is the single source of truth; `build.py` generates everything in `tokens/dist/`. Planned to become the `kentigern-tokens` git submodule (see below). |
| `tokens/dist/` | Generated: `tokens.css` (custom properties, `light` and `dark` themes), `kentigern-light.mplstyle` / `kentigern-dark.mplstyle`, `kentigern-tokens.sty` (LaTeX colours). |
| `tokens/legacy/` | The earlier hand-written SCSS and TeX tokens, copied from the blog's vendored `_webpack/kentigern-tokens`. Kept until the blog is moved onto `dist/`. |
| `design-system/` | A mirror of the artifact: brand book (`README.md`, `charts.md`, `slides.md`, `social.md`, `print.md`), component previews, logo and icon assets, the d3 helper, and the artifact's own `design-system.json` index. |
| `latex/beamer/` | Beamer theme (`\usetheme{kentigern}`), an example deck and a preview image. |
| `charts/` | Python helper `kentigern_mpl.py` and `example.py`; renders `example-light.png` / `example-dark.png`. |

## Use

```python
import sys; sys.path.insert(0, "charts")
import kentigern_mpl as kn
kn.use("light")                       # or "dark"
ax.set_xlabel(kn.axis_label("Frequency", "Hz"))
colour = kn.run_colour("o4b")
```

```html
<link rel="stylesheet" href="tokens/dist/tokens.css">
<html data-theme="dark">  <!-- light is the default -->
```

```latex
\usepackage{kentigern-tokens}   % \knPrimary, \knInk, ... and \knPrimaryDark etc.
\kentigernhypersetup
```

## Changing the system

1. Edit `tokens/tokens.json` (colours, type, spacing, radii) or the guides in `design-system/`.
2. `make sync` regenerates `tokens/dist/` and copies `tokens.json` into `design-system/`.
3. `make check` fails if anything is stale.
4. Publish `design-system/` to the artifact to keep it in step (ask Claude to publish it, or use `/design-sync` in Claude Code where the appifacts plugin is installed). The artifact's `design-system.json` records its uploaded logo files by id; keep it with the files.

## Thesis class

The 2016 `kentigern.cls` that lived here has been removed (it remains in git history at commit `0fa3a46`). The maintained class is in [`kentigern-thesis`](https://github.com/transientlunatic/kentigern-thesis) (v1.0, 2025). Moving that class onto these tokens (Loch Teal links, Highland Rust citations, Lato, EB Garamond and Source Code Pro) is a change to that repository: load `kentigern-tokens.sty` from it.

## Status and known gaps

- `kentigern-tokens` is not yet a submodule: the repository could not be reached from the session that set this up, so `tokens/` is an ordinary directory that moves into it unchanged.
- `kentigern-tokens.sty` compiles (the Beamer theme builds on it), but the thesis class has not been moved onto it yet.
- No `.pptx` template yet; slides exist as HTML previews, a guide and a Beamer theme.
- The favicon is SVG only; no PNG or ICO exports.
- Logo outlines are from EB Garamond Italic (SIL Open Font License).

Licence: MIT (see `LICENSE`).
