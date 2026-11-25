# Page content, taken from the Figma v4 deck (17 pages, 2026-11-25).

def did(items):
    lis = ''.join(f'<li><span class="n">{i+1}</span><p>{t}</p></li>' for i, t in enumerate(items))
    return f'<div class="did"><p class="label">What I did</p><ol>{lis}</ol></div>'

def facts(rows):
    return '<dl class="facts">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows) + '</dl>'

def story(blocks, take):
    b = ''.join(f'<div class="blk"><h5>0{i+1}&nbsp;&nbsp;{h}</h5><p>{t}</p></div>' for i, (h, t) in enumerate(blocks))
    return f'<div class="story">{b}<div class="takeaway"><p class="label">Takeaway</p><p>{take}</p></div></div>'

def head(code, kicker, title, sub, gh=None, sub_k=None):
    btn = f' <a class="btn" href="https://github.com/{gh}" target="_blank" rel="noopener">{{GH}}GitHub</a>' if gh else ''
    k = f'<span class="sub-k">{sub_k}</span>' if sub_k else kicker
    return f'<div class="p-kicker"><span class="chip">{code}</span>{k}{btn}</div><h1 class="p-title">{title}</h1><p class="p-sub">{sub}</p>'

def h2(code, kicker, title, sub):
    return f'<div class="p-kicker"><span class="chip">{code}</span><span class="sub-k">{kicker}</span></div><h2 class="p-title">{title}</h2><p class="p-sub">{sub}</p>'

def fig(cap, parts):
    ps = ''.join(f'<div class="fig-part"><div class="fig-head"><span class="h">{h}</span><span class="r">{r}</span></div>{body}</div>' for h, r, body in parts)
    return f'<figure class="fig rv"><figcaption class="fig-cap"><span class="label">FIG.</span>{cap}</figcaption>{ps}</figure>'

def dl(rows):
    return '<dl class="dl">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows) + '</dl>'

