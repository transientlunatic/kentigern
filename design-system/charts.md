# Charts

Interactive figures are written in d3 and take every colour from the tokens, so the same code is right on `light` and `dark`. Copy `assets/Charts/kentigern-d3.js` next to the chart and read colours through it instead of typing hex values.

## Colour roles

- **Categorical, by observing run.** O1 `run-o1` (red), O2 `run-o2` (orange), O3a `run-o3a` (indigo), O3b `run-o3b` (blue), O4a `run-o4a` (gold), O4b `run-o4b` (green), always in that order in every chart and legend. A run keeps its colour across the whole site and deck. O4c (`run-o4c`, grey) is partial: draw it hollow or dashed.
- **Other categories.** Take `cat-1` to `cat-6` in order and `cat-other` for the rest. Six is the limit. The set separates well for colour-blind viewers on the dark theme but has two known weak spots on light: adjacent pairs, and gold at 1.9:1 on parchment. So always add direct labels, marker shapes or a table; never colour alone.
- **Semantic.** `viz-pos` (red) and `viz-neg` (blue) for positive and negative change, `viz-good` and `viz-warn` for status, each with a word or icon.
- **Sequential.** `seq-1` to `seq-6` for counts, densities and volumes. Light-to-dark follows 'more' against the ground. Label the scale with numbers; do not rely on colour alone.
- **Terrain.** `terrain-1` to `terrain-6`, the hillshade creams and shadow browns sampled from the site's map tiles. Use it for elevation, map-based density or anything read as relief, and for charts that sit beside the map. Use the blue sequential ramp for counts.
- **Diverging.** `div-neg2` to `div-pos2` only for a quantity with a meaningful zero (residuals, a spin that can be either sign). Zero is `div-mid`.
- **Reference.** Priors, thresholds and the line y = x are `grey`, dashed, 1.5px.

## Marks and furniture

- Points: 4–5px radius, `fill` at 0.85 opacity, no stroke, on `surface`. Dense scatter dims to 0.6.
- Lines: 2.2px, round joins and caps. Highlighted series 3.6px.
- Uncertainty: draw credible intervals as filled bands behind the line: 90% at 0.18 opacity, 50% at 0.3, same hue. Label them 'credible', never 'confidence'. Posterior densities are filled with the same 0.3 opacity and outlined at full strength.
- Axes: ticks point outward. Tick labels are mono (`site-mono` family) in `ink-muted` at 11px; axis titles are sans in `ink-muted`, written `Quantity / unit`: `Latitude / deg`, `Frequency / Hz`, `Strain / Hz^-1/2`. The axis line is `border-strong`.
- Frames: none by default. Erase every line that carries no data, so small multiples and charts in text sit on the ground with axes only. A single standalone plot may take a thin `border-strong` frame when it helps it read as a figure; never frame small multiples.
- Gridlines: `grid-fine`, the light blue, at 1px for major and 0.5px for the minor lines of a log axis. None on the category axis of a bar chart. On dark slides the grid is a faint blue behind the data.
- Panels: a chart sits on `surface-raised` with `radius-md` and `space-4` padding on the site; it sits straight on `surface` in a slide.
- Tooltips: `surface-raised`, `border-strong` 1px, `radius-md`, `shadow-tooltip`, 7px 10px padding, series name in its own colour then values in `ink`.
- Direct labels: for four series or fewer, drop the legend and write each name in its series colour at 11px, set along the curve near its end and turned to the slope of the line (LISA and DECIGO in red and blue). Use a legend only when the labels would collide.
- Points of interest on maps and scatter: a 3px `ink` dot with a 10px mono `ink-muted` label, as for summits. Contours are thin `orange`-family lines, 0.8px, at 0.6 opacity.
- Legends: pill toggles (`radius-pill`, 1px `rule` border). A hollow marker means incomplete data.

## Do and don't

- Do label the highlighted point or series directly in its colour.
- Do write axis titles as `Quantity / unit`, e.g. `m₁ / M☉`. Do not use square brackets.
- Do set the caption under a figure in `site-figcaption`: bold figure number, then the text.
- Don't use `red` and `green` as the only difference between two series; `blue` vs `red`, or lightness, separates them.
- Don't set `gold` text on `light`: it is for marks and fills only. Use `ink` for the label next to it.
