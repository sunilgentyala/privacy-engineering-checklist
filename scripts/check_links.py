#!/usr/bin/env python3
"""Check every http(s) link in the top-level markdown files.

Hard-fails on 404, 410 and network errors. Sites that block automated clients
(403, 429, 999) are reported as warnings only.
"""
import pathlib
import re
import sys
import urllib.error
import urllib.request

root = pathlib.Path(__file__).resolve().parent.parent
urls = {}
for f in root.glob("*.md"):
    text = f.read_text(encoding="utf-8")
    for m in re.finditer(r"https?://[^\s)>\"'`]+", text):
        urls.setdefault(m.group(0).rstrip(".,;"), f.name)

bad, warn = [], []
for u, f in sorted(urls.items()):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (link-check)"})
    code = None
    for _ in range(2):
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                code = r.status
            break
        except urllib.error.HTTPError as e:
            code = e.code
            break
        except Exception as e:  # network error, retry once
            code = repr(e)
    if isinstance(code, int) and code < 400:
        continue
    (warn if code in (403, 429, 999) else bad).append((code, u, f))

for c, u, f in warn:
    print(f"WARN {c} {u} ({f})")
for c, u, f in bad:
    print(f"FAIL {c} {u} ({f})")
print(f"{len(urls)} links checked, {len(bad)} failed, {len(warn)} warnings")
sys.exit(1 if bad else 0)
