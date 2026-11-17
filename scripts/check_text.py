#!/usr/bin/env python3
"""Fail if any text file in the repo contains an em dash (style rule for these checklists)."""
import pathlib
import sys

EM_DASH = chr(0x2014)
root = pathlib.Path(__file__).resolve().parent.parent
skip = {".git"}
bad = []
for p in root.rglob("*"):
    if not p.is_file() or skip & set(p.parts) or p.suffix.lower() in {".gif", ".png", ".jpg"}:
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"NOT UTF-8: {p.relative_to(root)}")
        bad.append(p)
        continue
    if EM_DASH in text:
        print(f"em dash in {p.relative_to(root)}")
        bad.append(p)
print(f"{len(bad)} problem file(s)")
sys.exit(1 if bad else 0)
