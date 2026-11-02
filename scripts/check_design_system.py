#!/usr/bin/env python3
"""Check that design-system/ (the artifact mirror) is consistent with the tokens.

- design-system/tokens.json equals tokens/tokens.json
- every asset recorded in design-system.json exists on disk
- every component has a preview with a @dsCard marker, and a README (Cover excepted)
- every var(--x) in a preview, and every css('x') in the d3 helper, names a real token
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DS = ROOT / "design-system"
errors = []


def err(m):
    errors.append(m)


tokens = json.loads((ROOT / "tokens/tokens.json").read_text())
if (DS / "tokens.json").read_text() != (ROOT / "tokens/tokens.json").read_text():
    err("design-system/tokens.json differs from tokens/tokens.json (run: make sync)")

names = {t["name"] for fam in ("spacing", "radius", "shadow") for t in tokens[fam]["tokens"]}
names |= {t["name"] for t in tokens["color"]["tokens"]}
names |= {f"font-{k}" for k in tokens["type"]["families"]}

index = json.loads((DS / "design-system.json").read_text())
for group, g in index["assetGroups"].items():
    for fname in g["files"]:
        if not (DS / "assets" / group / fname).exists():
            err(f"design-system.json lists assets/{group}/{fname} but the file is missing")

comp = DS / "components"
for d in sorted(p for p in comp.iterdir() if p.is_dir()):
    prev = d / "preview.html"
    if not prev.exists():
        err(f"{d.name}: no preview.html")
        continue
    text = prev.read_text()
    if not text.startswith("<!-- @dsCard"):
        err(f"{d.name}/preview.html: line 1 must be the @dsCard marker")
    if d.name != "Cover" and not (d / "README.md").exists():
        err(f"{d.name}: no README.md")
    local = set(re.findall(r"(--[a-z0-9-]+)\s*:", text))
    for var in set(re.findall(r"var\((--[a-z0-9-]+)", text)):
        if var[2:] not in names and var not in local:
            err(f"{d.name}/preview.html: var({var}) is not a token")

helper = (DS / "assets/Charts/kentigern-d3.js").read_text()
for n in set(re.findall(r"css\('([a-z0-9-]+)'\)", helper)) | set(re.findall(r"'((?:cat|seq|div|terrain)-[a-z0-9]+)'", helper)):
    if n not in names:
        err(f"kentigern-d3.js reads unknown token {n!r}")

if errors:
    print("\n".join("FAIL " + e for e in errors))
    sys.exit(1)
n_assets = sum(len(g["files"]) for g in index["assetGroups"].values())
print(f"design-system ok: {len(list(comp.iterdir()))} components, {n_assets} recorded assets")