def table(head_, rows, num_cols=()):
    th = ''.join(f'<th>{h}</th>' for h in head_)
    trs = ''.join('<tr>' + ''.join(f'<td class="{"n" if j in num_cols else ""}">{c}</td>' for j, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<div class="dtable-wrap"><table class="dtable"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def why(t, take):
    return f'<div class="why"><p class="label">Why</p><p>{t}</p></div><div class="takeaway"><p class="label">Takeaway</p><p>{take}</p></div>'

def rowfig(k, id_, v, sub=''):
    s = f'<div class="sub">{sub}</div>' if sub else ''
    return f'<div class="rowfig"><span class="k">{k}</span><div id="{id_}"></div><span class="v">{v}</span>{s}</div>'

PAGES = {}

# ───────────────────────── P01 ─────────────────────────
PAGES['p01.html'] = dict(
    title='DEEPFAKE DETECTION', desc='멀티모달 딥페이크 탐지 모듈 · 처음 보는 데이터에서의 성능으로 모델 선정', on=[1],
    where='(P01) PROJECT · MAIN', prev=('more.html#p08', 'P08 INFLUENCE'), next=('p02.html', 'P02 PREDICTIVE MAINTENANCE'),
    body=f'''
<section class="p-sec p-hero" id="overview">
 <header class="p-head rv">{head('P01', "TOBIG'S · 멀티모달/CV 팀 · 2026.08–11", 'DEEPFAKE DETECTION', '멀티모달 딥페이크 탐지 모듈')}</header>
 <div class="p-grid">
  <div class="rv">
   <p class="p-intro">투자 사기 탐지 서비스에서 이미지 · 얼굴 영상 · 음성이 <b>합성인지</b> 판별하는 모듈을 맡았습니다.<br><b>처음 보는 데이터</b>에서의 성능으로 모델을 골랐습니다.</p>
   {did(['이미지 · 얼굴 · 음성 후보 <b>12종</b>을 외부 데이터로 비교,<br><b>부트스트랩 신뢰구간 · 짝 비교</b>로 차이가 우연이 아님을 확인',
         '저화질(<b>360p 이하</b>)에서 우세 모델 역전<br>→ 얼굴 크기(<b>170px</b>) 기준 모델 <b>자동 선택</b>',
         '외부 AUC <span class="hl">0.907 · 0.858 · 0.988</span>,<br><b>결과 전에 합격선을 고정</b>한 서비스 벤치마크 <b>8개 중 7개 통과</b>'])}
   {facts([('ROLE', '4명 중 딥페이크 탐지 모델 전담 · 비교 · 선정 · 추론 API 구현'), ('IMPACT', '백엔드 · 웹 확장이 호출하는 API로 연결 (판정 일치율 100%)'), ('MODEL', '이미지 CLIP-L/14 · 얼굴 CLIP + Xception · 음성 wav2vec2 XLS-R')])}
  </div>
  {fig('처음 보는 데이터에서의 성능', [
    ('01&nbsp;&nbsp;외부 데이터 AUC', '학습에 쓰지 않은 데이터셋', '<div id="f-auc"></div>'),
    ('02&nbsp;&nbsp;얼굴 크기로 모델 선택', '영상통화 화질 재현 실험', '<div id="f-res"></div>'),
    ('03&nbsp;&nbsp;서비스 경로 벤치마크', '기준 8개 · 결과 전에 고정', '<div class="rowfig" style="grid-template-columns:1fr 70px"><div id="f-bench"></div><span class="v">7 / 8</span></div><p class="fig-note">미달 1개 · 탭 녹화 얼굴 탐지율 0.351 (기준 0.60)<br>음성은 탭 녹화에서도 AUC 0.999</p>'),
  ])}
 </div>
</section>

<section class="p-sec" id="data">
 <div class="exp-grid">
  <div class="rv">
   {h2('P01', '데이터 · 모델 선정', 'DATA &amp; EXPERIMENT', '외부 데이터 기준 모델 선정')}
   <div style="margin-top:28px">{dl([
     ('DATA', '학습 이미지 SID_Set · OpenFake<br>얼굴 ThinothW / 음성 In-the-Wild<br>외부 평가 Community Forensics · KoDF · Celeb-DF · ASVspoof2019'),
     ('PREPROC', '형식 단서 → 384 JPEG로 다시 저장 (기준선 0.49)<br>비율 · 크기 단서 (AUC 0.694) → 정사각 크롭 재학습'),
     ('CRITERIA', '외부 2종 중 낮은 쪽 AUC 기준 1위 (0.856)<br>부트스트랩 1위 확률 100%<br>앙상블보다 유의하게 높음'),
     ('MODELS', '이미지 CLIP-L/14 다층 · 얼굴 CLIP-L/14 + Xception<br>음성 wav2vec2 XLS-R (후보 12종 중 선정)')])}</div>
  </div>
  <div class="exp-right">
   <div class="rv">{table(['MODALITY', 'EVAL SET', 'MODEL', 'EXT. AUC', 'NOTE'], [
     ['이미지', 'Community Forensics', 'CLIP-L/14 다층', '<span class="hl">0.907</span>', '정사각 크롭 · 외부 2종 1위'],
     ['얼굴 영상', 'KoDF', 'CLIP-L/14', '0.858', 'Xception 대비 +0.051'],
     ['음성', 'ASVspoof2019', 'wav2vec2 XLS-R', '0.988', '전화망 G.711 0.976'],
     ['임계값', 'KoDF', '검증셋 기준 고정', '46%', '탐지율 · 재보정 필요']], num_cols=(3,))}</div>
   <div class="exp-sub">
    {fig('처음 보는 생성기(OOD)에서의 이미지 AUC', [('OOD AUC', '정사각 크롭 전 비교', '<div id="f-ood"></div><p class="fig-note">최종 선정은 외부 2종 기준 · UnivFD 공개 가중치는 2018 GAN 학습이라 우연 수준</p>')])}
    <div class="rv">{why('내부 검증 점수는 데이터 단서까지 학습한 결과일 수 있어, 처음 보는 데이터의 AUC를 기준으로 했다. 차이가 작은 후보는 신뢰구간과 짝 비교로 우연이 아님을 확인한 뒤 골랐다.', '처음 보는 데이터의 점수로 선정')}</div>
   </div>
  </div>
 </div>
</section>

<section class="p-sec" id="finding">
 <div class="p-grid">
  <div class="rv">
   {h2('P01', 'KEY FINDING · MULTIMODAL · CV', 'SHORTCUT', '가짜 단서 학습 · 파일 형식과 비율')}
   {story([('SITUATION', '첫 파이프라인은 돌릴 때마다 결과가 크게 달라졌습니다. 이미지 내용을 보지 않는 <b>FFT 기준선</b>의 AUC가 실행마다 <b>0.015 · 0.500 · 0.601</b>로 흔들렸습니다.'),
           ('DOUBT', '진짜 이미지가 일부 샤드에서만 뽑혀 <span class="hl">파일 형식</span>이 정답과 겹쳐 있었습니다. 합성 흔적이 아니라 JPEG/PNG를 보고 맞힐 수 있는 상태였습니다.'),
           ('CHECK', '모든 이미지를 <b>384 JPEG</b>로 다시 저장하자 기준선은 <b>0.49</b>로 우연 수준이 됐습니다. 그럼에도 비율 · 크기 두 숫자만으로 <b>0.694</b>가 나와 <b>정사각 크롭</b>으로 다시 학습했습니다.')],
          '가짜 단서 제거 모델 · 서비스 API 연결')}
  </div>
  {fig('내용을 보지 않는 모델(FFT 기준선)의 AUC', [('점이 0.5(우연)에서 멀수록 데이터에 가짜 단서가 남아 있다는 뜻', '', '<div id="f-fft"></div><p class="fig-note">같은 코드가 0.015와 0.601 사이를 오간 건, 모델이 합성 흔적이 아니라 파일 형식 · 비율 같은 가짜 단서를 보고 있었다는 신호였다.</p>')])}
 </div>
</section>
''',
    script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-auc'), F.hbars({min:.4,max:1,ticks:[.4,.5,.6,.7,.8,.9,1],ref:.5,refLabel:'0.5 = 우연',noteW:170,
 rows:[{k:'IMAGE',v:.907,note:'Community Forensics'},{k:'FACE',v:.858,note:'KoDF · 한국인 얼굴'},{k:'VOICE',v:.988,note:'ASVspoof2019'}]}));
