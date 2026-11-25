# Site text. Facts follow the Figma v4 deck (2026-11-25).

def stag(text, href, icon='{AR}', ext=True):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="stag" href="{href}"{t}>{icon}{text}</a>'

def thumb(cells, label, value):
    n, k, cols, cls = cells
    rows = -(-n // cols)
    w = min(100, round(84 * cols / rows / 1.68))  # % of thumb inner width, grid height ≈ 84px
    return f'<div class="thumb"><div class="tg" style="width:{w}%" data-cells="{n},{k},{cols},{cls}"></div><div class="tl"><span>{label}</span><b>{value}</b></div></div>'

DEMO_P03 = 'https://leebomin.github.io/pill-finder/demo'

def pitem(code, meta, title, ko, line, href, th, gh=None, demo=None):
    tags = (stag('Demo', demo) if demo else '') + (stag('GitHub', f'https://github.com/{gh}', '{GH}') if gh else '')
    return f'''<article class="pitem rv">
  <a class="cover" href="{href}" aria-label="{title} {ko}"></a>
  {th}
  <div class="pinfo">
    <div class="badge"><span class="k">{code}</span>{meta}</div>
    <h3>{title}<span class="ko">{ko}</span></h3>
    <p>{line}</p>
    {'<div class="small-tags">' + tags + '</div>' if tags else ''}
  </div>
</article>'''

_P = ([
  pitem('P01', "TOBIG'S · 멀티모달/CV 팀 · 2026", 'Deepfake Detection', '멀티모달 딥페이크 탐지 모듈',
        '이미지 · 얼굴 영상 · 음성 후보 12종을 <b>처음 보는 데이터</b>로 비교해 골랐습니다. 파일 형식에 남은 가짜 단서를 먼저 지웠습니다.',
        'works/p01.html', thumb((100, 91, 10, 'f'), '외부 AUC · 칸=0.01', '0.907')),
  pitem('P02', '미래내일 일경험 · 제주항공 · 2026 · 동상', 'Predictive Maintenance', '항공 엔진 정비 시점 결정',
        '잔여수명을 확률분포로 예측해 정비 시점을 정했습니다. 15~20% 개선이 <b>데이터 누수</b>였음을 찾았습니다.',
        'works/p02.html', thumb((100, 12, 10, 'f'), '정비 전 고장 · 칸=1%', '0.119'), gh='leebomin/jejuairline'),
  pitem('P03', '네이버클라우드 에이전틱 AI 과정 · 2026', 'Pill Finder', '공식 문서 근거 LLM 웹앱',
        '모델에게 맡기지 않을 것부터 정하고, 규칙을 보지 않은 질문 40개로 평가했습니다. 응급 질문 감지 <b>3/20 → 20/20</b>.',
        'works/p03.html', thumb((20, 20, 10, 'f'), '응급 질문 감지', '20/20'), gh='leebomin/pill-finder', demo=DEMO_P03),
  pitem('P04', "TOBIG'S · DA 트랙 과제 · 2026", 'A/B Testing', '숙박 앱 전환율 실험',
        '결과를 보기 전에 판정 규칙을 고정했습니다. 12일차에 멈췄다면 뒤집혔을 결론을 21일 고정 판정으로 확인했습니다.',
        'works/p04.html', thumb((12, 3, 12, 'f'), '관찰 격차 10.7 중 · %p', '+2.75'), gh='leebomin/tobigs-26th'),
  pitem('P05', "TOBIG'S · SQL 과제 · 2026", 'Join Fan-out', 'Olist 이커머스 SQL 분석',
        '에러 없이 돈 쿼리에서 JOIN 중복으로 결제금액이 28.23% 부풀어 있었습니다.',
        'works/more.html#p05', thumb((100, 28, 10, 'f'), '과대 집계 · 칸=1%', '+28.23%'), gh='leebomin/tobigs-26th'),
  pitem('P06', '도시조사방법론 · 팀 · 2023', 'Effect Size', '비수도권 대학 쇠퇴현황 분석',
        '격차는 뚜렷했지만(p&lt;0.001) 청년 순이동에 대한 설명력은 11%였습니다.',
        'works/more.html#p06', thumb((100, 11, 10, 'f'), '설명력 R² · 칸=1%', '0.11')),
  pitem('P07', '다변량통계학 · 개인 · 2024', 'Definition Bias', '지방소멸위험지수 다변량 분석',
        '가장 큰 요인이 계산식의 공통 분모 때문일 수 있음을 짚었습니다.',
        'works/more.html#p07', thumb((100, 85, 10, 'f'), 'PC1–4 누적 · 칸=1%', '85.3%')),
  pitem('P08', '회귀분석1 · 개인 · 2024', 'Influence', '빈집 비율 회귀 진단',
        '영향점 12곳을 빼면 바뀌는 값을 흔들림의 크기로 보고했습니다.',
        'works/more.html#p08', thumb((261, 12, 29, 'f'), '영향점 · 시군구 261', '12')),
])
PROJECTS = ''.join(_P)
MAIN4 = ''.join(_P[:4])

UPDATES = [
  ('2026.11', '알약 찾기 도우미(P03) 데모 완성'),
  ('2026.10', "TOBIG'S A/B 테스트 과제(P04)"),
  ('2026.08', "TOBIG'S 26기 · 멀티모달/CV 팀 합류"),
  ('2026.07', '에어로AI트랙 경진대회 <b>동상</b> · 항공 정비 PoC(P02)'),
  ('2026.06', 'ADsP 취득 · AI 에이전트 부트캠프 시작'),
  ('2026.04', 'TEPS 363'),
  ('2025.12', 'SQLD 취득'),
  ('2025.09', '국토교통부 토지정책과 청년인턴'),
  ('2025.01', '핀란드 Tampere University 교환학생'),
]
def updates():
    first, rest = UPDATES[0], UPDATES[1:]
    lis = ''.join(f'<li><div class="upd"><time>{d}</time><span>{t}</span></div></li>' for d, t in rest)
    return f'''<details class="updates rv"><summary><div class="upd"><time>{first[0]}</time><span>{first[1]}</span></div><svg class="chev" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 6l4 4 4-4"/></svg></summary><ul>{lis}</ul></details>'''

INDEX = dict(title='이보민 · Data Scientist', desc='데이터 사이언티스트 이보민의 포트폴리오. 실험 설계 · 모델 평가와 검증 · 통계 모델링 · LLM 서비스.', body=f'''
<section id="about" class="rv">
  <div class="photo m" data-src="{{A}}assets/img/portrait.png" aria-label="이보민 사진. 커서를 올리면 그 주변이, 누르면 사진 전체가 픽셀로 바뀝니다."></div>
  <h1 class="headline"><span class="ko">안녕하세요, 이보민입니다.</span></h1>
  <div class="prose">
    <p>서울시립대학교에서 도시행정학과 통계학을 공부하고 있습니다.</p>
    <p>모델을 만들고, 그 결과가 정말 맞는지 다시 확인하는 일을 주로 합니다.<br>최근에는 딥페이크 탐지, 항공 엔진 정비 예측, 공식 문서 기반 LLM 웹앱을 만들었습니다.</p>
  </div>
  <div class="tags"><span class="tag">실험 설계</span><span class="tag">모델 평가 · 검증</span><span class="tag">통계 모델링</span><span class="tag">LLM 서비스</span></div>
</section>


<section class="sec" id="projects">
  <h2 class="sec-t">Selected Projects</h2>
  <div class="plist">{MAIN4}</div>
  <p class="more rv"><a href="projects.html">전체 프로젝트 {'{AR}'}</a><a href="cv.html">CV {'{AR}'}</a></p>
</section>

''')


PROJECTS_PAGE = dict(title='Projects · 이보민', desc='이보민의 프로젝트 — 모델 평가, 실험 설계, 통계 분석, LLM 서비스.', body=f'''
<h1 class="pg-t rv">Projects</h1>
<div class="plist">{PROJECTS}</div>
''')

CV_PAGE = dict(title='CV · 이보민', desc='이보민의 경력 · 학력 · 기술 · 자격.', body=f'''
<h1 class="pg-t rv">CV</h1>
<section class="sec" id="experience" style="padding-top:0">
  <h2 class="sec-t">Experience</h2>
  <ul class="rows rv">
    <li><time>2026.08–</time><span>TOBIG'S 26기 · DA 트랙 · 멀티모달/CV 팀</span><span class="r">P01 · P04 · P05</span></li>
    <li><time>2026.06–11</time><span>AI 에이전트 부트캠프 · 네이버클라우드 과정 포함</span><span class="r">P03</span></li>
    <li><time>2026.06–07</time><span>미래내일 일경험 · 항공우주산학융합원 × 제주항공</span><span class="r">P02 · 동상</span></li>
    <li><time>2025.09–12</time><span>국토교통부 토지정책과 청년인턴</span><span class="r"></span></li>
    <li><time>2025.01–05</time><span>Tampere University 교환학생 · 핀란드</span><span class="r"></span></li>
    <li><time>2024.03–25.02</time><span>통계청 대학생 기자단 16기</span><span class="r">통계 콘텐츠 기사</span></li>
    <li><time>2022.03–</time><span>서울시립대 도시행정 · 통계학</span><span class="r">GPA 4.19 / 4.5</span></li>
  </ul>
</section>

<section class="sec" id="skills">
  <h2 class="sec-t">Skills &amp; Credentials</h2>
  <div class="skills rv">
    <div><b>Python</b><span>pandas · sklearn · PyTorch</span></div>
    <div><b>SQL</b><span>MySQL · SQLite</span></div>
    <div><b>R · SAS</b><span>R · SAS · Jamovi</span></div>
    <div><b>통계 검정 · 회귀</b><span>t-test · 회귀 · VIF</span></div>
    <div><b>실험 설계</b><span>SRM · MDE · CI</span></div>
    <div><b>ML · DL</b><span>CLIP · 1D-CNN</span></div>
    <div><b>LLM · RAG</b><span>RAG · MCP · ChromaDB · Ollama</span></div>
    <div><b>자격 · 어학</b><span>ADsP · SQLD · TEPS 363 · OPIc IH</span></div>
  </div>
</section>

<section class="sec" id="contact">
  <h2 class="sec-t">Contact</h2>
  <p class="prose rv" style="margin-top:0"><a class="u" href="mailto:ibomin88@gmail.com">ibomin88@gmail.com</a></p>
</section>
''')

# ───────── project page helpers ─────────
def top(code, kind, title, ko, links, meta, award=None):
    ls = ''.join(links)
    ms = ''.join(f'<div><dt class="label">{k}</dt><dd>{v}</dd></div>' for k, v in meta)
    aw = f'<span class="award">{award}</span>' if award else ''
    return f'''<div class="crumb label rv"><a href="../projects.html">Projects</a><span>/</span><span>{code} · {kind}</span></div>
<h1 class="ptitle rv">{title}</h1><p class="psub rv">{ko}</p>
{'<div class="small-tags rv">' + ls + '</div>' if ls else ''}{aw}
<dl class="meta rv">{ms}</dl>'''

def fig(parts, cap=''):
    ps = ''.join(f'<div class="fig-part">{"<div class=fig-head><span class=h>" + h + "</span><span class=r>" + r + "</span></div>" if h else ""}{b}</div>' for h, r, b in parts)
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="fig rv"><div class="fig-box">{ps}</div>{c}</figure>'

def h2(en, ko):
    return f'<h2 class="rv">{en}<span class="ko">{ko}</span></h2>'

def take(t):
    return f'<div class="take rv"><span class="label">Takeaway</span><p>{t}</p></div>'

def rowfig(k, cells, v, sub=''):
    s = f'<div class="sub">{sub}</div>' if sub else ''
    return f'<div class="rowfig"><span class="k">{k}</span><div data-cells="{cells}"></div><span class="v">{v}</span>{s}</div>'

def table(head_, rows, num=()):
    th = ''.join(f'<th>{h}</th>' for h in head_)
    tr = ''.join('<tr>' + ''.join(f'<td class="{"n" if j in num else ""}">{c}</td>' for j, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<div class="dtable-wrap rv"><table class="dtable"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def dl(rows):
    return '<dl class="dl rv">' + ''.join(f'<div><dt class="label">{k}</dt><dd>{v}</dd></div>' for k, v in rows) + '</dl>'

PAGES = {}

PAGES['p01.html'] = dict(title='Deepfake Detection', desc='멀티모달 딥페이크 탐지 모듈 · 처음 보는 데이터에서의 성능으로 모델 선정',
 prev=('more.html#p08', 'P08 Influence'), next=('p02.html', 'P02 Predictive Maintenance'),
 body=top('P01', 'Main', 'Deepfake Detection', '멀티모달 딥페이크 탐지 모듈', [],
  [('Period', '2026.08–11'), ('Team', "TOBIG'S 멀티모달/CV 팀 · 4명"), ('Role', '딥페이크 탐지 모델 전담 · 비교 · 선정 · 추론 API'), ('Model', '이미지 CLIP-L/14 · 얼굴 CLIP + Xception · 음성 wav2vec2 XLS-R')]) + f'''
<div class="body">
<p class="rv">투자 사기 탐지 서비스(브라우저 확장)에서 이미지 · 얼굴 영상 · 음성이 <b>합성인지</b> 판별하는 모듈을 맡았습니다. 학습 데이터에서 잘 맞히는 모델보다 <b>처음 보는 데이터</b>에서 성능이 유지되는 모델이 필요했기 때문에, 학습에 쓰지 않은 외부 데이터셋의 AUC를 1순위 기준으로 삼았습니다.</p>
{fig([('외부 데이터 AUC', '학습에 쓰지 않은 데이터셋', '<div id="f-auc"></div>')], '세 모달리티 모두 외부 데이터에서 측정했습니다. 점선 0.5는 우연 수준입니다.')}

{h2('What I did', '한 일')}
<ol class="steps rv">
<li>이미지 · 얼굴 · 음성 후보 <b>12종</b>을 외부 데이터로 비교하고, <b>부트스트랩 신뢰구간 · 짝 비교</b>로 차이가 우연이 아님을 확인했습니다.</li>
<li>영상통화 화질을 재현해 보니 저화질(<b>360p 이하</b>)에서는 우세 모델이 뒤집혔습니다. 얼굴 크기(<b>170px</b>)를 기준으로 모델을 자동으로 고르게 했습니다.</li>
<li>결과를 보기 전에 합격선을 고정한 서비스 벤치마크 <b>8개 중 7개</b>를 통과했고, 백엔드 · 웹 확장이 호출하는 API로 연결했습니다(판정 일치율 100%).</li>
</ol>
{fig([('얼굴 크기로 모델 선택', '영상통화 화질 재현 실험', '<div id="f-res"></div>'), ('서비스 경로 벤치마크', '기준 8개 · 결과 전에 고정', '<div class="rowfig" style="grid-template-columns:1fr 56px"><div data-cells="8,7,8,f" style="max-width:320px"></div><span class="v">7 / 8</span></div><p class="fig-note">미달 1개는 탭 녹화 얼굴 탐지율 0.351 (기준 0.60). 음성은 탭 녹화에서도 AUC 0.999.</p>')])}

{h2('Key finding', 'Shortcut · 가짜 단서')}
<h3 class="rv">상황</h3>
<p class="rv">첫 파이프라인은 돌릴 때마다 결과가 크게 달라졌습니다. 이미지 내용을 보지 않는 <b>FFT 기준선</b>의 AUC가 실행마다 <b>0.015 · 0.500 · 0.601</b>로 흔들렸습니다.</p>
<h3 class="rv">의심</h3>
<p class="rv">진짜 이미지가 일부 샤드에서만 뽑혀 <span class="hl">파일 형식</span>이 정답과 겹쳐 있었습니다. 합성 흔적이 아니라 JPEG/PNG를 보고 맞힐 수 있는 상태였습니다.</p>
<h3 class="rv">확인</h3>
<p class="rv">모든 이미지를 <b>384 JPEG</b>로 다시 저장하자 기준선은 <b>0.49</b>로 우연 수준이 됐습니다. 그럼에도 비율 · 크기 두 숫자만으로 <b>0.694</b>가 나와 <b>정사각 크롭</b>으로 다시 학습했습니다.</p>
{fig([('', '', '<div id="f-fft"></div>')], '내용을 보지 않는 모델(FFT 기준선)의 AUC. 점이 0.5(회색 띠)에서 멀수록 데이터에 가짜 단서가 남아 있다는 뜻입니다.')}
{take('가짜 단서 제거 모델 · 서비스 API 연결')}

{h2('Data &amp; Experiment', '데이터 · 모델 선정')}
{dl([('Data', '학습 이미지 SID_Set · OpenFake / 얼굴 ThinothW / 음성 In-the-Wild<br>외부 평가 Community Forensics · KoDF · Celeb-DF · ASVspoof2019'),
     ('Preproc', '형식 단서 → 384 JPEG로 다시 저장 (기준선 0.49)<br>비율 · 크기 단서 (AUC 0.694) → 정사각 크롭 재학습'),
     ('Criteria', '외부 2종 중 낮은 쪽 AUC 기준 1위 (0.856) · 부트스트랩 1위 확률 100% · 앙상블보다 유의하게 높음')])}
{table(['Modality', 'Eval set', 'Model', 'Ext. AUC', 'Note'], [
  ['이미지', 'Community Forensics', 'CLIP-L/14 다층', '0.907', '정사각 크롭 · 외부 2종 1위'],
  ['얼굴 영상', 'KoDF', 'CLIP-L/14', '0.858', 'Xception 대비 +0.051'],
  ['음성', 'ASVspoof2019', 'wav2vec2 XLS-R', '0.988', '전화망 G.711 0.976'],
  ['임계값', 'KoDF', '검증셋 기준 고정', '46%', '탐지율 · 재보정 필요']], (3,))}
{fig([('처음 보는 생성기(OOD) AUC', '정사각 크롭 전 비교', '<div id="f-ood"></div>')], '최종 선정은 외부 2종 기준입니다. UnivFD 공개 가중치는 2018 GAN으로 학습돼 우연 수준입니다.')}
<p class="rv">내부 검증 점수는 데이터 단서까지 학습한 결과일 수 있어, 처음 보는 데이터의 AUC를 기준으로 했습니다. 차이가 작은 후보는 신뢰구간과 짝 비교로 우연이 아님을 확인한 뒤 골랐습니다. AUC가 유지돼도 고정 임계값에서는 얼굴 탐지율이 46%로 떨어져, 재보정에 필요한 표본 수까지 정리해 전달했습니다.</p>
{take('처음 보는 데이터의 점수로 선정')}
</div>''',
 script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-auc'), F.hbars({min:.4,max:1,ticks:[.4,.5,.6,.7,.8,.9,1],ref:.5,refLabel:'0.5 = 우연',noteW:160,
 rows:[{k:'IMAGE',v:.907,note:'Community Forensics'},{k:'FACE',v:.858,note:'KoDF · 한국인 얼굴'},{k:'VOICE',v:.988,note:'ASVspoof2019'}]}));
mount(document.getElementById('f-res'), w=>{
 const X=F.lin(0,5,10,w-10), r=['1080p','720p','480p',null,'360p','240p'], pos=[0,1,2,2.55,3.4,4.6];
 let s=`<line x1="${X(0)}" x2="${X(5)}" y1="40" y2="40" stroke="#C8C8C8"/>`;
 r.forEach((t,i)=>{ if(!t) return; s+=`<line x1="${X(pos[i])}" x2="${X(pos[i])}" y1="36" y2="44" stroke="#3A3A3A"/>`+F.T(X(pos[i]),28,t,{a:i?'middle':'start',fs:10.5,c:'#686868'}); });
 s+=`<line x1="${X(2.55)}" x2="${X(2.55)}" y1="8" y2="86" stroke="#141414" stroke-width="1.2"/>`+F.T(X(2.55),6,'얼굴 170px',{a:'middle',fs:11,ko:true,b:true});
 s+=`<rect x="${X(0)}" y="58" width="${X(2.55)-X(0)-4}" height="5" fill="#141414"/>`+F.T(X(0),80,'CLIP · 480p 이상',{fs:11,ko:true});
 s+=`<rect x="${X(2.55)+4}" y="58" width="${X(5)-X(2.55)-4}" height="5" fill="#8C8C8C"/>`+F.T(X(2.55)+8,80,w<520?'XCEPTION':'XCEPTION · 360p 이하 · 얼굴 170px 미만',{fs:11,ko:true});
 return F.svg(w,92,s);});
mount(document.getElementById('f-ood'), F.dotrows({min:.3,max:1,ticks:[.3,.5,.7,.9],ref:.5,refLabel:'0.5',rowH:26,inline:true,labelW:118,
 rows:[['CLIP 마지막 층',.878],['CLIP 다층 · 선정',.834,1],['ConvNeXt-S',.831],['DINOv2-L',.821],['Xception',.796],['EfficientNet-B4',.754],['FFT 기준선',.486],['UnivFD 공개',.398]]
 .map(([k,v,sel])=>({k,sel,sub:'',pts:[{v,t:v.toFixed(3),a:'start',dx:9,r:sel?5:3.5,c:sel?'#141414':'#8C8C8C'}]}))}));
mount(document.getElementById('f-fft'), F.dotrows({min:0,max:1,ticks:[0,.2,.4,.6,.8,1],band:[.45,.55],ref:.5,refLabel:'0.5 = 우연',notes:true,rowH:88,
 rows:[{k:'01  BEFORE',sub:'같은 코드 · 실행 3번',range:true,note:'실행마다\\n제각각',pts:[{v:.015,t:'0.015'},{v:.5,t:'0.500',below:true},{v:.601,t:'0.601'}]},
       {k:'02  FIX 1',sub:'384 JPEG로 형식 통일',note:'우연 수준',pts:[{v:.49,t:'OOD 0.490',a:'start',dx:9},{v:.46,t:'외부 0.460',a:'end',dx:-9,below:true}]},
       {k:'03  남은 단서',sub:'비율 · 크기 두 숫자만',note:'→ 정사각\\n크롭 재학습',pts:[{v:.694,t:'0.694'}]}]}));
''')

PAGES['p02.html'] = dict(title='Predictive Maintenance', desc='엔진 잔여수명 확률 예측 · 정비 시점 결정',
 prev=('p01.html', 'P01 Deepfake Detection'), next=('p03.html', 'P03 Pill Finder'),
 body=top('P02', 'Main', 'Predictive Maintenance', '엔진 잔여수명 확률 예측 · 정비 시점 결정',
  [stag('GitHub', 'https://github.com/leebomin/jejuairline', '{GH}')],
  [('Period', '2026.06–07'), ('Team', '미래내일 일경험 · 항공우주산학융합원 × 제주항공 · 4명'), ('Role', '팀장 · 1D-CNN 앙상블 · conformal 공동 구현 · 보고서'), ('Model', '1D-CNN 앙상블 + conformal · 우도비 베이즈 결합')],
  award='에어로AI트랙 경진대회 동상 · 2026.07') + f'''
<div class="body">
<p class="rv">정비가 늦으면 결함이 생기고, 너무 잦으면 비용이 듭니다. 엔진 잔여수명을 숫자 하나가 아니라 <b>확률분포</b>로 예측하고, 이 비대칭을 반영해 <b>정비 시점</b>을 정하는 PoC를 만들었습니다. 데이터는 NASA 시뮬레이션인 N-CMAPSS 엔진 34대와 NGAFID 실비행 28,935편입니다.</p>
{fig([('정비 전 고장 확률', '칸 하나 = 1%', '<div class="waffles"><div><div data-cells="100,0,10,"></div><p class="w-l">기존 정책</p><p class="w-v dim">0.196</p></div><div><div data-cells="100,0,10,"></div><p class="w-l">확률 보정 후</p><p class="w-v">0.119</p></div><p class="w-txt fig-note">100번 정비 결정 중 정비하기 전에 고장 나는 경우가 약 20번에서 12번으로 줄었습니다.</p></div>')])}

{h2('What I did', '한 일')}
<ol class="steps rv">
<li>평가 방식을 다시 점검해, 15~20% 개선이 <b>데이터 누수</b>였음을 찾았습니다.</li>
<li>1D-CNN 앙상블의 예측 분포를 conformal로 보정해, 90% 구간이 실제로 <b>0.902</b>를 덮는 것을 확인했습니다.</li>
<li>보정된 확률로 정비 시점을 정해 정비 전 고장 확률을 <span class="hl">0.196 → 0.119</span>로 낮췄습니다.</li>
</ol>
{fig([('90% 예측 구간 커버리지', '', '<div id="f-cov"></div><p class="fig-note">“90% 구간”이라고 예측한 범위 안에 실제 잔여수명의 90.2%가 들어왔습니다.</p>'),
      ('정책 시뮬레이션 · 엔진 34대 · 참고치', '칸 하나 = 엔진 1대', rowfig('평균 기반', '34,34,34,f', '1 / 34').replace('data-cells="34,34,34,f"', 'id="e-a"') + rowfig('확률 기반', '34,34,34,f', '0 / 34') + '<p class="fig-note">× = 정비 전에 고장 난 엔진. 1대 차이라 단독 근거로 쓰지 않았습니다.</p>')])}

{h2('Key finding', 'Leakage · 데이터 누수')}
<h3 class="rv">상황</h3>
<p class="rv">‘LCC 단거리 가중치’를 넣자 RMSE가 <b>15~20% 개선</b>됐습니다. 같은 데이터로 실험한 팀원들의 결과와 비교하면 지나치게 큰 폭이었습니다.</p>
<h3 class="rv">의심</h3>
<p class="rv">개선폭이 실행마다 들쭉날쭉했습니다. 확인해 보니 스케일러와 변수 선택이 <span class="hl">교차검증 폴드 밖에서 fit</span>되어, 평가셋 정보가 학습에 섞이고 있었습니다.</p>
<h3 class="rv">확인</h3>
<p class="rv">전처리를 폴드 안으로 옮기자 효과는 <b>≈ 0</b>으로 사라졌습니다. 가설을 기각하고, 같은 원인으로 생긴 <b>버그 5건</b>도 함께 고쳤습니다.</p>
{fig([('Before · 전처리 먼저, 나누기는 나중', '', '<div class="flow"><div class="box"><span class="label">Data</span><p>전체 데이터<br><small>평가 데이터 포함</small></p></div><span class="arr">→</span><div class="box"><span class="label">Fit</span><p>스케일러 · 변수 선택<br><small>전체 데이터 기준</small></p></div><span class="arr">→</span><div class="box"><span class="label">Split</span><p>학습 / 평가</p></div></div>'),
      ('After · 나누기 먼저, 전처리는 학습 데이터로만', '', '<div class="flow"><div class="box"><span class="label">Split</span><p>학습 / 평가</p></div><span class="arr">→</span><div class="box"><span class="label">Fit</span><p>스케일러 · 변수 선택<br><small>학습 데이터 기준</small></p></div><span class="arr">→</span><div class="box"><span class="label">Apply</span><p>평가에는 적용만</p></div></div>'),
      ('RMSE 개선폭', '', '<div id="f-rmse"></div>')], '개선처럼 보였던 15~20%는 평가 데이터를 미리 본 효과였습니다.')}
{take('좋은 수치일수록 출처부터')}

{h2('Data &amp; Experiment', '예측 구간 보정 · 정비 결정')}
{dl([('Data', 'N-CMAPSS 엔진 34대 (NASA 시뮬레이션) · NGAFID 실비행 28,935편 (진단)'), ('Preproc', '스케일러 · 변수선택을 교차검증 폴드 안에서만 fit'), ('Unit', '엔진 단위 교차검증 · 같은 엔진이 학습 · 평가에 섞이지 않게'), ('Decision', '늦은 정비(결함)와 잦은 정비(비용)의 비대칭을 반영한 정비 시점')])}
{table(['Metric', 'Baseline', 'Final', 'How'], [
  ['정비 전 고장 확률', '0.196', '0.119', '보정된 분포로 정비 시점 결정'],
  ['90% 구간 커버리지', '—', '0.902', '1D-CNN 앙상블 + conformal'],
  ['정책 시뮬 고장', '최선 1대', '0 / 34', '평균 기반 → 확률 기반 정책'],
  ['실비행 진단 AUC', '0.76', '0.849', '우도비 베이즈 결합']], (1, 2))}
<p class="rv">RMSE가 데이터 규모의 한계에 닿은 뒤에는 모델을 더 키워도 정비 결정이 나아지지 않았습니다. 그래서 예측 구간이 실제로 90%를 덮는지를 먼저 맞추고, 그 확률로 정비 시점을 정했습니다.</p>
{take('모델 크기보다 예측 구간의 신뢰도')}
</div>''',
 script='''
const {mount}=PF, F=FIG;
const w=document.querySelectorAll('.waffles [data-cells]');
w[0].innerHTML=PF.cells(100,i=>i>=80?'g':'',10); w[1].innerHTML=PF.cells(100,i=>i>=88?'f':'',10);
document.getElementById('e-a').innerHTML=PF.cells(34,i=>i===23?'x':'f',34);
mount(document.getElementById('f-cov'), F.target({v:.902,t:.9,tl:'목표 90%',vt:'0.902'}));
mount(document.getElementById('f-rmse'), w=>{
 const X=F.lin(0,22,70,w-90); let s='';
 [0,5,10,15,20].forEach(t=>{s+=`<line x1="${X(t)}" x2="${X(t)}" y1="4" y2="76" stroke="#C8C8C8" stroke-width=".6"/>`+F.T(X(t),92,t+'%',{a:'middle',fs:10.5,c:'#686868'});});
 s+=F.T(0,24,'BEFORE',{fs:11,b:true})+`<rect x="${X(0)}" y="12" width="${X(15)-X(0)}" height="16" fill="#141414"/>`;
 for(let x=X(15);x<X(20);x+=4) s+=`<rect x="${x}" y="12" width="2" height="16" fill="#141414"/>`;
 s+=F.T(X(20)+8,25,'+15~20%',{disp:true,fs:15});
 s+=F.T(0,62,'AFTER',{fs:11,b:true})+`<rect x="${X(0)}" y="50" width="3" height="16" fill="#141414"/>`+F.T(X(0)+12,63,'≈ 0',{disp:true,fs:15});
 return F.svg(w,98,s);});
''')

PAGES['p03.html'] = dict(title='Pill Finder', desc='알약 찾기 도우미 · 공식 문서 근거 LLM 웹앱',
 prev=('p02.html', 'P02 Predictive Maintenance'), next=('p04.html', 'P04 A/B Testing'),
 body=top('P03', 'Main', 'Pill Finder', '알약 찾기 도우미 · 공식 문서 근거 LLM 웹앱',
  [stag('Demo', DEMO_P03), stag('GitHub', 'https://github.com/leebomin/pill-finder', '{GH}')],
  [('Period', '2026.11'), ('Team', '개인 · 네이버클라우드 에이전틱 AI 과정'), ('Role', '기획 · 모델 역할 설계 · 앱 · MCP 도구 · 평가 설계'), ('Model', 'HyperCLOVA X(답변) · Qwen3 4B(판단) · Claude API(검토)')]) + f'''
<div class="body">
<p class="rv">1인 가구가 남은 약을 확인할 때 쓰는 도구입니다. 공식 자료만 근거로 알약 후보를 찾고, 일반의약품에 한해 <b>쉬운 말 요약</b>과 질문 답변을 줍니다. 진단 · 복용 지시는 하지 않으며, 의료인 검수 전 데모입니다.</p>
{fig([('Pipeline', '모델에게 맡기지 않을 것부터', '<div class="flow"><div class="box"><span class="label">Question</span><p>입력</p></div><span class="arr">→</span><div class="box"><span class="label">Emergency</span><p>코드 + Qwen3 4B</p></div><span class="arr">→</span><div class="box"><span class="label">Retrieve</span><p>식약처 원문</p></div><span class="arr">→</span><div class="box on"><span class="label">Answer</span><p>HyperCLOVA X</p></div><span class="arr">→</span><div class="box"><span class="label">Review</span><p>Claude API</p></div></div><div class="flow-sub"><span>규칙 · 검색은 코드</span><span>답변 · 검토만 LLM</span></div>')])}

{h2('What I did', '한 일')}
<ol class="steps rv">
<li>계산 · 규칙은 코드, 답변은 HyperCLOVA X, 검토는 Claude API로 나눠 <span class="hl">모델에게 맡기지 않을 것</span>부터 정했습니다.</li>
<li>표현 목록에 걸리지 않은 응급 질문을 Qwen3 4B가 한 번 더 판단하게 해 감지율을 <b>3/20 → 20/20</b>으로 올렸습니다.</li>
<li>모든 답변에 근거 문단 또는 “공식 자료에 없음”을 표시하고(<b>20/20</b>), 개인정보는 확인 전 외부 전송을 막았습니다(<b>9/10</b> 가림).</li>
</ol>
{fig([('안전 장치', '칸 하나 = 1건', rowfig('Citation', '20,20,20,f', '20 / 20', '근거 문단 또는 “공식 자료에 없음” 표시') + rowfig('PII mask', '10,9,10,f', '9 / 10', '확인 전 외부 전송 0 / 10') + rowfig('Done', '19,17,19,f', '17 / 19', '남은 2개는 사진 인식 측정 필요'))])}

{h2('Key finding', 'Eval set · 평가셋 먼저 고정')}
<h3 class="rv">상황</h3>
<p class="rv">‘삼켰’, ‘한꺼번에’ 같은 <b>표현 목록</b>만으로는 응급 질문을 <b>3/20</b>밖에 잡지 못했습니다.</p>
<h3 class="rv">의심</h3>
<p class="rv">규칙을 고칠 때마다 직접 만든 질문으로 확인하면, 규칙에 맞춘 질문만 통과하는 <b>착시</b>가 생길 수 있었습니다.</p>
<h3 class="rv">확인</h3>
<p class="rv">규칙을 보지 않은 에이전트가 쓴 <span class="hl">새 질문 40개</span>를 먼저 고정하고 그것으로만 평가했습니다. Qwen3 4B 판단을 더하자 <b>20/20</b>, 평가셋 안 추가 오탐 <b>0</b>, 응답 약 <b>0.4초</b>였습니다.</p>
{fig([('Eval set', '시험지 먼저 고정', '<div class="flow"><div class="box"><span class="label">Step 1</span><p>질문 40개 먼저 고정<br><small>규칙을 보지 않은 에이전트가 작성</small></p></div><span class="arr">→</span><div class="box"><span class="label">Step 2</span><p>규칙 · 모델 수정</p></div><span class="arr">→</span><div class="box"><span class="label">Step 3</span><p>같은 40개로 재측정</p></div></div><div class="flow-sub"><span></span><span>↺ 2 → 3 반복 · 시험지는 바꾸지 않음</span></div>'),
      ('Result', '같은 40개로만 측정 · 칸 하나 = 질문 1개', rowfig('Keyword list', '20,3,20,f', '3 / 20') + rowfig('+ Qwen3 4B', '20,20,20,f', '20 / 20', '평가셋 기준 추가 오탐 0 · 응답 약 0.4초') + rowfig('Limit', '20,2,20,g', '2 / 20', '가정형 질문에도 119 안내가 뜨는 오탐 · 미해결'))])}
{take('응급 질문 감지 3/20 → 20/20')}
</div>''', script=' ')

PAGES['p04.html'] = dict(title='A/B Testing', desc='숙박 앱 전환율 A/B 테스트 · 사전 판정 규칙',
 prev=('p03.html', 'P03 Pill Finder'), next=('more.html', 'P05–08'),
 body=top('P04', 'Main', 'A/B Testing', '숙박 앱 전환율 A/B 테스트 · 사전 판정 규칙',
  [stag('GitHub', 'https://github.com/leebomin/tobigs-26th', '{GH}')],
  [('Period', '2026.10'), ('Team', "TOBIG'S DA 트랙 · 개인 과제"), ('Role', '실험 설계 · 판정 규칙 · 분석 전 과정'), ('Method', '사용자 단위 배정 · delta method · SRM 검정 · MDE')]) + f'''
<div class="body">
<p class="rv">분석팀이 진단한 promotion 채널의 목록 → 상세 전환율 <b>약 10.7%p 격차</b>를 개선안(목록 카드 할인가 표시)으로 바꾸고, <b>결과를 보기 전에 정한 규칙</b>대로 실험을 설계 · 판정했습니다.</p>
{fig([('Gap', '관찰 격차 중 실험으로 확인된 몫 · %p', '<div id="f-gap"></div>'), ('Effect', '목록 → 상세 전환율 · 95% CI · %p', '<div id="f-ci"></div>')], '구간 전체가 0보다 커서 효과가 있다고 판정했습니다(p = 0.0026). 매출 증가는 이 실험으로 확인하지 않았습니다.')}

{h2('What I did', '한 일')}
<ol class="steps rv">
<li><b>사용자 단위</b>로 배정하고 delta method로 분산을 보정했습니다. 디자인 효과 <b>1.59 → 2.11</b>을 반영해 MDE 3%p · 기간 <b>21일</b>을 정했습니다.</li>
<li>배정 비율(SRM p = 0.71, 3,446명 vs 3,415명)과 <b>8일차 광고 캠페인</b> 전후를 나눠 확인하고, 광고 이후 구간은 탐색적으로만 해석했습니다.</li>
<li>목록 → 상세 전환율 <span class="hl">+2.75%p</span> (95% CI 0.96~4.54), 가드레일 유의한 악화 없음 → <b>단계적 배포</b>를 권고했습니다.</li>
</ol>

{h2('Key finding', 'Peeking · 중간 확인')}
<h3 class="rv">상황</h3>
<p class="rv">같은 데이터로 <b>고정 기간 21일 판정</b>과 <b>매일 확인 후 중단</b>하는 방식을 비교했습니다.</p>
<h3 class="rv">의심</h3>
<p class="rv">매일 p값을 보다 멈추면 우연히 낮아진 날 결론이 나거나, 효과가 있어도 <b>출시를 접는</b> 판단이 나올 수 있었습니다.</p>
<h3 class="rv">확인</h3>
<p class="rv">12일차에 멈추면 사용자 단위 p = <b>0.084</b>로 출시하지 않는 결론이었고, <span class="hl">21일 고정 판정</span>에서는 p = <b>0.0026</b>, +2.75%p였습니다.</p>
{fig([('Timeline', '21일 · 칸 하나 = 하루', '<div id="f-days"></div>'),
      ('Decision', '같은 데이터 · 다른 규칙', '<div class="cards2"><div class="c"><span class="label">D12 · Peek</span><p class="p">p = 0.084</p><small>사용자 단위로 유의하지 않음 → 출시 안 함</small></div><div class="c"><span class="label">D21 · Fixed</span><p class="p">p = 0.0026</p><small>+2.75%p · 가드레일 유의한 악화 없음 → 단계적 배포 권고</small></div></div>'),
      ('p-value', '로그 축 · 0.05 기준선', '<div id="f-logp"></div>')], '8일차 광고 이후 구간은 전후를 나눠 탐색적으로만 해석했습니다.')}
<p class="rv">관찰 격차 10.7%p 중 실험으로 확인된 건 2.75%p였습니다. 관찰된 차이를 하나의 원인으로 돌리지 않고, 판정 규칙과 분석 단위는 결과를 보기 전에 고정했습니다.</p>
{take('판정 규칙은 결과보다 먼저')}
</div>''',
 script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-gap'), w=>{
 const X=F.lin(0,10.7,4,w-92); let s='';
 s+=`<rect x="${X(0)}" y="14" width="${X(10.7)-X(0)}" height="22" fill="none" stroke="#141414"/>`;
 s+=`<rect x="${X(0)}" y="14" width="${X(2.75)-X(0)}" height="22" fill="#1F32A8"/>`;
 s+=F.T(X(10.7)+8,30,'10.7',{disp:true,fs:16})+F.T(X(10.7)+8,46,'관찰 격차',{fs:10.5,ko:true,c:'#686868'});
 [0,2,4,6,8,10].forEach(t=>s+=F.T(X(t),56,t,{a:'middle',fs:10.5,c:'#686868'}));
 s+=F.T(X(0),76,'+2.75 · 실험으로 확인',{fs:11.5,ko:true,b:true,c:'#1F32A8'});
 return F.svg(w,82,s);});
mount(document.getElementById('f-ci'), F.ci({min:0,max:6,lo:.96,hi:4.54,est:2.75,mde:3,zeroLabel:'효과 없음'}));
mount(document.getElementById('f-days'), F.days({n:21,peek:12,ad:8,lab:[1,5,8,12,17,21]}));
mount(document.getElementById('f-logp'), F.logp({min:.001,max:1,ticks:[.001,.01,.05,.1,1],alpha:.05,pts:[{v:.0026,t:'D21'},{v:.084,t:'D12'}]}));
''')

