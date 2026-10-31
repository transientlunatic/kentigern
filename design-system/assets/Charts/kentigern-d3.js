/* Kentigern d3 helper: reads the design tokens from CSS custom properties,
   so charts follow the page theme (data-theme="light" | "dark").
   Usage: <script src="kentigern-d3.js"></script> after d3, then Kentigern.* */
(function (global) {
  var base = document.documentElement, root = base;
  function css(name) { return getComputedStyle(root).getPropertyValue('--' + name).trim(); }
  var RUNS = ['o1', 'o2', 'o3a', 'o3b', 'o4a', 'o4b', 'o4c'];
  var CATEGORICAL = ['cat-1', 'cat-2', 'cat-3', 'cat-4', 'cat-5', 'cat-6', 'cat-other'];
  var K = {
    css: css,
    /* Read tokens from an element (e.g. a card with its own data-theme); scope(null) goes back to the page. */
    scope: function (el) { root = el || base; },
    runs: RUNS,
    run: function (id) { return css('run-' + String(id).toLowerCase()); },
    categorical: function () { return CATEGORICAL.map(css); },
    sequential: function () { return d3.interpolateRgbBasis([1, 2, 3, 4, 5, 6].map(function (i) { return css('seq-' + i); })); },
    terrain: function () { return d3.interpolateRgbBasis([1, 2, 3, 4, 5, 6].map(function (i) { return css('terrain-' + i); })); },
    diverging: function () { return d3.interpolateRgbBasis(['div-neg2', 'div-neg1', 'div-mid', 'div-pos1', 'div-pos2'].map(css)); },
    /* Style a d3 axis group: border-strong line, ticks outward, ink-muted 11px mono labels. */
    axis: function (g, opts) {
      opts = opts || {};
      g.selectAll('path,line').attr('stroke', css('border-strong'));
      g.selectAll('text').attr('fill', css('ink-muted')).attr('font-size', 11).attr('font-family', css('font-mono'));
      if (opts.noLine) g.select('.domain').remove();
      return g;
    },
    /* Gridlines in the light blue grid-fine; pass {minor: true} for the 0.5px minor lines of a log axis. */
    grid: function (g, opts) { g.selectAll('line').attr('stroke', css('grid-fine')).attr('stroke-width', opts && opts.minor ? 0.5 : 1); g.select('.domain').remove(); return g; },
    /* Axis title in the house form: K.axisTitle(svg, 'Frequency / Hz', x, y, rotate) */
    axisTitle: function (svg, text, x, y, rotate) {
      return svg.append('text').attr('x', x).attr('y', y).attr('text-anchor', 'middle').attr('font-size', 13).attr('fill', css('ink-muted')).attr('font-family', css('font-sans')).attr('transform', rotate ? 'rotate(-90 ' + x + ' ' + y + ')' : null).text(text);
    },
    /* A tooltip div inside container; show(html, event) / hide(). */
    tooltip: function (container) {
      var el = d3.select(container).style('position', 'relative').append('div')
        .style('position', 'absolute').style('pointer-events', 'none').style('opacity', 0)
        .style('background', css('surface-raised')).style('color', css('ink'))
        .style('border', '1px solid ' + css('border-strong')).style('border-radius', css('radius-lg'))
        .style('box-shadow', css('shadow-tooltip')).style('padding', '7px 10px')
        .style('font', '400 13px/1.4 ' + css('font-sans')).style('white-space', 'nowrap').style('z-index', 5);
      return {
        show: function (html, ev) {
          var r = container.getBoundingClientRect();
          el.html(html).style('opacity', 1).style('left', (ev.clientX - r.left + 12) + 'px').style('top', (ev.clientY - r.top + 12) + 'px');
        },
        hide: function () { el.style('opacity', 0); }
      };
    }
  };
  global.Kentigern = K;
})(window);
