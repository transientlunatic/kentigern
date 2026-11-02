#!/usr/bin/env python3
"""Build the Kentigern token outputs from tokens.json.

    python3 build.py            writes dist/tokens.css, dist/kentigern-light.mplstyle,
                                dist/kentigern-dark.mplstyle and dist/kentigern-tokens.sty
    python3 build.py --check    exits 1 if dist/ is out of date

tokens.json is the single source of truth. Colour values are hex or {alias}; each colour
has a value per theme ("light", "dark").
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
T = json.loads((HERE / "tokens.json").read_text())
THEMES = [t["id"] for t in T["color"]["themes"]]
FIRST = THEMES[0]
COLORS = {t["name"]: t["value"] for t in T["color"]["tokens"]}


def val(name, theme):
    v = COLORS[name]["value"] if "value" in COLORS[name] else COLORS[name]
    v = v if isinstance(v, str) else v.get(theme, v[FIRST])
    m = re.fullmatch(r"\{(.+)\}", v)
    return val(m.group(1), theme) if m else v


def hexrgb(h):
    h = h.lstrip("#")
    return h[:6].upper()


def css():
    out = ["/* Kentigern: generated from tokens.json by build.py. Do not edit. */"]
    for theme in THEMES:
        sel = f':root, [data-theme="{theme}"]' if theme == FIRST else f'[data-theme="{theme}"]'
        lines = [f"  --{n}: {val(n, theme)};" for n in COLORS]
        for t in T.get("shadow", {}).get("tokens", []):
            v = t["value"]
            lines.append(f"  --{t['name']}: {v if isinstance(v, str) else v.get(theme, v[FIRST])};")
        out.append(sel + " {\n" + "\n".join(lines) + "\n  color-scheme: " + ("dark" if theme == "dark" else "light") + ";\n}")
    root = []
    for fam in ("spacing", "radius"):
        root += [f"  --{t['name']}: {t['value']};" for t in T[fam]["tokens"]]
    root += [f"  --font-{k}: {v};" for k, v in T["type"]["families"].items()]
    out.append(":root {\n" + "\n".join(root) + "\n}")
    for g in T["type"]["groups"]:
        for s in g["styles"]:
            fam = s.get("family", g["family"])
            rules = [
                f"font-family: var(--font-{fam});",
                f"font-size: {s['fontSize']};",
                f"line-height: {s['lineHeight']};",
                f"font-weight: {s['fontWeight']};",
            ]
            if s.get("fontStyle"):
                rules.append(f"font-style: {s['fontStyle']};")
            if s.get("letterSpacing"):
                rules.append(f"letter-spacing: {s['letterSpacing']};")
            out.append(f".{s['name']} {{ " + " ".join(rules) + " }")
    return "\n".join(out) + "\n"


def mpl(theme):
    def g(n):
        return val(n, theme).lstrip("#")[:6]

    cycle = [g(f"cat-{i}") for i in range(1, 7)]
    return f"""# Kentigern matplotlib style ({theme}): generated from tokens.json by build.py. Do not edit.
# Use:  plt.style.use("kentigern-{theme}.mplstyle")
figure.facecolor: {g('surface')}
savefig.facecolor: {g('surface')}
savefig.dpi: 300
axes.facecolor: {g('surface')}
axes.edgecolor: {g('border-strong')}
axes.labelcolor: {g('ink-muted')}
axes.titlecolor: {g('ink')}
axes.linewidth: 0.8
axes.spines.top: False
axes.spines.right: False
axes.grid: False
axes.axisbelow: True
axes.prop_cycle: cycler('color', {cycle!r})
grid.color: {g('grid-fine')}
grid.linewidth: 0.6
text.color: {g('ink')}
xtick.color: {g('border-strong')}
ytick.color: {g('border-strong')}
xtick.labelcolor: {g('ink-muted')}
ytick.labelcolor: {g('ink-muted')}
xtick.direction: out
ytick.direction: out
xtick.major.size: 3.5
ytick.major.size: 3.5
lines.linewidth: 2.0
lines.solid_capstyle: round
lines.solid_joinstyle: round
patch.linewidth: 0
legend.frameon: False
legend.labelcolor: {g('ink')}
font.family: sans-serif
font.sans-serif: Lato, DejaVu Sans
font.serif: EB Garamond, DejaVu Serif
font.monospace: Source Code Pro, DejaVu Sans Mono
font.size: 10
mathtext.fontset: stix
"""


def camel(n):
    return "".join(p.capitalize() for p in re.split(r"[-_]", n))


def sty():
    L = ["% Kentigern LaTeX colours: generated from tokens.json by build.py. Do not edit.",
         "\\NeedsTeXFormat{LaTeX2e}", "\\ProvidesPackage{kentigern-tokens}[2026/10/30 Kentigern design tokens]",
         "\\RequirePackage{xcolor}", "% Light theme as kn<Name>; dark theme as kn<Name>Dark."]
    for n in COLORS:
        for theme, suf in (("light", ""), ("dark", "Dark")):
            if theme in THEMES:
                L.append(f"\\definecolor{{kn{camel(n)}{suf}}}{{HTML}}{{{hexrgb(val(n, theme))}}}")
    L += ["% Hyperlinks in the thesis: teal links, rust citations.",
          "\\newcommand{\\kentigernhypersetup}{\\hypersetup{colorlinks=true,linkcolor=knLink,urlcolor=knLink,citecolor=knSecondary,filecolor=knLink}}",
          "\\endinput"]
    return "\n".join(L) + "\n"


OUT = {
    "dist/tokens.css": css(),
    "dist/kentigern-light.mplstyle": mpl("light"),
    "dist/kentigern-dark.mplstyle": mpl("dark"),
    "dist/kentigern-tokens.sty": sty(),
}
if __name__ == "__main__":
    bad = 0
    for p, s in OUT.items():
        f = HERE / p
        if "--check" in sys.argv:
            if not f.exists() or f.read_text() != s:
                print("stale:", p)
                bad = 1
        else:
            f.parent.mkdir(exist_ok=True)
            f.write_text(s)
            print("wrote", p)
    sys.exit(bad)
