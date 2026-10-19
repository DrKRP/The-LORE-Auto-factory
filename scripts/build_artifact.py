#!/usr/bin/env python3
"""Build a single-file, shareable player page with one module built in.

    python3 scripts/build_artifact.py <module.json> <out.html>

The output has no <html>/<head>/<body> wrapper (the Artifact host adds one) and needs
no network: the module JSON is inlined as window.LORE_MODULE.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
mod = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
html = (ROOT / "player" / "index.html").read_text(encoding="utf-8")
style = re.search(r"<style>.*?</style>", html, re.S).group(0)
body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
# Side gutters that clear a phone's system bars.
style = style.replace("padding: 10px 16px;", "padding: 10px max(16px, env(safe-area-inset-right, 0px)) 10px max(16px, env(safe-area-inset-left, 0px));")
# Hosted pages cannot start downloads; keep only the copy button.
body = body.replace('`</ol><div class="row"><button id="export">Download session record</button>', '`</ol><div class="row">')
body = re.sub(r'  if \(\$\("export"\)\) \$\("export"\)\.onclick = \(\) => \{.*?\n  \};\n', "", body, flags=re.S)
data = json.dumps(mod, ensure_ascii=False).replace("</", "<\\/")
page = (f"<title>{mod.get('title', 'LORE journey')}</title>\n"
        f"{style}\n<script>window.LORE_MODULE = {data};</script>\n{body}")
Path(sys.argv[2]).write_text(page, encoding="utf-8")
print(f"wrote {sys.argv[2]} ({len(page) // 1024} KB)")
