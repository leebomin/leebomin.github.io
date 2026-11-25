#!/usr/bin/env python3
"""Generate the project pages (works/*.html) from the page bodies in pages.py."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES

OUT = sys.argv[1]
GH = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>'
LINKS = {1: 'p01.html', 2: 'p02.html', 3: 'p03.html', 4: 'p04.html', 5: 'more.html#p05', 6: 'more.html#p06', 7: 'more.html#p07', 8: 'more.html#p08'}


def tracker(on):
    out = []
    for i in range(1, 9):
        if i == 5:
            out.append('<span class="sep"></span>')
        cls = ' class="on"' if i in on else ''
        out.append(f'<a href="{LINKS[i]}"{cls}>P0{i}</a>')
    return ''.join(out)


def page(p):
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p["title"]} · 이보민</title>
<meta name="description" content="{p["desc"]}">
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
<header class="run">
  <a class="brand" href="../index.html">LEE BOMIN<span class="long"> — PORTFOLIO</span></a>
  <nav class="tracker" aria-label="프로젝트">{tracker(p["on"])}</nav>
  <span class="where">{p["where"]}</span>
</header>
<main class="wrap">
{p["body"]}
<nav class="pager">
  <a href="{p["prev"][0]}"><span class="label">← PREV</span><span class="t">{p["prev"][1]}</span></a>
  <a href="{p["next"][0]}"><span class="label">NEXT →</span><span class="t">{p["next"][1]}</span></a>
</nav>
</main>
<footer class="foot"><span>© 2026 LEE BOMIN</span><a href="../index.html#works">ALL WORKS ↑</a></footer>
<script src="../assets/js/main.js"></script>
<script src="../assets/js/figs.js"></script>
<script>
{p["script"]}
</script>
</body>
</html>
'''


os.makedirs(os.path.join(OUT, 'works'), exist_ok=True)
for name, p in PAGES.items():
    p['body'] = p['body'].replace('{GH}', GH)
    with open(os.path.join(OUT, 'works', name), 'w') as f:
        f.write(page(p))
    print('wrote', name)
