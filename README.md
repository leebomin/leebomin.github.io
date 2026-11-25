# leebomin.github.io

이보민 포트폴리오 웹사이트 · https://leebomin.github.io

- `index.html` — About · News · Selected Projects
- `projects.html` — 전체 프로젝트 목록
- `cv.html` — Experience · Skills · Contact
- `works/p01.html` ~ `p04.html` — 프로젝트 상세, `works/more.html` — P05–P08
- `en/` — 같은 구조의 영어판 (사이드바의 한국어 / English로 전환)
- `assets/` — 스타일, 스크립트(사진 픽셀 효과, 실제 수치로 그린 그림), 이미지

## 내용 고치기

모든 HTML은 `tools/content.py`(한국어)와 `tools/content_en.py`(영어)에서 만들어집니다. 사실을 고칠 땐 두 파일을 같이 고쳐 주세요. 고친 뒤 저장소 루트에서

```
python3 tools/build.py
```
