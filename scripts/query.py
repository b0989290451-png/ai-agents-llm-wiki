#!/usr/bin/env python3
"""Search only ingested Markdown knowledge; deterministic lexical retrieval."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = list((ROOT / "wiki").glob("*.md")) + list((ROOT / "sources").glob("S*.md"))

def query(term):
    tokens = [x.lower() for x in re.findall(r"[\w\u4e00-\u9fff-]+", term) if x]
    scored = []
    for path in FILES:
        contents = path.read_text(encoding="utf-8")
        score = sum(contents.lower().count(t) for t in tokens)
        if score:
            ids = sorted(set(re.findall(r"S0[1-5]-E[1-9]", contents)))
            scored.append((score, path, ids, contents))
    return sorted(scored, key=lambda item: (-item[0], str(item[1])))

if __name__ == "__main__":
    term = " ".join(sys.argv[1:]).strip()
    if not term:
        sys.exit('用法：python scripts/query.py "agent loop"')
    for score, path, ids, content in query(term)[:8]:
        print(f"\n[{score}] {path.relative_to(ROOT)} | Evidence: {', '.join(ids) or '請回查來源'}")
        print("  " + re.sub(r"\s+", " ", content)[:240] + "...")
