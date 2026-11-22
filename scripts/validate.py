#!/usr/bin/env python3
"""Basic deterministic validation for Wiki evidence, slide count and citations."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
source_paths = sorted((ROOT / "sources").glob("S*.md"))
html_path = ROOT / "index.html"
issues = []
if len(source_paths) < 5:
    issues.append(f"ingest sources < 5: {len(source_paths)}")
source_text = "\n".join(p.read_text(encoding="utf-8") for p in source_paths)
known = set(re.findall(r"S0[1-5]-E[1-9]", source_text))
for path in (ROOT / "wiki").glob("*.md"):
    for e in re.findall(r"S0[1-5]-E[1-9]", path.read_text(encoding="utf-8")):
        if e not in known: issues.append(f"未知證據卡：{path.name} {e}")
if not html_path.exists():
    issues.append("index.html 尚不存在")
else:
    html = html_path.read_text(encoding="utf-8")
    slides = re.findall(r'<section\b[^>]*class="slide[^"]*"[^>]*>', html)
    if not (8 <= len(slides) <= 15):
        issues.append(f"簡報頁數需 8–15，實際 {len(slides)}")
    for e in re.findall(r"S0[1-5]-E[1-9]", html):
        if e not in known: issues.append(f"HTML 未知來源：{e}")
    if len(re.findall(r'class="source"', html)) < len(slides):
        issues.append("並非每頁都有引用來源")
print(f"source files: {len(source_paths)}, evidence ids: {len(known)}")
print("PASS (static only)" if not issues else "FAIL (static):\n" + "\n".join("- "+i for i in issues))
print("瀏覽器渲染、文字忠實度及人工審核必須另行完成。")
sys.exit(bool(issues))
