# tokens

`tokens.json` is the source of truth for colours (light and dark), type, spacing, radii and shadow. Colour values are hex or `{alias}`; a token with no value for a theme inherits the first (`light`).

```
python3 build.py          # writes dist/
python3 build.py --check  # exits 1 if dist/ is stale
```

Outputs in `dist/`: `tokens.css`, `kentigern-light.mplstyle`, `kentigern-dark.mplstyle`, `kentigern-tokens.sty`.

`legacy/` holds the earlier hand-written SCSS/TeX tokens (Loch Teal, Highland Rust, Parchment, the `kn-cat` palette), which `tokens.json` was rebased on and extends with the observing-run colours, the sequential, terrain and diverging ramps, `grid-fine`, per-hue `on-*` text colours, spacing and radius scales.

This directory is intended to be the `kentigern-tokens` repository, included in `kentigern` as a git submodule.