mount(document.getElementById('f-res'), w=>{
 const X=F.lin(0,5,10,w-10), r=['1080p','720p','480p',null,'360p','240p'], pos=[0,1,2,2.55,3.4,4.6];
 let s=`<line x1="${X(0)}" x2="${X(5)}" y1="40" y2="40" stroke="#C6C6C0"/>`;
 r.forEach((t,i)=>{ if(!t) return; s+=`<line x1="${X(pos[i])}" x2="${X(pos[i])}" y1="36" y2="44" stroke="#3A3A37"/>`+F.T(X(pos[i]),28,t,{a:'middle',fs:10.5,c:'#686863'}); });
 s+=`<line x1="${X(2.55)}" x2="${X(2.55)}" y1="8" y2="86" stroke="#141414" stroke-width="1.2"/>`+F.T(X(2.55),6,'얼굴 170px',{a:'middle',fs:11,ko:true,b:true});
 s+=`<rect x="${X(0)}" y="58" width="${X(2.55)-X(0)-4}" height="5" fill="#141414"/>`+F.T(X(0),80,'CLIP · 480p 이상',{fs:11,ko:true});
 s+=`<rect x="${X(2.55)+4}" y="58" width="${X(5)-X(2.55)-4}" height="5" fill="#8C8C86"/>`+F.T(X(2.55)+8,80,w<520?'XCEPTION':'XCEPTION · 360p 이하 · 얼굴 170px 미만',{fs:11,ko:true});
 return F.svg(w,92,s);});
document.getElementById('f-bench').innerHTML=PF.cells(8,i=>i<7?'f':'',8);
mount(document.getElementById('f-ood'), F.dotrows({min:.3,max:1,ticks:[.3,.5,.7,.9],ref:.5,refLabel:'0.5',rowH:28,inline:true,labelW:118,
 rows:[['CLIP 마지막 층',.878],['CLIP 다층 · 선정',.834,1],['ConvNeXt-S',.831],['DINOv2-L',.821],['Xception',.796],['EfficientNet-B4',.754],['FFT 기준선',.486],['UnivFD 공개',.398]]
 .map(([k,v,sel])=>({k,sel,sub:'',pts:[{v,t:v.toFixed(3),a:'start',dx:9,r:sel?5:3.5,c:sel?'#141414':'#8C8C86'}]}))}));
mount(document.getElementById('f-fft'), F.dotrows({min:0,max:1,ticks:[0,.2,.4,.6,.8,1],band:[.45,.55],ref:.5,refLabel:'0.5 = 우연',notes:true,rowH:92,
 rows:[{k:'01  BEFORE',sub:'같은 코드 · 실행 3번',range:true,note:'실행마다\\n제각각',pts:[{v:.015,t:'0.015'},{v:.5,t:'0.500',below:true},{v:.601,t:'0.601'}]},
       {k:'02  FIX 1',sub:'384 JPEG로 형식 통일',note:'우연 수준',pts:[{v:.49,t:'OOD 0.490',a:'start',dx:9},{v:.46,t:'외부 0.460',a:'end',dx:-9,below:true}]},
       {k:'03  남은 단서',sub:'비율 · 크기 두 숫자만',note:'→ 정사각\\n크롭 재학습',pts:[{v:.694,t:'0.694'}]}]}));
'''
)

# ───────────────────────── P02 ─────────────────────────
PAGES['p02.html'] = dict(
    title='PREDICTIVE MAINTENANCE', desc='엔진 잔여수명 확률 예측 · 정비 시점 결정', on=[2],
    where='(P02) PROJECT · MAIN', prev=('p01.html', 'P01 DEEPFAKE DETECTION'), next=('p03.html', 'P03 PILL FINDER'),
    body=f'''
<section class="p-sec p-hero" id="overview">
 <header class="p-head rv">{head('P02', '미래내일 일경험 · 제주항공 · 2026.06–07', 'PREDICTIVE MAINTENANCE', '엔진 잔여수명 확률 예측 · 정비 시점 결정', gh='leebomin/jejuairline')}</header>
 <div class="p-grid">
  <div class="rv">
   <p class="p-intro">엔진 잔여수명을 숫자 하나가 아니라 <b>확률분포</b>로 예측하고, 늦은 정비(결함)와 잦은 정비(비용)의 비대칭을 반영해 <b>정비 시점</b>을 정하는 PoC입니다.</p>
   <span class="award">에어로AI트랙 경진대회 동상 · 2026.07</span>
   {did(['평가 방식을 다시 점검해, 팀이 기대한 15~20% 개선이 <b>데이터 누수</b>였음을 발견',
         '1D-CNN 앙상블의 예측 분포를 conformal로 보정, 90% 구간이 실제로 <b>0.902</b>를 덮는 것을 확인',
         '보정된 확률로 정비 시점을 정해 정비 전 고장 확률 <span class="hl">0.196 → 0.119</span>로 감소'])}
   {facts([('ROLE', '팀장(4명) · 1D-CNN 앙상블 · conformal 공동 구현 · 보고서'), ('IMPACT', '정비 100번 중 늦은 정비 20 → 12번 · 구간 커버리지 0.902'), ('MODEL', '1D-CNN 앙상블 + conformal · 우도비 베이즈 결합')])}
  </div>
  {fig('칸 하나 = 1%', [
    ('01&nbsp;&nbsp;정비 전 고장 확률', '', '<div class="waffles"><div><div id="w-a"></div><p class="w-l">기존 정책</p><p class="w-v dim">0.196</p></div><div><div id="w-b"></div><p class="w-l">확률 보정 후</p><p class="w-v">0.119</p></div><p class="w-txt fig-note">100번 정비 결정 중 정비하기 전에 고장 나는 경우가 약 20번에서 12번으로 줄었다.</p></div>'),
    ('02&nbsp;&nbsp;90% 예측 구간 커버리지', '', '<div id="f-cov"></div><p class="fig-note">“90% 구간”이라고 예측한 범위 안에 실제 잔여수명의 90.2%가 들어왔다. 이 확률을 믿고 결정해도 된다는 근거.</p>'),
    ('03&nbsp;&nbsp;정책 시뮬레이션 · 엔진 34대 · 참고치', '칸 하나 = 엔진 1대', rowfig('평균 기반', 'e-a', '1 / 34') + rowfig('확률 기반', 'e-b', '0 / 34') + '<p class="fig-note">× = 정비 전에 고장 난 엔진 · 1대 차이라 단독 근거로 쓰지 않음</p>'),
  ])}
 </div>