def short(code, id_, title, ko, meta, figs, found, limit, gh=None):
    links = stag('GitHub', f'https://github.com/{gh}', '{GH}') if gh else ''
    return f'''<section class="sec" id="{id_}" style="padding-top:56px">
<div class="crumb label rv"><span>{code} · Short</span><span>/</span><span class="ko-t">{meta}</span></div>
<h2 class="ptitle rv" style="font-size:24px">{title}</h2><p class="psub rv">{ko}</p>
{'<div class="small-tags rv">' + links + '</div>' if links else ''}
<div class="body" style="margin-top:12px">{figs}
<h3 class="rv">발견</h3><p class="rv">{found}</p>
<h3 class="rv">한계</h3><p class="rv">{limit}</p></div>
</section>'''

PAGES['more.html'] = dict(title='P05–08', desc='Olist SQL · 대학 쇠퇴 · 지방소멸위험 다변량 · 빈집 회귀 진단',
 prev=('p04.html', 'P04 A/B Testing'), next=('p01.html', 'P01 Deepfake Detection'),
 body='''<div class="crumb label rv"><a href="../projects.html">Projects</a><span>/</span><span>P05–08 · Short</span></div>
<h1 class="ptitle rv">Short projects</h1>''' +
 short('P05', 'p05', 'Join Fan-out', 'Olist 이커머스 SQL 분석', "TOBIG'S SQL 과제 · MySQL 8.0",
   fig([('주문 1건이 여러 행으로 늘어나는 JOIN', 'Orders → Items × Payments · 예시', '<div id="f-fan"></div>'), ('Over-count', '', '<div id="f-over"></div>')]),
   '쿼리는 에러 없이 돌았지만, JOIN 한 번으로 결제금액이 <span class="hl">28.23%</span>(상품 판매금액은 4.48%) 과대 집계되어 있었습니다. 테이블마다 행 수와 고유 주문 수를 비교하고, 여러 행이 붙는 테이블은 <b>주문 단위로 먼저 집계</b>해 행 수를 다시 맞췄습니다.',
   '12월 매출 −26.5%가 부진인지 11월 행사 효과인지는 전년 동기 · 트래픽 데이터가 없어 확인하지 못했습니다.', gh='leebomin/tobigs-26th') +
 short('P06', 'p06', 'Effect Size', '비수도권 대학 쇠퇴현황 분석', '도시조사방법론 · 팀 5명 · 데이터 분석 · R · 2023.03–06',
   fig([('GS 누백 평균', '낮을수록 선호', '<div id="f-gs"></div>'), ('선호도 ~ 청년 순이동', '시군구 81 · 칸 하나 = 1%', '<div class="waffles" style="grid-template-columns:140px 1fr"><div data-cells="100,11,10,f"></div><div><p class="w-v">R² ≈ 0.11</p><p class="fig-note">설명된 몫은 11칸뿐입니다.</p></div></div>')]),
   'GS 누백 격차는 뚜렷했지만(수도권 24.0 vs 비수도권 52.5, Welch p&lt;0.001), 청년 순이동에 대한 설명력은 <b>11%</b>에 그쳤습니다. 유의성과 설명력을 나눠서 해석했습니다.',
   '2개 연도 · 81개 표본의 상관 분석이라 인과로 말하기 어렵습니다.') +
 short('P07', 'p07', 'Definition Bias', '지방소멸위험지수 다변량 분석', '다변량통계학 · 개인 · SAS · 2024.09–12',
   fig([('Scree · 9 components', '고유값 · 칸 하나 = 0.2', '<div id="f-scree"></div>'), ('계산식이 겹치는 두 변수', 'r = −0.908', '<div class="cards2"><div class="c"><small>독거노인 비율 = <b>독거노인</b> / <b>65세+</b></small></div><div class="c"><small>소멸위험 = <b>20–39 여성</b> / <b>65세+</b></small></div></div>')]),
   '시군구 229곳 · 변수 9개로 회귀 · PCA · 인자분석 · LDA · MANOVA를 했습니다. 변수를 9 → 5개로 줄여도 adj R² <b>0.857</b>이 유지됐고, 주성분 4개가 <b>85.3%</b>를 설명했습니다.',
   '독거노인 비율과 반응변수가 같은 분모(65세 이상)를 품고 있어, 상관 −0.908의 상당 부분은 계산식에서 나올 수 있습니다.') +
 short('P08', 'p08', 'Influence', '빈집 비율 회귀 진단', '회귀분석1 · 개인 · SAS · 2024.03–06',
   fig([("Cook’s D", '시군구 261곳 · 큰 순 정렬 · ■ = 4/n 초과 12곳', '<div data-cells="261,12,29,f"></div>'), ('adj R²', '영향점 포함 / 제외', '<div id="f-r2"></div>')]),
   'all-subsets와 stepwise가 같은 4개 변수를 골라 adj R² <b>0.587</b>. 영향점 12곳을 빼면 0.633으로 바뀌어, 이를 모형 개선이 아니라 <b>흔들림의 크기</b>로 보고했습니다.',
   '노후주택 계수는 단순 상관(+0.33)과 부호가 반대입니다. 다른 변수와 겹친 정보 때문이라 인과로 읽지 않았습니다.'),
 script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-fan'), F.fanout({}));
mount(document.getElementById('f-over'), F.hbars({min:0,max:32,ticks:[0,10,20,30],noteW:80,labelW:70,rows:[{k:'결제금액',v:28.23,vt:'+28.23%'},{k:'판매금액',v:4.48,vt:'+4.48%',c:'#8C8C8C'}]}));
mount(document.getElementById('f-gs'), F.dotrows({min:0,max:70,ticks:[0,10,20,30,40,50,60,70],tf:0,rowH:58,rows:[{k:'수도권',sub:'',pts:[{v:24,t:'24.0'}]},{k:'비수도권',sub:'Δ 28.5 · p<0.001',pts:[{v:52.5,t:'52.5'}]}]}));
mount(document.getElementById('f-scree'), F.scree({ev:[5.28,1.22,.67,.49,.47,.38,.27,.17,.02],k:4,cum:'85.3%'}));
mount(document.getElementById('f-r2'), F.hbars({min:0,max:.8,ticks:[0,.2,.4,.6,.8],noteW:110,labelW:70,rows:[{k:'포함',v:.587,vt:'0.587'},{k:'제외 시',v:.633,vt:'0.633',c:'#BABABA',note:'12곳 제외'}]}));
''')
