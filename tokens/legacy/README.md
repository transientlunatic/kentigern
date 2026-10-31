# kentigern-tokens

Design tokens for the Kentigern design system — shared across the Jekyll personal site, the Sphinx documentation theme, and LaTeX documents.

## Files

| File | Purpose |
|---|---|
| `_tokens.scss` | Canonical token definitions — no Bootstrap dependency |
| `_bootstrap-overrides.scss` | Maps tokens to Bootstrap 5 `$variables` |
| `_css-properties.scss` | Exports tokens as CSS custom properties (runtime theming) |
| `tokens.tex` | LaTeX colour and font definitions |

## Usage

### Web (Webpack + Bootstrap 5)

```scss
// Import in this order:
@import "kentigern-tokens/tokens";             // 1. Token vars
@import "kentigern-tokens/bootstrap-overrides"; // 2. BS5 overrides
@import "bootstrap/scss/bootstrap";            // 3. Bootstrap
@import "kentigern-tokens/css-properties";     // 4. CSS custom props
```

### LaTeX (XeLaTeX / LuaLaTeX)

```latex
\usepackage{xcolor}
\usepackage{fontspec}
\usepackage{hyperref}
\input{kentigern-tokens}
\kentigernhypersetup   % coloured hyperlinks
\kentigernfonts        % Lato + Source Code Pro
```

## Colour Palette

| Token | Value | Use |
|---|---|---|
| `$kn-primary` | `#2D6A7F` | Loch Teal — links, active nav, headings |
| `$kn-secondary` | `#962C26` | Highland Rust — emphasis, danger |
| `$kn-parchment` | `#F4F2F0` | Page background |
| `$kn-ink` | `#2C1E10` | Body text |
| `$kn-dark-link` | `#BE81F0` | Dark-mode links |

### Data-visualisation palette

Six categorical hues (`--kn-cat-1` … `--kn-cat-6`, with `--kn-party-snp/con/ld/ref/grn/lab` as aliases and `--kn-cat-other`
for the unassigned series), plus chart furniture (`--kn-viz-bg/ink/ink2/muted/grid/axis/ring/neutral`) and semantic colours
(`--kn-viz-pos/neg/seq/good/warn`). Each has a light-surface and a dark-surface step that switch with
`[data-bs-theme="dark"]`, so charts follow the site's theme picker and need no `prefers-color-scheme` logic of their own.
Read them in SVG/CSS with `var(--kn-cat-1)`, or in JS with `getComputedStyle(el).getPropertyValue('--kn-cat-1')`.

The set was checked for colour-vision-deficiency separation on both surfaces. Light mode has two known WARN results
(adjacent-pair CVD 7.2, and the yellow at 2.2:1 contrast on the page), so a chart using it must also carry direct labels, a
legend, distinct marker shapes and a table view, never colour alone.

## Integration via Git Submodule

```bash
# In your project root:
git submodule add https://github.com/transientlunatic/kentigern-tokens <path>

# Update to latest:
git submodule update --remote
```