</section>

<section class="p-sec" id="data">
 <div class="exp-grid">
  <div class="rv">
   {h2('P02', '데이터 · 모델 선정', 'DATA &amp; EXPERIMENT', '예측 구간 보정 · 정비 결정')}
   <div style="margin-top:28px">{dl([
     ('DATA', 'N-CMAPSS 엔진 34대 (NASA 시뮬레이션)<br>NGAFID 실비행 28,935편 (진단)'),
     ('PREPROC', '스케일러 · 변수선택을 교차검증 폴드 안에서만 fit<br>누수로 생긴 15~20% 개선 제거'),
     ('UNIT', '엔진 단위 교차검증<br>같은 엔진이 학습 · 평가에 섞이지 않게'),
     ('DECISION', '늦은 정비(결함)와 잦은 정비(비용)의 비대칭을 반영한 정비 시점')])}</div>
  </div>
  <div class="exp-right">
   <div class="rv">{table(['METRIC', 'BASELINE', 'FINAL', 'HOW'], [
     ['정비 전 고장 확률', '0.196', '<span class="hl">0.119</span>', '보정된 분포로 정비 시점 결정'],
     ['90% 구간 커버리지', '—', '0.902', '1D-CNN 앙상블 + conformal'],
     ['정책 시뮬 고장', '최선 1대', '0 / 34', '평균 기반 → 확률 기반 정책'],
     ['실비행 진단 AUC', '0.76', '0.849', '우도비 베이즈 결합']], num_cols=(1, 2))}</div>
   <div class="exp-sub">
    {fig('정비 전 고장 확률', [('평균 기반 vs 확률 기반', '', '<div id="f-pf"></div><p class="fig-note">엔진 34대 시뮬레이션 · 고장 1대 → 0대는 1대 차이라 단독 근거로 쓰지 않음</p>')])}
    <div class="rv">{why('RMSE가 데이터 규모의 한계에 닿은 뒤에는 모델을 더 키워도 정비 결정이 나아지지 않았다. 그래서 예측 구간이 실제로 90%를 덮는지(0.902)를 먼저 맞추고, 그 확률로 정비 시점을 정했다.', '모델 크기보다 예측 구간의 신뢰도')}</div>
   </div>
  </div>
 </div>
</section>

<section class="p-sec" id="finding">
 <div class="p-grid">
  <div class="rv">
   {h2('P02', 'KEY FINDING · 항공 정비', 'LEAKAGE', '데이터 누수 점검 · 폴드 안 전처리')}
   {story([('SITUATION', '‘LCC 단거리 가중치’를 넣자 RMSE가 <b>15~20% 개선</b>됐습니다. 같은 데이터로 실험한 팀원들의 결과와 비교하면 지나치게 큰 폭이었습니다.'),
           ('DOUBT', '개선폭이 실행마다 들쭉날쭉했습니다. 확인해 보니 스케일러와 변수 선택이 <span class="hl">교차검증 폴드 밖에서 fit</span>되어, 평가셋 정보가 학습에 섞이고 있었습니다.'),
           ('CHECK', '전처리를 폴드 안으로 옮기자 효과는 <b>≈ 0</b>으로 사라졌습니다. 가설을 기각하고, 같은 원인으로 생긴 <b>버그 5건</b>도 함께 고쳤습니다.')],
          '좋은 수치일수록 출처부터')}
  </div>
  {fig('차이는 전처리를 언제 하느냐 하나', [
    ('BEFORE · 전처리 먼저, 나누기는 나중', '', '<div class="flow"><div class="box"><span class="label">DATA</span><p>전체 데이터<br><small style="font-weight:500">평가 데이터 포함</small></p></div><span class="arr">→</span><div class="box"><span class="label">FIT</span><p>스케일러 · 변수 선택<br><small style="font-weight:500">전체 데이터 기준</small></p></div><span class="arr">→</span><div class="box"><span class="label">SPLIT</span><p>학습 / 평가</p></div></div><p class="fig-note">평가 데이터까지 보고 전처리 기준을 정했다 → 평가 점수가 부풀려짐</p>'),
    ('AFTER · 나누기 먼저, 전처리는 학습 데이터로만', '', '<div class="flow"><div class="box"><span class="label">SPLIT</span><p>학습 / 평가</p></div><span class="arr">→</span><div class="box"><span class="label">FIT</span><p>스케일러 · 변수 선택<br><small style="font-weight:500">학습 데이터 기준</small></p></div><span class="arr">→</span><div class="box"><span class="label">APPLY</span><p>평가에는 적용만</p></div></div><p class="fig-note">평가 데이터는 마지막에 점수를 매길 때만 쓴다</p>'),
    ('결과 · RMSE 개선폭', '', '<div id="f-rmse"></div><p class="fig-note">개선처럼 보였던 15~20%는 평가 데이터를 미리 본 효과였다.</p>'),
  ])}
 </div>
</section>
''',
    script='''
