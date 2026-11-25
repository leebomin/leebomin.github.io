# leebomin.github.io

이보민 포트폴리오 웹사이트 · https://leebomin.github.io

- `index.html` — 표지 · About · Works · Skills · Contact
- `works/p01.html` ~ `p04.html` — 프로젝트 상세 (개요 · 데이터와 실험 · 핵심 발견)
- `works/more.html` — P05–P08 요약
- `assets/` — 스타일, 스크립트(그림은 실제 수치로 SVG를 그림), 이미지

빌드 도구 없이 정적 파일 그대로 GitHub Pages에서 열립니다.

## 프로젝트 페이지 고치기

`works/*.html`은 `tools/pages.py`(내용)에서 만들어집니다. 내용을 고친 뒤 저장소 루트에서

```
python3 tools/build.py .
```
