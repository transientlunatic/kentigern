The colour roles for charts: one colour per observing run, a six-step sequential ramp, a six-step terrain ramp and a five-step diverging ramp.

Always draw O1 to O4b with `run-o1` … `run-o4b`, in order, in every chart and legend. Partial runs (O4c) are drawn dashed or hollow in `run-o4c`. Use the seq tokens for counts and densities, the terrain tokens for elevation and anything shown beside the map, and div tokens only for quantities with a meaningful zero.

The consumer reads the tokens through `Kentigern.run()`, `.sequential()` and `.diverging()` from `assets/Charts/kentigern-d3.js`. Never rely on colour alone: label direct, or add a marker shape.