const {mount}=PF, F=FIG;
document.getElementById('w-a').innerHTML=PF.cells(100,i=>i>=80?'g':'',10);
document.getElementById('w-b').innerHTML=PF.cells(100,i=>i>=88?'f':'',10);
mount(document.getElementById('f-cov'), F.target({v:.902,t:.9,tl:'목표 90%',vt:'0.902'}));
document.getElementById('e-a').innerHTML=PF.cells(34,i=>i===23?'x':'f',34);
document.getElementById('e-b').innerHTML=PF.cells(34,'f',34);
mount(document.getElementById('f-pf'), F.hbars({min:0,max:.25,ticks:[0,.05,.1,.15,.2,.25],noteW:90,
 rows:[{k:'평균 기반',v:.196,c:'#B9B9B3',vt:'0.196'},{k:'확률 기반',v:.119,vt:'0.119',vc:'#1F32A8'}]}));
mount(document.getElementById('f-rmse'), w=>{
 const X=F.lin(0,22,70,w-90); let s='';
 [0,5,10,15,20].forEach(t=>{s+=`<line x1="${X(t)}" x2="${X(t)}" y1="4" y2="76" stroke="#C6C6C0" stroke-width=".6"/>`+F.T(X(t),92,t+'%',{a:'middle',fs:10.5,c:'#686863'});});
 s+=F.T(0,24,'BEFORE',{fs:11,b:true})+`<rect x="${X(0)}" y="12" width="${X(15)-X(0)}" height="16" fill="#141414"/>`;
 for(let x=X(15);x<X(20);x+=4) s+=`<rect x="${x}" y="12" width="2" height="16" fill="#141414"/>`;
 s+=F.T(X(20)+8,25,'+15~20%',{disp:true,fs:17});
 s+=F.T(0,62,'AFTER',{fs:11,b:true})+`<rect x="${X(0)}" y="50" width="3" height="16" fill="#141414"/>`+F.T(X(0)+12,63,'≈ 0',{disp:true,fs:17});
 return F.svg(w,98,s);});
'''
)

# ───────────────────────── P03 ─────────────────────────
PAGES['p03.html'] = dict(
    title='PILL FINDER', desc='알약 찾기 도우미 · 공식 문서 근거 LLM 웹앱', on=[3],
    where='(P03) PROJECT · MAIN', prev=('p02.html', 'P02 PREDICTIVE MAINTENANCE'), next=('p04.html', 'P04 A/B TESTING'),
    body=f'''
<section class="p-sec p-hero" id="overview">
 <header class="p-head rv">{head('P03', '네이버클라우드 에이전틱 AI 과정 · 데모 · 2026.11', 'PILL FINDER', '알약 찾기 도우미 · 공식 문서 근거 LLM 웹앱', gh='leebomin/pill-finder')}</header>
 <div class="p-grid">
  <div class="rv">
   <p class="p-intro">공식 자료만 근거로 알약 후보를 찾고, 일반의약품에 한해 <b>쉬운 말 요약</b>과 질문 답변을 주는 웹앱입니다. 진단 · 복용 지시는 하지 않습니다.</p>
   {did(['계산 · 규칙은 코드, 답변은 HyperCLOVA X, 검토는 Claude API<br>→ <span class="hl">모델에게 맡기지 않을 것</span>부터 정의',
         '표현 목록에 걸리지 않은 응급 질문을 Qwen3 4B가 한 번 더 판단, 감지율 <b>3/20 → 20/20</b>',
         '모든 답변에 근거 문단 또는 “공식 자료에 없음” 표시(<b>20/20</b>), 개인정보는 확인 전 외부 전송 차단(<b>9/10</b> 가림)'])}
   {facts([('ROLE', '개인 · 기획 · 모델 역할 설계 · 앱 · MCP 도구 구현 · 평가 설계'), ('IMPACT', '완료 기준 19개 중 17개 충족 · 외부 호출 없는 무료 모드로도 동작'), ('MODEL', 'HyperCLOVA X(답변) · Qwen3 4B(판단) · Claude API(검토)')])}
  </div>
  {fig('단계별 역할 · 평가 결과', [
    ('01&nbsp;&nbsp;응급 질문 감지', '칸 하나 = 질문 1개', rowfig('KEYWORD LIST', 'c-1', '3 / 20') + rowfig('+ QWEN3 4B', 'c-2', '20 / 20')),
    ('02&nbsp;&nbsp;PIPELINE', '모델에게 맡기지 않을 것부터', '<div class="flow"><div class="box"><span class="label">QUESTION</span><p>입력</p></div><span class="arr">→</span><div class="box"><span class="label">EMERGENCY</span><p>코드 + Qwen3 4B</p></div><span class="arr">→</span><div class="box"><span class="label">RETRIEVE</span><p>식약처 원문</p></div><span class="arr">→</span><div class="box on"><span class="label">ANSWER</span><p>HyperCLOVA X</p></div><span class="arr">→</span><div class="box"><span class="label">REVIEW</span><p>Claude API</p></div></div><div class="flow-sub"><span>규칙 · 검색은 코드</span><span>답변 · 검토만 LLM</span></div>'),
    ('03&nbsp;&nbsp;안전 장치', '칸 하나 = 1건', rowfig('CITATION', 'c-3', '20 / 20', '근거 문단 또는 “공식 자료에 없음” 표시') + rowfig('PII MASK', 'c-4', '9 / 10', '확인 전 외부 전송 0 / 10') + rowfig('DONE', 'c-5', '17 / 19', '남은 2개는 사진 인식 측정 필요')),
  ])}
 </div>
</section>

