`kentigern-d3.js` reads the Kentigern colour tokens from CSS custom properties, so a chart takes `light` or `dark` from the page. It has no build step and needs d3 v7 loaded first.

It exposes `Kentigern.run('o4a')` (run colour), `.categorical()`, `.sequential()`, `.terrain()` and `.diverging()` (d3 interpolators over the seq and div tokens), `.axis(g)`, `.grid(g, {minor})` and `.axisTitle(svg, 'Quantity / unit', x, y, rotate)` to style an axis group, its gridlines and its title, and `.tooltip(container)` which returns `{show(html, event), hide()}`. Call `.scope(element)` to read tokens from an element that has its own `data-theme`, and `.scope(null)` to go back to the page. Mark everything else with `Kentigern.css('token-name')`; never type a hex.

The file is plain JavaScript, not an image, and carries no ink of its own.
