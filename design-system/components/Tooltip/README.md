Tooltip and legend toggle for interactive charts.

The tooltip is `surface-raised` with a 1px `border-strong` outline, `radius-md`, `shadow-tooltip` and 7px 10px padding. First line: the series name in its own colour (bold) and the event in `site-mono`. Second line: values in `ink`. It never covers the point it describes: offset it 12px down and right of the cursor.

Legend toggles are `radius-pill` buttons with a 1px `rule` border (`border-strong` when active), a 10px dot in the series colour (a hollow ring means incomplete data) and the label in `ink`. Keyboard focus is a 2px `focus` outline.

The consumer provides the series name, colour token and values. Use `Kentigern.tooltip(container)` to get this behaviour in d3.