<section class="p-sec" id="finding">
 <div class="p-grid">
  <div class="rv">
   {h2('P03', 'KEY FINDING · LLM · EVAL', 'EVAL SET', '고정 평가셋 40문항 · 재측정')}
   {story([('SITUATION', '‘삼켰’, ‘한꺼번에’ 같은 <b>표현 목록</b>만으로는 응급 질문을 <b>3/20</b>밖에 잡지 못했습니다.'),
           ('DOUBT', '규칙을 고칠 때마다 직접 만든 질문으로 확인하면, 규칙에 맞춘 질문만 통과하는 <b>착시</b>가 생길 수 있었습니다.'),
           ('CHECK', '규칙을 보지 않은 에이전트가 쓴 <span class="hl">새 질문 40개</span>를 먼저 고정하고 그것으로만 평가했습니다. Qwen3 4B 판단을 더하자 <b>20/20</b>, 평가셋 안 추가 오탐 <b>0</b>, 약 <b>0.4초</b>였습니다.')],
          '응급 질문 감지 3/20 → 20/20')}
  </div>
  {fig('규칙과 시험지를 다른 손에서', [
    ('01&nbsp;&nbsp;SEPARATION', '규칙을 만든 쪽과 질문을 만든 쪽', '<div class="cards2" style="position:relative"><div class="c"><span class="label">RULE · 규칙</span><small style="font-size:14px;font-weight:700;color:var(--ink);margin-top:6px">표현 목록 + Qwen3 4B 판단</small></div><div class="c"><span class="label">AGENT · 질문 작성</span><small style="font-size:14px;font-weight:700;color:var(--ink);margin-top:6px">규칙을 보지 않고 질문 작성</small></div></div><p class="fig-note" style="text-align:center">┆ 서로 비공개 ┆</p>'),
    ('02&nbsp;&nbsp;EVAL SET', '시험지 먼저 고정', '<div class="flow"><div class="box"><span class="label">STEP 1</span><p>질문 40개 먼저 고정</p></div><span class="arr">→</span><div class="box"><span class="label">STEP 2</span><p>규칙 · 모델 수정</p></div><span class="arr">→</span><div class="box"><span class="label">STEP 3</span><p>같은 40개로 재측정</p></div></div><div class="flow-sub"><span></span><span>↺ 2 → 3 반복 · 시험지는 바꾸지 않음</span></div>'),
    ('03&nbsp;&nbsp;RESULT', '같은 40개로만 측정', rowfig('KEYWORD LIST', 'r-1', '3 / 20') + rowfig('+ QWEN3 4B', 'r-2', '20 / 20', '평가셋 기준 추가 오탐 0 · 응답 약 0.4초') + rowfig('LIMIT', 'r-3', '2 / 20', '가정형 질문에도 119 안내가 뜨는 오탐 · 미해결 · 의료인 검수 전 데모')),
  ])}
 </div>
</section>
''',
    script='''
const C=(id,n,k,cls)=>document.getElementById(id).innerHTML=PF.cells(n,i=>i<k?(cls||'f'):'',n);
C('c-1',20,3);C('c-2',20,20);C('c-3',20,20);C('c-4',10,9);C('c-5',19,17);
C('r-1',20,3);C('r-2',20,20);C('r-3',20,2,'g');
'''
)

# ───────────────────────── P04 ─────────────────────────
PAGES['p04.html'] = dict(
    title='A/B TESTING', desc='숙박 앱 전환율 A/B 테스트 · 사전 판정 규칙', on=[4],
    where='(P04) PROJECT · MAIN', prev=('p03.html', 'P03 PILL FINDER'), next=('more.html', 'P05–08 SHORT'),
    body=f'''
<section class="p-sec p-hero" id="overview">
 <header class="p-head rv">{head('P04', "TOBIG'S · DA 트랙 과제 · 2026.10", 'A/B TESTING', '숙박 앱 전환율 A/B 테스트 · 사전 판정 규칙', gh='leebomin/tobigs-26th')}</header>
 <div class="p-grid">
  <div class="rv">
   <p class="p-intro">분석팀이 진단한 목록 → 상세 전환율 <b>약 10.7%p 격차</b>를 개선안으로 바꾸고, <b>결과를 보기 전에 정한 규칙</b>대로 실험을 설계 · 판정했습니다.</p>
   {did(['<b>사용자 단위</b> 배정 · delta method로 분산 보정, 디자인 효과 <b>1.59 → 2.11</b>을 반영해 MDE 3%p · 기간 <b>21일</b> 설정',
         '배정 비율(SRM p=0.71)과 <b>8일차 광고 캠페인</b> 전후를 분리 확인, 광고 이후 구간은 탐색적으로만 해석',
         '목록 → 상세 전환율 <span class="hl">+2.75%p</span> (95% CI 0.96~4.54, p=0.0026), 가드레일 유의한 악화 없음 → <b>단계적 배포 권고</b>'])}
   {facts([('ROLE', '개인 과제 · 실험 설계 · 판정 규칙 · 분석 전 과정'), ('IMPACT', '+2.75%p · 가드레일 유의한 악화 없음 → 단계적 배포 권고'), ('METHOD', '사용자 단위 배정 · delta method · SRM 검정 · MDE')])}
  </div>
  {fig('격차 · 배정 · 효과 구간', [
    ('01&nbsp;&nbsp;GAP', '관찰 격차 중 실험으로 확인된 몫 · %p', '<div id="f-gap"></div>'),
    ('02&nbsp;&nbsp;ASSIGNMENT', 'SRM p = 0.71', '<div id="f-asg"></div><p class="fig-note">사용자 단위 배정 · 두 그룹 비율이 기대와 다르지 않음</p>'),
    ('03&nbsp;&nbsp;EFFECT', '목록 → 상세 전환율 · 95% CI · %p', '<div id="f-ci"></div><p class="fig-note">구간 전체가 0보다 큼 → 효과 있음 · p = 0.0026<br>매출 증가는 이 실험으로 확인하지 않음</p>'),
  ])}
 </div>
