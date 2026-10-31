# Slides

Slides are 1920 × 1080 (16:9), `dark` theme (put `data-theme="dark"` on the slide root), and use the `Slides` styles. Titles are the serif italic; the one bold typographic moment is the stat.

## Layouts

- **Title.** `slide-title` left, ripple arcs bottom-right, presenter and affiliation in `slide-body`. Optional logo slot top-left.
- **Stat.** One number in `slide-stat` and one label in `slide-stat-label`, centred, on a full-bleed `gold`, `red` or `blue` ground with the matching `on-gold`, `on-red` or `on-blue` text. At most three stat slides in a row. Use `gold` for the default, `red` for the one result the talk is about, `blue` for a calm third.
- **Figure and notes.** Title in `slide-h1`, notes left in `slide-body` (about 40% width), figure on a `panel` tile right (about 55%), `slide-ref` bottom-right. Three notes at most; bold one line with `slide-emphasis`.
- **Scorecard.** `slide-table`, left-aligned text and right-aligned tabular numbers, header in `ink-muted`, the current row on `gold` with `on-gold`. Put footnotes in `slide-ref` under the table.
- **Process.** Up to four steps as `primary` (teal) chevrons with `on-primary` text; the step the talk is about is `gold` with `on-gold`.

- **Thanks.** "Thanks!" in `slide-title`, the site address in mono in `primary`, a QR code on a `panel` tile, and the Glasgow footer: the Wellington cone and "Glasgow · 55.86° N, 4.25° W" in mono.

## Glasgow and the address

The system is named for St Kentigern (Mungo), Glasgow's patron saint. The one visible nod is the footer on the thanks slide: the traffic cone from the Duke of Wellington statue, in `orange`, beside the coordinates. It is the only icon allowed on a slide. The title slide carries `daniel-williams.co.uk` as the last presenter line, in mono. No other slide gets a URL footer; the bottom-left is for footnotes.

## Blueprint tone

The slide design began as a blueprint: a deep blue sheet with pale line work. Keep that as a tone and nothing more. A faint `grid-fine` grid may sit behind a diagram or chart slide; never behind text. No title blocks, dimension lines or stamps.

## Rules

- Title top-left at the same position on every content slide, one line, no full stop.
- Slide number bottom-right in `slide-ref`; nothing else lives in the footer.
- Body text is never below `slide-body` (40px at 1920). If it does not fit, cut words or split the slide.
- No accent lines under titles, no stripes down the edge, no centred paragraphs.
- Charts on slides reuse the Charts rules with labels at least 24px.
