"""Kentigern helpers for matplotlib.

    import kentigern_mpl as kn
    kn.use("light")                      # or "dark"
    ax.set_xlabel(kn.axis_label("Frequency", "Hz"))     # -> "Frequency / Hz"

Colours come from ../tokens/tokens.json, so they never drift from the design system.
"""
import json
import re
from pathlib import Path

import matplotlib.pyplot as plt

_TOKENS = Path(__file__).resolve().parent.parent / "tokens"
_DATA = json.loads((_TOKENS / "tokens.json").read_text())
_COLORS = {t["name"]: t["value"] for t in _DATA["color"]["tokens"]}

RUNS = ["o1", "o2", "o3a", "o3b", "o4a", "o4b", "o4c"]


def colour(name, theme="light"):
    """Resolve a colour token (following {aliases}) to '#rrggbb[aa]'."""
    v = _COLORS[name]
    v = v if isinstance(v, str) else v.get(theme, v["light"])
    m = re.fullmatch(r"\{(.+)\}", v)
    return colour(m.group(1), theme) if m else v


def run_colour(run, theme="light"):
    """Observing-run colour, e.g. run_colour('o4b'). O4c is partial: draw it hollow or dashed."""
    return colour(f"run-{run.lower()}", theme)


def use(theme="light"):
    plt.style.use(_TOKENS / "dist" / f"kentigern-{theme}.mplstyle")
    return theme


def axis_label(quantity, unit=None):
    """House axis title: 'Quantity / unit'. No square brackets."""
    return f"{quantity} / {unit}" if unit else quantity


def mono_ticks(ax):
    """Tick labels in the mono family, as in the thesis figures."""
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_family("monospace")


def label_line(ax, x, y, text, color, rotation=0, **kw):
    """Direct label in the series colour, instead of a legend."""
    return ax.text(x, y, text, color=color, rotation=rotation, fontsize=9, ha="left", va="bottom", **kw)


def credible_band(ax, x, median, lo50, hi50, lo90, hi90, color):
    """Median with nested 50% and 90% credible bands (0.3 and 0.18 opacity)."""
    ax.fill_between(x, lo90, hi90, color=color, alpha=0.18, linewidth=0)
    ax.fill_between(x, lo50, hi50, color=color, alpha=0.30, linewidth=0)
    return ax.plot(x, median, color=color, linewidth=2.2)[0]