</section>

<section class="p-sec" id="finding">
 <div class="p-grid">
  <div class="rv">
   {h2('P04', 'KEY FINDING · EXPERIMENT', 'PEEKING', '중간 확인(peeking) · 고정 기간 판정')}
   {story([('SITUATION', '같은 데이터로 <b>고정 기간 21일 판정</b>과 <b>매일 확인 후 중단</b>하는 방식을 비교했습니다.'),
           ('DOUBT', '매일 p값을 보다 멈추면 우연히 낮아진 날 결론이 나거나, 효과가 있어도 <b>출시를 접는</b> 판단이 나올 수 있었습니다.'),
           ('CHECK', '12일차에 멈추면 사용자 단위 p=<b>0.084</b>로 출시하지 않는 결론이었고, <span class="hl">21일 고정 판정</span>에서는 p=<b>0.0026</b>, +2.75%p였습니다.')],
          '판정 규칙은 결과보다 먼저')}
  </div>
  {fig('같은 데이터 · 다른 중단 규칙', [
    ('01&nbsp;&nbsp;TIMELINE', '21일 · 칸 하나 = 하루', '<div id="f-days"></div>'),
    ('02&nbsp;&nbsp;DECISION', '같은 데이터 · 다른 규칙', '<div class="cards2"><div class="c"><span class="label">D12 · PEEK</span><p class="p">p = 0.084</p><small>사용자 단위로 유의하지 않음<br>→ 출시 안 함</small></div><div class="c on"><span class="label">D21 · FIXED</span><p class="p">p = 0.0026</p><small>+2.75%p · 가드레일 유의한 악화 없음<br>→ 단계적 배포 권고</small></div></div>'),
    ('03&nbsp;&nbsp;P-VALUE', '로그 축 · 0.05 기준선', '<div id="f-logp"></div><p class="fig-note">8일차 광고 이후 구간은 전후를 나눠 탐색적으로만 해석</p>'),
  ])}
 </div>
</section>
''',
    script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-gap'), w=>{
 const X=F.lin(0,12,4,w-70); let s='';
 s+=`<rect x="${X(0)}" y="14" width="${X(10.7)-X(0)}" height="24" fill="none" stroke="#141414"/>`;
 s+=`<rect x="${X(0)}" y="14" width="${X(2.75)-X(0)}" height="24" fill="#1F32A8"/>`;
 s+=F.T(X(10.7)+8,32,'10.7',{disp:true,fs:18})+F.T(X(10.7)+8,48,'관찰 격차',{fs:10.5,ko:true,c:'#686863'});
 [0,2,4,6,8,10,12].forEach(t=>s+=F.T(X(t),58,t,{a:'middle',fs:10.5,c:'#686863'}));
 s+=F.T(X(0),78,'+2.75 · 실험으로 확인',{fs:11.5,ko:true,b:true,c:'#1F32A8'});
 return F.svg(w,84,s);});
mount(document.getElementById('f-asg'), F.hbars({min:0,max:3600,ticks:[],noteW:70,labelW:110,
 rows:[{k:'A · CONTROL',v:3446,vt:'3,446',c:'#4A4A47'},{k:'B · 할인가',v:3415,vt:'3,415',c:'#4A4A47'}]}));
mount(document.getElementById('f-ci'), F.ci({min:0,max:6,lo:.96,hi:4.54,est:2.75,mde:3,zeroLabel:'효과 없음'}));
mount(document.getElementById('f-days'), F.days({n:21,peek:12,ad:8,lab:[1,5,8,12,17,21]}));
mount(document.getElementById('f-logp'), F.logp({min:.001,max:1,ticks:[.001,.01,.05,.1,1],alpha:.05,
 pts:[{v:.0026,t:'D21',c:'#141414'},{v:.084,t:'D12',c:'#141414'}]}));
'''
)

# ───────────────────────── P05–P08 ─────────────────────────
def short(code, id_, meta, title, sub, figcap, figbody, found, limit, gh=None):
    btn = f' <a class="btn" href="https://github.com/{gh}" target="_blank" rel="noopener">{{GH}}GitHub</a>' if gh else ''
    return f'''<article class="short" id="{id_}">
  <div class="p-kicker rv"><span class="chip">{code}</span>{meta}{btn}</div>
  <h2 class="p-title rv">{title}</h2><p class="p-sub rv">{sub}</p>
  {fig(figcap, [('', '', figbody)])}
  <div class="fl rv"><div><h5>FOUND</h5><p>{found}</p></div><div><h5>LIMIT</h5><p>{limit}</p></div></div>
</article>'''

