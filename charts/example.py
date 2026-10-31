"""Render the example figures: python3 example.py"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import kentigern_mpl as kn

OUT = Path(__file__).parent
# BBH candidates per run, from the GWTC-5.0 scorecard
RUNS = [("O1", 3), ("O2", 7), ("O3a", 42), ("O3b", 31), ("O4a", 128), ("O4b", 161), ("O4c", 2)]

for theme in ("light", "dark"):
    kn.use(theme)
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.6), constrained_layout=True)
    for i, (r, n) in enumerate(RUNS):
        c = kn.run_colour(r, theme)
        partial = r == "O4c"
        a.bar(i, n, color="none" if partial else c, edgecolor=c if partial else "none", linewidth=1.6, linestyle="--" if partial else "-")
        a.text(i, n + 4, str(n), ha="center", color=kn.colour("ink", theme), fontweight="bold")
    a.set_xticks(range(len(RUNS)), [r for r, _ in RUNS])
    a.set_yticks([])
    a.spines["left"].set_visible(False)
    a.set_title("O4b added 161 binary black hole candidates", loc="left", family="serif", style="italic", fontsize=12)
    kn.mono_ticks(a)
    x = np.logspace(0.7, 2, 60)
    med = 3.2 * (x / 8) ** -2.1 + 1.2 * np.exp(-0.5 * ((x - 35) / 5) ** 2)
    w = lambda k: np.exp(k * (0.35 + 0.5 * np.abs(np.log(x / 20)) / np.log(5)))
    c = kn.run_colour("o3b", theme)
    kn.credible_band(b, x, med, med / w(0.45), med * w(0.45), med / w(1), med * w(1), c)
    b.plot(x, 2.6 * (x / 8) ** -2.4, color=kn.colour("grey", theme), linestyle="--", linewidth=1.4)
    kn.label_line(b, 40, 0.02, "Illustrative shape, not data", kn.colour("ink-muted", theme))
    b.set_xscale("log"); b.set_yscale("log")
    b.set_xlabel(kn.axis_label("Primary mass", "$M_\\odot$"))
    b.set_ylabel(kn.axis_label("Rate density", "arbitrary"))
    kn.mono_ticks(b)
    fig.savefig(OUT / f"example-{theme}.png", dpi=150)
    print("wrote", f"example-{theme}.png")
