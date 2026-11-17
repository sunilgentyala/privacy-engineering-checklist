#!/usr/bin/env python3
"""Regenerate CHECKLIST.md from README.md. Use --check in CI to fail on drift."""
import pathlib
import re
import sys

TITLE = "Privacy Engineering Checklist"
RULE = "Sections 1 to 4 are blockers for launch. Sections 5 and 6 are hardening."
root = pathlib.Path(__file__).resolve().parent.parent


def build():
    s = (root / "README.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    out = [
        f"# {TITLE}: tick-box version",
        "",
        "Copy this into a pull request or review ticket. Tick an item only after you ran its test. "
        "The full text, tests, sources and the list of what was not verified are in the "
        f"[README](README.md). {RULE}",
        "",
    ]
    n = 0
    for line in s.split("\n"):
        if re.match(r"^## \d", line):
            out += ["", line, ""]
        elif line.startswith("- [ ] "):
            out.append("- [ ] " + line[6:].split(" *Test:*")[0].rstrip())
            n += 1
    out += ["", "Result: ____ of %d items ticked. Reviewer: ________  Date: ________" % n, ""]
    return "\n".join(out)


if __name__ == "__main__":
    target = root / "CHECKLIST.md"
    new = build()
    if "--check" in sys.argv:
        old = target.read_text(encoding="utf-8").replace("\r\n", "\n")
        if old != new:
            print("CHECKLIST.md is out of sync with README.md. Run: python scripts/sync_checklist.py")
            sys.exit(1)
        print("CHECKLIST.md is in sync.")
    else:
        target.write_text(new, encoding="utf-8", newline="\n")
        print("Wrote CHECKLIST.md")