PAGES['more.html'] = dict(
    title='P05–08 SHORT', desc='Olist SQL · 대학 쇠퇴 · 지방소멸위험 다변량 · 빈집 회귀 진단', on=[5, 6, 7, 8],
    where='(P05–08) PROJECT · SHORT', prev=('p04.html', 'P04 A/B TESTING'), next=('p01.html', 'P01 DEEPFAKE DETECTION'),
    body=f'''
<section class="p-sec p-hero">
 <div class="sec-head rv"><h1 class="sec-title">SHORT</h1><p class="sec-meta">P05–P08 · 2023–2026</p></div>
 <div class="short-grid">
 {short('P05', 'p05', "TOBIG'S · SQL 과제 · MySQL 8.0", 'JOIN FAN-OUT', 'Olist 이커머스 SQL 분석', '주문 1건이 여러 행으로 늘어나는 JOIN',
   '<p class="label" style="margin-bottom:10px">ORDERS → JOIN ITEMS × PAYMENTS · 예시</p><div id="f-fan"></div><div style="margin-top:18px"><p class="label">OVER-COUNT</p><div id="f-over"></div></div>',
   'JOIN 한 번으로 결제금액이 <span class="hl">28.23%</span> 과대 집계됐습니다. <b>주문 단위로 먼저 집계</b>해 행 수를 다시 맞췄습니다.', '12월 −26.5%의 원인은 미확인', gh='leebomin/tobigs-26th')}
 {short('P06', 'p06', '도시조사방법론 · 팀 5명 · 데이터 분석 · R · 2023.03–06', 'EFFECT SIZE', '비수도권 대학 쇠퇴현황 분석', '격차는 크고, 설명력은 작다',
   '<p class="label" style="margin-bottom:6px">GS 누백 평균 · 낮을수록 선호</p><div id="f-gs"></div><div class="waffles" style="margin-top:18px;grid-template-columns:150px 1fr"><div id="w-r2"></div><div><p class="w-l">선호도 ~ 청년 순이동 · 시군구 81</p><p class="w-v">R² ≈ 0.11</p><p class="fig-note">칸 하나 = 1% · 설명된 몫 11칸</p></div></div>',
   'GS 누백 격차는 뚜렷했지만 (수도권 24.0 vs 52.5, p&lt;0.001) 청년 순이동에 대한 설명력은 <b>11%</b>에 그쳤습니다.', '2개 연도 · 81개 표본, 인과 아님')}
 {short('P07', 'p07', '다변량통계학 · 개인 · SAS · 2024.09–12', 'DEFINITION BIAS', '지방소멸위험지수 다변량 분석', '주성분 4개 · 계산식이 겹치는 변수',
   '<p class="label" style="margin-bottom:6px">SCREE · 9 COMPONENTS · EIGENVALUE · 칸 하나 = 0.2</p><div id="f-scree"></div><div style="margin-top:18px"><p class="label" style="margin-bottom:8px">두 변수의 계산식이 같은 분모를 품는다 · r = −0.908</p><div class="cards2"><div class="c"><small>독거노인 비율 =<br><b>독거노인</b> / <b>65세+</b></small></div><div class="c"><small>소멸위험 =<br><b>20–39 여성</b> / <b>65세+</b></small></div></div></div>',
   '변수를 9 → 5개로 줄여도 adj R² <b>0.857</b>이 유지됐고, 주성분 4개가 <b>85.3%</b>를 설명했습니다.', '공통 분모로 상관이 과장될 수 있음')}
 {short('P08', 'p08', '회귀분석1 · 개인 · SAS · 2024.03–06', 'INFLUENCE', '빈집 비율 회귀 진단', '영향점 12곳 · 계수 부호 반전',
   '<p class="label" style="margin-bottom:8px">COOK’S D · 시군구 261곳 · 큰 순 정렬 · ■ = 4/n 초과 12곳</p><div id="c-261"></div><div style="margin-top:18px"><p class="label">adj R² · 영향점 포함 / 제외</p><div id="f-r2"></div></div><div style="margin-top:14px"><p class="label" style="margin-bottom:8px">노후주택 · 단순 상관 vs 회귀 계수</p><div class="cards2"><div class="c"><span class="label">단순 상관</span><p class="p">+0.33</p></div><div class="c"><span class="label">회귀 계수</span><p class="p">(−)</p><small>다른 변수와 겹친 정보 때문에 부호 반전</small></div></div></div>',
   '두 방법이 같은 4개 변수를 골라 adj R² <b>0.587</b>. 영향점 12곳을 빼면 0.633으로 바뀌어 <b>흔들림의 크기</b>를 보고했습니다.', '계수 부호를 인과로 읽지 않음')}
 </div>
</section>
''',
    script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-fan'), F.fanout({}));
mount(document.getElementById('f-over'), F.hbars({min:0,max:32,ticks:[0,10,20,30],noteW:80,labelW:70,
 rows:[{k:'결제금액',v:28.23,vt:'+28.23%'},{k:'판매금액',v:4.48,vt:'+4.48%',c:'#8C8C86'}]}));
mount(document.getElementById('f-gs'), F.dotrows({min:0,max:70,ticks:[0,10,20,30,40,50,60,70],tf:0,rowH:62,
 rows:[{k:'수도권',sub:'',pts:[{v:24,t:'24.0'}]},{k:'비수도권',sub:'Δ 28.5 · p<0.001',pts:[{v:52.5,t:'52.5'}]}]}));
document.getElementById('w-r2').innerHTML=PF.cells(100,i=>i<11?'f':'',10);
mount(document.getElementById('f-scree'), F.scree({ev:[5.28,1.22,.67,.49,.47,.38,.27,.17,.02],k:4,cum:'85.3%'}));
document.getElementById('c-261').innerHTML=PF.cells(261,i=>i<12?'f':'',29);
mount(document.getElementById('f-r2'), F.hbars({min:0,max:.8,ticks:[0,.2,.4,.6,.8],noteW:120,labelW:70,
 rows:[{k:'포함',v:.587,vt:'0.587'},{k:'제외 시',v:.633,vt:'0.633',c:'#B9B9B3',note:'12곳 제외'}]}));
'''
)
