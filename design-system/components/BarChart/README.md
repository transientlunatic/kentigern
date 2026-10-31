Bar chart by observing run, the house pattern for counts.

Each bar takes its `run-*` colour with a 2px corner radius, a value label above it in `ink`, gridlines in `rule`, axes in `border-strong` with `ink-muted` 11px labels. The partial run is drawn with a dashed outline and no fill. Hover shows a tooltip.

The consumer provides `[label, value]` pairs and a figure caption in `site-caption` that names the source. It needs d3 v7 and `assets/Charts/kentigern-d3.js`. Do not add a legend when the x-axis already names every run, and do not colour bars by value.
