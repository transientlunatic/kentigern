#!/usr/bin/env python3
"""Validate tokens.json: structure, aliases and WCAG contrast of the documented pairs.

    python3 check.py        exits 1 on any problem

Contrast pairs are the ones the usage notes promise. Pairs that are known to miss are
listed in KNOWN with the reason; the check fails if a pair outside KNOWN misses, and also
if a KNOWN pair now passes (so the note can be removed).
"""
import json
import re
import sys
from pathlib import Path

T = json.loads((Path(__file__).parent / "tokens.json").read_text())
THEMES = [t["id"] for t in T["color"]["themes"]]
COLORS = {t["name"]: t for t in T["color"]["tokens"]}
HEX = re.compile(r"^#(?:[0-9a-f]{3}|[0-9a-f]{4}|[0-9a-f]{6}|[0-9a-f]{8})$")
NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
errors = []


def err(msg):
    errors.append(msg)


# ---- structure ------------------------------------------------------------------
seen = {}
families = [("color", T["color"]["tokens"])] + [(f, T[f]["tokens"]) for f in ("spacing", "radius", "shadow") if f in T]
for fam, toks in families:
    for t in toks:
        n = t["name"]
        if not NAME.match(n):
            err(f"bad token name: {n!r}")
        if n in seen:
            err(f"duplicate token name across families: {n} ({seen[n]} and {fam})")
        seen[n] = fam
        if not t.get("usage"):
            err(f"{n}: missing usage note")


def resolve(name, theme, trail=()):
    if name in trail:
        err(f"alias cycle: {' -> '.join(trail + (name,))}")
        return "#000000"
    if name not in COLORS:
        err(f"alias of missing token: {name}")
        return "#000000"
    v = COLORS[name]["value"]
    v = v if isinstance(v, str) else v.get(theme, v.get(THEMES[0]))
    m = re.fullmatch(r"\{(.+)\}", v or "")
    if m:
        return resolve(m.group(1), theme, trail + (name,))
    if not v or not HEX.match(v):
        err(f"{name} [{theme}]: not a hex colour or alias: {v!r}")
        return "#000000"
    return v


RES = {th: {n: resolve(n, th) for n in COLORS} for th in THEMES}
for th in THEMES:
    for n, t in COLORS.items():
        v = t["value"]
        if isinstance(v, dict) and th not in v and th != THEMES[0]:
            pass  # inherits the first theme, allowed


# ---- contrast ---------------------------------------------------------------------
def lum(h):
    h = h.lstrip("#")[:6]
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]

    def f(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


PAIRS = []  # (fg, bg, minimum)
for g in ("surface", "surface-raised"):
    PAIRS += [("ink", g, 4.5), ("ink-muted", g, 4.5), ("link", g, 4.5), ("primary", g, 4.5), ("secondary", g, 4.5)]
    PAIRS += [("focus", g, 3.0), ("border-strong", g, 3.0)]
PAIRS += [("link-visited", "surface", 4.5), ("on-panel", "panel", 4.5), ("on-primary", "primary", 4.5), ("on-secondary", "secondary", 4.5)]
for h in ("gold", "blue", "orange", "indigo", "green", "red"):
    PAIRS.append((f"on-{h}", h, 4.5))
for i in range(1, 7):
    PAIRS.append((f"cat-{i}", "surface", 3.0))   # marks need 3:1

KNOWN = {  # (fg, bg, theme): reason
    ("on-blue", "blue", "light"): "large text only (4.4:1); documented on the token",
    ("on-red", "red", "light"): "large text only (4.1:1); documented on the token",
    ("cat-1", "surface", "light"): "gold is 1.9:1 on Parchment; series need direct labels (documented)",
    ("cat-3", "surface", "light"): "orange is 2.9:1 on Parchment; series need direct labels (documented)",
}
for th in THEMES:
    for fg, bg, minimum in PAIRS:
        r = ratio(RES[th][fg], RES[th][bg])
        key = (fg, bg, th)
        if r < minimum and key not in KNOWN:
            err(f"contrast {fg} on {bg} [{th}] is {r:.2f}:1, needs {minimum}:1")
        if r >= minimum and key in KNOWN:
            err(f"{fg} on {bg} [{th}] now passes ({r:.2f}:1); remove it from KNOWN")

# ---- sequential ramps keep their steps distinguishable --------------------------------
for th in THEMES:
    for fam in ("seq", "terrain"):
        for i in range(1, 6):
            r = ratio(RES[th][f"{fam}-{i}"], RES[th][f"{fam}-{i + 1}"])
            if r < 1.2:
                err(f"{fam}-{i}/{i + 1} [{th}] steps differ by only {r:.2f}:1")

if errors:
    print("\n".join("FAIL " + e for e in errors))
    sys.exit(1)
print(f"tokens ok: {len(COLORS)} colours x {len(THEMES)} themes, {len(PAIRS) * len(THEMES)} contrast pairs checked")
