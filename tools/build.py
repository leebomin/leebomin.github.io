#!/usr/bin/env python3
"""Build the site: python3 tools/build.py  (writes index.html and works/*.html next to tools/)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import INDEX, PAGES, PROJECTS_PAGE, CV_PAGE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ICON = {
 'gh': '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>',
 'velog': '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x=".5" y=".5" width="15" height="15" fill="none" stroke="currentColor"/><path d="M4.3 4.6l1.9-.3 1.1 5.6c.9-1.3 1.9-3.2 1.9-4.6 0-.5-.1-.8-.2-1l1.8-.4c.2.3.3.8.3 1.3 0 1.9-1.6 4.6-3.3 6.4H5.9z" fill="currentColor"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14"/><path d="M3 6l9 7 9-7"/></svg>',
 'arrow': '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M3 9l6-6M4 3h5v5"/></svg>',
}

def head(title, desc, pre):
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Inter+Tight:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
</head>
<body>
'''

def shell(pre, main, active):
    nav = [('About', 'index.html'), ('Projects', 'projects.html'), ('CV', 'cv.html')]
    navs = ''.join(f'<a href="{pre}{u}"{" class=on aria-current=page" if t == active else ""}>{t}</a>' for t, u in nav)
    icons = (f'<a href="https://github.com/leebomin" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">{ICON["gh"]}</a>'
             f'<a href="https://velog.io/@leebomin" target="_blank" rel="noopener" aria-label="velog" title="velog">{ICON["velog"]}</a>'
             f'<a href="mailto:ibomin88@gmail.com" aria-label="Email" title="ibomin88@gmail.com">{ICON["mail"]}</a>')
    return f'''<header class="topbar"><a class="nm" href="{pre}index.html">이보민</a><nav>{navs}</nav></header>
<div class="shell">
<aside class="side">
  <div>
    <a class="name" href="{pre}index.html">이보민<small>Bomin Lee · Data Scientist</small></a>
    <div class="photo" data-src="{pre}assets/img/portrait.png" aria-label="이보민 사진. 커서를 올리면 그 주변이, 누르면 사진 전체가 픽셀로 바뀝니다."></div>
    <nav>{navs}</nav>
  </div>
  <div class="foot"><div class="icons">{icons}</div><p class="copy">© 2026 Bomin Lee</p></div>
</aside>
<main class="main">
{main}
</main>
</div>
'''

def tail(pre, script=''):
    figs = f'<script src="{pre}assets/js/figs.js"></script>\n' if script else ''
    s = f'<script>\n{script}\n</script>\n' if script else ''
    return f'<script src="{pre}assets/js/main.js"></script>\n{figs}{s}</body>\n</html>\n'


def fix(b):
    return b.replace('{GH}', ICON['gh']).replace('{AR}', ICON['arrow'])
for fn, P, act in [('index.html', INDEX, 'About'), ('projects.html', PROJECTS_PAGE, 'Projects'), ('cv.html', CV_PAGE, 'CV')]:
    with open(os.path.join(ROOT, fn), 'w') as f:
        f.write(head(P['title'], P['desc'], '') + shell('', fix(P['body']), act) + tail(''))
os.makedirs(os.path.join(ROOT, 'works'), exist_ok=True)
for name, p in PAGES.items():
    body = p['body'] + f'''
<nav class="pager">
  <a href="{p["prev"][0]}"><span class="label">← Prev</span><span class="t">{p["prev"][1]}</span></a>
  <a href="{p["next"][0]}"><span class="label">Next →</span><span class="t">{p["next"][1]}</span></a>
</nav>'''
    with open(os.path.join(ROOT, 'works', name), 'w') as f:
        f.write(head(p['title'] + ' · 이보민', p['desc'], '../') + shell('../', fix(body), 'Projects') + tail('../', p['script']))
print('built', 3 + len(PAGES), 'pages')
