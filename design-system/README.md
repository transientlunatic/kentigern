Kentigern, after Glasgow's patron saint, is the visual language for a physicist's writing: a long-form blog, conference talks and interactive d3 figures. It is dark by default, sparing with colour, and lets the data be the loudest thing on the page.

## Content fundamentals

- Write as one researcher talking to peers. First person is fine ("we've released", "we think"), hedged claims stay hedged ("likely", "consistent with"), and nothing is hyped.
- Sentence case everywhere, including slide titles: "Source masses", "Defining thresholds". Event names keep their own case and are set in `site-mono` or inline code: `GW231123_135430`.
- Say what the number means, right under it. A stat is never alone: "104 — New candidates from O4b with full parameter estimation results".
- Small asides are allowed and welcome: "O4 is now a bit longer…". No emoji, no exclamation marks except a closing "Thanks!".
- Cite the paper on the slide that shows its figure: arXiv link in `slide-ref`, bottom-right.

## Visual foundations

- **Ground.** `light` is the default: `surface` Parchment, `surface-raised` white, `ink` warm near-black, `primary` Loch Teal. `dark` (`surface` #0E1521) is for slides, interactive figures and the site's dark mode. Never hard-code a hex; read tokens.
- **Blueprint.** Slides began as blueprints: a deep blue sheet with pale line work. The `dark` theme with `primary` teal line work and `grid-fine` gridlines keeps that tone. It is a tone, not a theme: no title blocks or decorative drafting marks.
- **Colour.** Teal and ink do most of the work. `secondary` (Highland Rust) is for emphasis and danger. Data colour comes from `cat-1` to `cat-6` (`gold`, `blue`, `orange`, `indigo`, `green`, `red`) and `cat-other`; text on any of those fills is the matching `on-gold`, `on-blue`, and so on. The extended palette (`tan`, `ocean`, `ice`, `sky`, `purple`, `magenta`, `rust`, `teal-bright`, `lime`) is for tags, badges and map-adjacent work.
- **Type.** Headings are `site-h2` / `slide-h1`: the serif (EB Garamond), italic, regular weight. Body and UI are `site-body` (Lato 300). The single heavy moment is `slide-stat`: Lato Black Italic, huge, centred. Citations, event names and code are Source Code Pro.
- **Surfaces.** Flat. Separate regions with `surface-raised` or a `rule` hairline, never a drop shadow; `shadow-tooltip` is for hover tooltips only. No gradients, no accent stripes on cards.
- **Shape.** Corners stay small: `radius-md` (4px) for buttons and inputs, `radius-lg` (8px) for cards, tooltips, chart panels and slide tiles, `radius-sm` (2px) for table highlights, `radius-pill` for filter buttons.
- **Spacing.** Multiples of 4px from `space-1` to `space-9`. A slide's outer margin is `space-9`; a page's section gap is `space-6`.
- **Links.** `link` (teal; lavender on dark), `link-visited` after. Underline appears on hover.
- **Focus.** 2px solid `focus` ring, offset 2px, on every interactive element.
- **Motion.** None decorative. Chart transitions are 200ms ease-out and only when the data changes.

## Iconography

The site uses Font Awesome 6 (solid, `fa` class) for share and social links at body size, coloured `ink-muted`. Slides and figures use no icons: say it in words or draw it with the data. The one exception is the traffic cone beside the coordinates on the thanks slide, a Glasgow joke. Never use emoji.

## Imagery

Figures are the imagery. Place a published figure on a `panel` tile so its white background looks intentional on the dark slide, and keep its aspect ratio. Dark-ground figures made in d3 sit directly on `surface`. The personal wordmark (see the Logo card) goes top-left on the title slide and in the site header; institutional logos are optional and go in a slot beside it, sized to the cap height of `slide-title`.

## Fonts

Lato (sans), EB Garamond (serif) and Source Code Pro (mono), all free. On the site they load from Google Fonts; in PowerPoint and LaTeX they must be installed.
