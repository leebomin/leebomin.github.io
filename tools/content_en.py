# English site text. Mirrors content.py; keep facts in sync when editing either file.
from content import DEMO_P03, stag, thumb, pitem, top, fig, h2, take, rowfig, table, dl

_P = ([
  pitem('P01', "TOBIG'S · Multimodal/CV team · 2026", 'Deepfake Detection', 'Multimodal deepfake detection module',
        'Compared 12 image, face-video and voice candidates on <b>data they had never seen</b>, after first removing a fake cue left in the file format.',
        'works/p01.html', thumb((100, 91, 10, 'f'), 'External AUC · cell=0.01', '0.907')),
  pitem('P02', 'Future Work Experience · Jeju Air · 2026 · Bronze', 'Predictive Maintenance', 'When to service an aircraft engine',
        'Predicted remaining useful life as a probability distribution to time maintenance, and found that the expected 15–20% gain was <b>data leakage</b>.',
        'works/p02.html', thumb((100, 12, 10, 'f'), 'Failure before service · cell=1%', '0.119'), gh='leebomin/jejuairline'),
  pitem('P03', 'NAVER Cloud Agentic AI course · 2026', 'Pill Finder', 'LLM web app grounded in official documents',
        'Decided first what the model should not do, then evaluated on 40 questions written without seeing the rules. Emergency detection <b>3/20 → 20/20</b>.',
        'works/p03.html', thumb((20, 20, 10, 'f'), 'Emergency questions caught', '20/20'), gh='leebomin/pill-finder', demo=DEMO_P03),
  pitem('P04', "TOBIG'S · DA track assignment · 2026", 'A/B Testing', 'Conversion experiment for a lodging app',
        'Fixed the decision rule before looking at results. Stopping on day 12 would have reversed the conclusion; the fixed 21-day rule confirmed the effect.',
        'works/p04.html', thumb((12, 3, 12, 'f'), 'Of a 10.7 observed gap · %p', '+2.75'), gh='leebomin/tobigs-26th'),
  pitem('P05', "TOBIG'S · SQL assignment · 2026", 'Join Fan-out', 'Olist e-commerce SQL analysis',
        'A query that ran without errors inflated payment totals by 28.23% through duplicated JOIN rows.',
        'works/more.html#p05', thumb((100, 28, 10, 'f'), 'Over-count · cell=1%', '+28.23%'), gh='leebomin/tobigs-26th'),
  pitem('P06', 'Urban Research Methods · team · 2023', 'Effect Size', 'Decline of universities outside the capital region',
        'The gap was clear (p&lt;0.001), yet it explained only 11% of young people’s net migration.',
        'works/more.html#p06', thumb((100, 11, 10, 'f'), 'Explained R² · cell=1%', '0.11')),
  pitem('P07', 'Multivariate Statistics · solo · 2024', 'Definition Bias', 'Multivariate analysis of the local extinction index',
        'Showed that the strongest factor may come from a denominator shared with the index formula.',
        'works/more.html#p07', thumb((100, 85, 10, 'f'), 'PC1–4 cumulative · cell=1%', '85.3%')),
  pitem('P08', 'Regression Analysis I · solo · 2024', 'Influence', 'Regression diagnostics for vacant-house rates',
        'Reported how much the fit moves when 12 influential points are removed, as a measure of instability.',
        'works/more.html#p08', thumb((261, 12, 29, 'f'), 'Influential points · 261 districts', '12')),
])
PROJECTS = ''.join(_P)
MAIN4 = ''.join(_P[:4])

INDEX = dict(title='Bomin Lee · Data Scientist', desc='Portfolio of Bomin Lee, data scientist. Experiment design · model evaluation and validation · statistical modeling · LLM services.', body=f'''
<section id="about" class="rv">
  <div class="photo m" data-src="{{A}}assets/img/portrait.png" aria-label="Photo of Bomin Lee. Tap to turn it into pixel art."></div>
  <h1 class="headline"><span class="ko">Hi, I’m Bomin Lee.</span></h1>
  <div class="prose">
    <p>I study Urban Administration and Statistics at the University of Seoul.</p>
    <p>I build models, then check again whether their results actually hold up.<br>Recently I built deepfake detection, aircraft engine maintenance prediction, and an LLM web app grounded in official documents.</p>
  </div>
  <div class="tags"><span class="tag">Experiment design</span><span class="tag">Model evaluation · validation</span><span class="tag">Statistical modeling</span><span class="tag">LLM services</span></div>
</section>

<section class="sec" id="projects">
  <h2 class="sec-t">Selected Projects</h2>
  <div class="plist">{MAIN4}</div>
  <p class="more rv"><a href="projects.html">All projects {{AR}}</a><a href="cv.html">CV {{AR}}</a></p>
</section>
''')

PROJECTS_PAGE = dict(title='Projects · Bomin Lee', desc='Projects by Bomin Lee: model evaluation, experiment design, statistical analysis, LLM services.', body=f'''
<h1 class="pg-t rv">Projects</h1>
<div class="plist">{PROJECTS}</div>
''')

CV_PAGE = dict(title='CV · Bomin Lee', desc='Experience, education, skills and certificates of Bomin Lee.', body='''
<h1 class="pg-t rv">CV</h1>
<section class="sec" id="experience" style="padding-top:0">
  <h2 class="sec-t">Experience</h2>
  <ul class="rows rv">
    <li><time>2026.08–</time><span>TOBIG'S 26th cohort · DA track · Multimodal/CV team</span><span class="r">P01 · P04 · P05</span></li>
    <li><time>2026.06–11</time><span>AI Agent Bootcamp · incl. NAVER Cloud course</span><span class="r">P03</span></li>
    <li><time>2026.06–07</time><span>Future Work Experience · Aerospace Industry-Academia Institute × Jeju Air</span><span class="r">P02 · Bronze</span></li>
    <li><time>2025.09–12</time><span>Youth Intern, Land Policy Division, Ministry of Land, Infrastructure and Transport</span><span class="r"></span></li>
    <li><time>2025.01–05</time><span>Exchange student, Tampere University · Finland</span><span class="r"></span></li>
    <li><time>2024.03–25.02</time><span>Statistics Korea student reporter, 16th cohort</span><span class="r">Articles on statistics</span></li>
    <li><time>2022.03–</time><span>University of Seoul · Urban Administration, Statistics</span><span class="r">GPA 4.19 / 4.5</span></li>
  </ul>
</section>

<section class="sec" id="skills">
  <h2 class="sec-t">Skills &amp; Credentials</h2>
  <div class="skills rv">
    <div><b>Python</b><span>pandas · sklearn · PyTorch</span></div>
    <div><b>SQL</b><span>MySQL · SQLite</span></div>
    <div><b>R · SAS</b><span>R · SAS · Jamovi</span></div>
    <div><b>Tests · Regression</b><span>t-test · regression · VIF</span></div>
    <div><b>Experiment design</b><span>SRM · MDE · CI</span></div>
    <div><b>ML · DL</b><span>CLIP · 1D-CNN</span></div>
    <div><b>LLM · RAG</b><span>RAG · MCP · ChromaDB · Ollama</span></div>
    <div><b>Certificates</b><span>ADsP · SQLD · TEPS 363 · OPIc IH</span></div>
  </div>
</section>

<section class="sec" id="contact">
  <h2 class="sec-t">Contact</h2>
  <p class="prose rv" style="margin-top:0"><a class="u" href="mailto:ibomin88@gmail.com">ibomin88@gmail.com</a></p>
</section>
''')

PAGES = {}

PAGES['p01.html'] = dict(title='Deepfake Detection', desc='Multimodal deepfake detection module · models chosen by performance on unseen data',
 prev=('more.html#p08', 'P08 Influence'), next=('p02.html', 'P02 Predictive Maintenance'),
 body=top('P01', 'Main', 'Deepfake Detection', 'Multimodal deepfake detection module', [],
  [('Period', '2026.08–11'), ('Team', "TOBIG'S Multimodal/CV team · 4"), ('Role', 'Owned the detection models · comparison · selection · inference API'), ('Model', 'Image CLIP-L/14 · Face CLIP + Xception · Voice wav2vec2 XLS-R')]) + f'''
<div class="body">
<p class="rv">For an investment-fraud detection service (a browser extension), I owned the module that decides whether an image, face video or voice is <b>synthetic</b>. We needed a model that holds up on <b>data it has never seen</b>, not one that scores well on its training data, so the AUC on external datasets not used for training was the first criterion.</p>
{fig([('External AUC', 'Datasets not used for training', '<div id="f-auc"></div>')], 'All three modalities were measured on external data. The dashed line at 0.5 is chance.')}

{h2('What I did', '')}
<ol class="steps rv">
<li>Compared <b>12</b> image, face and voice candidates on external data, and used <b>bootstrap confidence intervals and paired comparisons</b> to make sure the differences were not chance.</li>
<li>Reproducing video-call quality showed the winning model flips at low resolution (<b>360p and below</b>). The service now picks a model automatically by face size (<b>170px</b>).</li>
<li>Passed <b>7 of 8</b> service benchmarks whose thresholds were fixed before seeing results, and connected the module to an API called by the backend and the extension (100% verdict agreement).</li>
</ol>
{fig([('Model choice by face size', 'Video-call quality experiment', '<div id="f-res"></div>'), ('Service-path benchmarks', '8 criteria · fixed in advance', '<div class="rowfig" style="grid-template-columns:1fr 56px"><div data-cells="8,7,8,f" style="max-width:320px"></div><span class="v">7 / 8</span></div><p class="fig-note">The one miss: face detection rate on tab recordings, 0.351 (target 0.60). Voice reached AUC 0.999 even on tab recordings.</p>')])}

{h2('Key finding', 'Shortcut · fake cues')}
<h3 class="rv">Situation</h3>
<p class="rv">The first pipeline gave very different results on every run. The AUC of an <b>FFT baseline</b> that never looks at image content swung between <b>0.015 · 0.500 · 0.601</b>.</p>
<h3 class="rv">Doubt</h3>
<p class="rv">Real images had been drawn from only some shards, so the <span class="hl">file format</span> overlapped with the label. A model could answer by looking at JPEG vs PNG rather than synthesis traces.</p>
<h3 class="rv">Check</h3>
<p class="rv">After re-saving every image as <b>384 JPEG</b>, the baseline fell to <b>0.49</b>, chance level. Aspect ratio and size alone still reached <b>0.694</b>, so I retrained with <b>square crops</b>.</p>
{fig([('', '', '<div id="f-fft"></div>')], 'AUC of a model that ignores content (FFT baseline). The farther a dot is from 0.5 (grey band), the more fake cues remain in the data.')}
{take('Fake cues removed · model connected to the service API')}

{h2('Data &amp; Experiment', 'Data · model selection')}
{dl([('Data', 'Training: images SID_Set · OpenFake / faces ThinothW / voice In-the-Wild<br>External eval: Community Forensics · KoDF · Celeb-DF · ASVspoof2019'),
     ('Preproc', 'Format cue → re-saved as 384 JPEG (baseline 0.49)<br>Ratio · size cue (AUC 0.694) → retrained on square crops'),
     ('Criteria', 'Best on the lower AUC of two external sets (0.856) · bootstrap P(best) 100% · significantly above the ensemble')])}
{table(['Modality', 'Eval set', 'Model', 'Ext. AUC', 'Note'], [
  ['Image', 'Community Forensics', 'CLIP-L/14 multi-layer', '0.907', 'Square crop · best on both external sets'],
  ['Face video', 'KoDF', 'CLIP-L/14', '0.858', '+0.051 over Xception'],
  ['Voice', 'ASVspoof2019', 'wav2vec2 XLS-R', '0.988', 'Phone line G.711 0.976'],
  ['Threshold', 'KoDF', 'Fixed on validation set', '46%', 'Detection rate · needs recalibration']], (3,))}
{fig([('AUC on unseen generators (OOD)', 'Before square cropping', '<div id="f-ood"></div>')], 'Final selection used the two external sets. Public UnivFD weights were trained on 2018 GANs and sit at chance.')}
<p class="rv">Internal validation scores can include the data cues the model learned, so I chose by AUC on unseen data. When candidates were close, I picked only after confidence intervals and paired comparisons showed the gap was real. AUC held, but at a fixed threshold the face detection rate dropped to 46%, so I also handed over the sample size needed for recalibration.</p>
{take('Chosen by scores on unseen data')}
</div>''',
 script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-auc'), F.hbars({min:.4,max:1,ticks:[.4,.5,.6,.7,.8,.9,1],ref:.5,refLabel:'0.5 = chance',noteW:160,
 rows:[{k:'IMAGE',v:.907,note:'Community Forensics'},{k:'FACE',v:.858,note:'KoDF · Korean faces'},{k:'VOICE',v:.988,note:'ASVspoof2019'}]}));
mount(document.getElementById('f-res'), w=>{
 const X=F.lin(0,5,10,w-10), r=['1080p','720p','480p',null,'360p','240p'], pos=[0,1,2,2.55,3.4,4.6];
 let s=`<line x1="${X(0)}" x2="${X(5)}" y1="40" y2="40" stroke="#C8C8C8"/>`;
 r.forEach((t,i)=>{ if(!t) return; s+=`<line x1="${X(pos[i])}" x2="${X(pos[i])}" y1="36" y2="44" stroke="#3A3A3A"/>`+F.T(X(pos[i]),28,t,{a:i?'middle':'start',fs:10.5,c:'#686868'}); });
 s+=`<line x1="${X(2.55)}" x2="${X(2.55)}" y1="8" y2="86" stroke="#141414" stroke-width="1.2"/>`+F.T(X(2.55),6,'Face 170px',{a:'middle',fs:11,b:true});
 s+=`<rect x="${X(0)}" y="58" width="${X(2.55)-X(0)-4}" height="5" fill="#141414"/>`+F.T(X(0),80,'CLIP · 480p and up',{fs:11});
 s+=`<rect x="${X(2.55)+4}" y="58" width="${X(5)-X(2.55)-4}" height="5" fill="#8C8C8C"/>`+F.T(X(2.55)+8,80,w<520?'XCEPTION':'XCEPTION · 360p and below · face under 170px',{fs:11});
 return F.svg(w,92,s);});
mount(document.getElementById('f-ood'), F.dotrows({min:.3,max:1,ticks:[.3,.5,.7,.9],ref:.5,refLabel:'0.5',rowH:26,inline:true,labelW:128,
 rows:[['CLIP last layer',.878],['CLIP multi · chosen',.834,1],['ConvNeXt-S',.831],['DINOv2-L',.821],['Xception',.796],['EfficientNet-B4',.754],['FFT baseline',.486],['UnivFD public',.398]]
 .map(([k,v,sel])=>({k,sel,sub:'',pts:[{v,t:v.toFixed(3),a:'start',dx:9,r:sel?5:3.5,c:sel?'#141414':'#8C8C8C'}]}))}));
mount(document.getElementById('f-fft'), F.dotrows({min:0,max:1,ticks:[0,.2,.4,.6,.8,1],band:[.45,.55],ref:.5,refLabel:'0.5 = chance',notes:true,rowH:88,
 rows:[{k:'01  BEFORE',sub:'Same code · 3 runs',range:true,note:'Different\\nevery run',pts:[{v:.015,t:'0.015'},{v:.5,t:'0.500',below:true},{v:.601,t:'0.601'}]},
       {k:'02  FIX 1',sub:'All saved as 384 JPEG',note:'Chance level',pts:[{v:.49,t:'OOD 0.490',a:'start',dx:9},{v:.46,t:'Ext. 0.460',a:'end',dx:-9,below:true}]},
       {k:'03  CUE LEFT',sub:'Ratio and size only',note:'→ retrain on\\nsquare crops',pts:[{v:.694,t:'0.694'}]}]}));
''')

PAGES['p02.html'] = dict(title='Predictive Maintenance', desc='Probabilistic remaining-life prediction for engines · maintenance timing',
 prev=('p01.html', 'P01 Deepfake Detection'), next=('p03.html', 'P03 Pill Finder'),
 body=top('P02', 'Main', 'Predictive Maintenance', 'Probabilistic engine life prediction · maintenance timing',
  [stag('GitHub', 'https://github.com/leebomin/jejuairline', '{GH}')],
  [('Period', '2026.06–07'), ('Team', 'Future Work Experience · Aerospace Industry-Academia Institute × Jeju Air · 4'), ('Role', 'Team lead · 1D-CNN ensemble · co-built conformal · report'), ('Model', '1D-CNN ensemble + conformal · likelihood-ratio Bayesian fusion')],
  award='Aero AI Track competition · Bronze · 2026.07') + f'''
<div class="body">
<p class="rv">Servicing too late causes faults; servicing too often costs money. I built a PoC that predicts an engine’s remaining useful life as a <b>probability distribution</b> rather than a single number, and uses that asymmetry to set the <b>maintenance time</b>. Data: 34 engines from N-CMAPSS (a NASA simulation) and 28,935 real flights from NGAFID.</p>
{fig([('Probability of failure before service', 'One cell = 1%', '<div class="waffles"><div><div data-cells="100,0,10,"></div><p class="w-l">Previous policy</p><p class="w-v dim">0.196</p></div><div><div data-cells="100,0,10,"></div><p class="w-l">After calibration</p><p class="w-v">0.119</p></div><p class="w-txt fig-note">Out of 100 maintenance decisions, failures before service fell from about 20 to 12.</p></div>')])}

{h2('What I did', '')}
<ol class="steps rv">
<li>Re-examined the evaluation and found that the expected 15–20% gain was <b>data leakage</b>.</li>
<li>Calibrated the 1D-CNN ensemble’s predictive distribution with conformal prediction; the 90% interval actually covered <b>0.902</b>.</li>
<li>Timed maintenance with the calibrated probabilities, lowering failure-before-service from <span class="hl">0.196 → 0.119</span>.</li>
</ol>
{fig([('90% prediction interval coverage', '', '<div id="f-cov"></div><p class="fig-note">90.2% of true remaining lives fell inside the predicted “90% interval”.</p>'),
      ('Policy simulation · 34 engines · reference only', 'One cell = one engine', rowfig('Mean-based', '34,34,34,f', '1 / 34').replace('data-cells="34,34,34,f"', 'id="e-a"') + rowfig('Probabilistic', '34,34,34,f', '0 / 34') + '<p class="fig-note">× = engine that failed before service. A one-engine gap, so not used as evidence on its own.</p>')])}

{h2('Key finding', 'Leakage')}
<h3 class="rv">Situation</h3>
<p class="rv">Adding an “LCC short-haul weight” improved RMSE by <b>15–20%</b>.</p>
<h3 class="rv">Doubt</h3>
<p class="rv">Teammates saw almost no gain on the same data; only my result looked much better. The scaler and feature selection were being <span class="hl">fit outside the cross-validation folds</span>, so test information leaked into training.</p>
<h3 class="rv">Check</h3>
<p class="rv">Moving preprocessing inside the folds made the effect vanish to <b>≈ 0</b>. I rejected the hypothesis and fixed <b>5 more bugs</b> with the same cause.</p>
{fig([('Before · preprocess first, split later', '', '<div class="flow"><div class="box"><span class="label">Data</span><p>All data<br><small>incl. test data</small></p></div><span class="arr">→</span><div class="box"><span class="label">Fit</span><p>Scaler · feature selection<br><small>on all data</small></p></div><span class="arr">→</span><div class="box"><span class="label">Split</span><p>Train / test</p></div></div>'),
      ('After · split first, preprocess on training data only', '', '<div class="flow"><div class="box"><span class="label">Split</span><p>Train / test</p></div><span class="arr">→</span><div class="box"><span class="label">Fit</span><p>Scaler · feature selection<br><small>on training data</small></p></div><span class="arr">→</span><div class="box"><span class="label">Apply</span><p>Only applied to test</p></div></div>'),
      ('RMSE improvement', '', '<div id="f-rmse"></div>')], 'The apparent 15–20% came from having already seen the test data.')}
{take('The better the number, the sooner to check its source')}

{h2('Data &amp; Experiment', 'Interval calibration · maintenance decision')}
{dl([('Data', 'N-CMAPSS 34 engines (NASA simulation) · NGAFID 28,935 real flights (diagnosis)'), ('Preproc', 'Scaler and feature selection fit only inside CV folds'), ('Unit', 'Engine-level CV · no engine in both train and test'), ('Decision', 'Maintenance time reflecting late (fault) vs early (cost) asymmetry')])}
{table(['Metric', 'Baseline', 'Final', 'How'], [
  ['Failure before service', '0.196', '0.119', 'Timing from calibrated distribution'],
  ['90% interval coverage', '—', '0.902', '1D-CNN ensemble + conformal'],
  ['Failures in policy sim', 'best: 1', '0 / 34', 'Mean-based → probabilistic policy'],
  ['Real-flight diagnosis AUC', '0.76', '0.849', 'Likelihood-ratio Bayesian fusion']], (1, 2))}
<p class="rv">Once RMSE hit the limit of the data size, bigger models no longer improved maintenance decisions. So I first made sure the 90% interval really covered 90%, then set maintenance timing from those probabilities.</p>
{take('Trustworthy intervals over bigger models')}
</div>''',
 script='''
const {mount}=PF, F=FIG;
const w=document.querySelectorAll('.waffles [data-cells]');
w[0].innerHTML=PF.cells(100,i=>i>=80?'g':'',10); w[1].innerHTML=PF.cells(100,i=>i>=88?'f':'',10);
document.getElementById('e-a').innerHTML=PF.cells(34,i=>i===23?'x':'f',34);
mount(document.getElementById('f-cov'), F.target({v:.902,t:.9,tl:'Target 90%',vt:'0.902'}));
mount(document.getElementById('f-rmse'), w=>{
 const X=F.lin(0,22,70,w-90); let s='';
 [0,5,10,15,20].forEach(t=>{s+=`<line x1="${X(t)}" x2="${X(t)}" y1="4" y2="76" stroke="#C8C8C8" stroke-width=".6"/>`+F.T(X(t),92,t+'%',{a:'middle',fs:10.5,c:'#686868'});});
 s+=F.T(0,24,'BEFORE',{fs:11,b:true})+`<rect x="${X(0)}" y="12" width="${X(15)-X(0)}" height="16" fill="#141414"/>`;
 for(let x=X(15);x<X(20);x+=4) s+=`<rect x="${x}" y="12" width="2" height="16" fill="#141414"/>`;
 s+=F.T(X(20)+8,25,'+15~20%',{disp:true,fs:15});
 s+=F.T(0,62,'AFTER',{fs:11,b:true})+`<rect x="${X(0)}" y="50" width="3" height="16" fill="#141414"/>`+F.T(X(0)+12,63,'≈ 0',{disp:true,fs:15});
 return F.svg(w,98,s);});
''')

PAGES['p03.html'] = dict(title='Pill Finder', desc='Pill Finder · LLM web app grounded in official documents',
 prev=('p02.html', 'P02 Predictive Maintenance'), next=('p04.html', 'P04 A/B Testing'),
 body=top('P03', 'Main', 'Pill Finder', 'LLM web app grounded in official documents',
  [stag('Demo', DEMO_P03), stag('GitHub', 'https://github.com/leebomin/pill-finder', '{GH}')],
  [('Period', '2026.11'), ('Team', 'Solo · NAVER Cloud Agentic AI course'), ('Role', 'Planning · model roles · app · MCP tools · evaluation design'), ('Model', 'HyperCLOVA X (answers) · Qwen3 4B (triage) · Claude API (review)')]) + f'''
<div class="body">
<p class="rv">A tool for people living alone to check leftover medicine. It finds pill candidates using only official sources and, for over-the-counter drugs only, gives a <b>plain-language summary</b> and answers questions. It never diagnoses or tells you what to take, and it is a demo awaiting review by medical professionals.</p>
{fig([('Pipeline', 'Start from what the model should not do', '<div class="flow"><div class="box"><span class="label">Question</span><p>Input</p></div><span class="arr">→</span><div class="box"><span class="label">Emergency</span><p>Code + Qwen3 4B</p></div><span class="arr">→</span><div class="box"><span class="label">Retrieve</span><p>MFDS source text</p></div><span class="arr">→</span><div class="box on"><span class="label">Answer</span><p>HyperCLOVA X</p></div><span class="arr">→</span><div class="box"><span class="label">Review</span><p>Claude API</p></div></div><div class="flow-sub"><span>Rules and search in code</span><span>LLM only for answers and review</span></div>')])}

{h2('What I did', '')}
<ol class="steps rv">
<li>Split the work: calculations and rules in code, answers by HyperCLOVA X, review by Claude API, deciding first <span class="hl">what the model should not do</span>.</li>
<li>Had Qwen3 4B re-check emergency questions the keyword list missed, raising detection from <b>3/20 → 20/20</b>.</li>
<li>Every answer shows its source passage or “not in official sources” (<b>20/20</b>), and personal data is blocked from leaving before confirmation (<b>9/10</b> masked).</li>
</ol>
{fig([('Safeguards', 'One cell = one case', rowfig('Citation', '20,20,20,f', '20 / 20', 'Source passage or “not in official sources” shown') + rowfig('PII mask', '10,9,10,f', '9 / 10', 'Sent out before confirmation: 0 / 10') + rowfig('Done', '19,17,19,f', '17 / 19', 'The other 2 need photo-recognition measurement'))])}

{h2('Key finding', 'Eval set · fixed first')}
<h3 class="rv">Situation</h3>
<p class="rv">A <b>keyword list</b> (“swallowed”, “all at once”) caught only <b>3/20</b> emergency questions.</p>
<h3 class="rv">Doubt</h3>
<p class="rv">Checking each rule change with questions I wrote myself risked an <b>illusion</b>: only questions shaped to fit the rules would pass.</p>
<h3 class="rv">Check</h3>
<p class="rv">I first fixed <span class="hl">40 new questions</span> written by an agent that had never seen the rules, and evaluated only on them. Adding Qwen3 4B triage gave <b>20/20</b>, <b>0</b> extra false alarms in the set, and about <b>0.4 s</b> per response.</p>
{fig([('Eval set', 'Fix the test first', '<div class="flow"><div class="box"><span class="label">Step 1</span><p>Fix 40 questions first<br><small>written by an agent blind to the rules</small></p></div><span class="arr">→</span><div class="box"><span class="label">Step 2</span><p>Change rules · model</p></div><span class="arr">→</span><div class="box"><span class="label">Step 3</span><p>Re-measure on the same 40</p></div></div><div class="flow-sub"><span></span><span>↺ repeat 2 → 3 · the test never changes</span></div>'),
      ('Result', 'Same 40 only · one cell = one question', rowfig('Keyword list', '20,3,20,f', '3 / 20') + rowfig('+ Qwen3 4B', '20,20,20,f', '20 / 20', '0 extra false alarms in the set · about 0.4 s') + rowfig('Limit', '20,2,20,g', '2 / 20', 'Hypothetical questions still trigger the 119 notice · unresolved'))])}
{take('Emergency detection 3/20 → 20/20')}
</div>''', script=' ')

PAGES['p04.html'] = dict(title='A/B Testing', desc='Lodging app conversion A/B test · decision rule fixed in advance',
 prev=('p03.html', 'P03 Pill Finder'), next=('more.html', 'P05–08'),
 body=top('P04', 'Main', 'A/B Testing', 'Lodging app conversion A/B test · rule fixed in advance',
  [stag('GitHub', 'https://github.com/leebomin/tobigs-26th', '{GH}')],
  [('Period', '2026.10'), ('Team', "TOBIG'S DA track · individual assignment"), ('Role', 'Experiment design · decision rule · full analysis'), ('Method', 'User-level assignment · delta method · SRM test · MDE')]) + f'''
<div class="body">
<p class="rv">The analytics team had diagnosed a <b>gap of about 10.7%p</b> in list → detail conversion for the promotion channel. I tested a fix (showing the discounted price on list cards) and designed and judged the experiment by <b>rules set before seeing the results</b>.</p>
{fig([('Gap', 'Share of the observed gap confirmed by the experiment · %p', '<div id="f-gap"></div>'), ('Effect', 'List → detail conversion · 95% CI · %p', '<div id="f-ci"></div>')], 'The whole interval is above 0, so the effect was judged real (p = 0.0026). Revenue impact was not tested here.')}

{h2('What I did', '')}
<ol class="steps rv">
<li>Assigned by <b>user</b> and corrected the variance with the delta method. With a design effect of <b>1.59 → 2.11</b>, set MDE 3%p and a <b>21-day</b> duration.</li>
<li>Checked the split (SRM p = 0.71, 3,446 vs 3,415 users) and split the analysis around a <b>day-8 ad campaign</b>, treating the post-ad period as exploratory only.</li>
<li>List → detail conversion <span class="hl">+2.75%p</span> (95% CI 0.96–4.54), no significant guardrail harm → recommended a <b>staged rollout</b>.</li>
</ol>

{h2('Key finding', 'Peeking')}
<h3 class="rv">Situation</h3>
<p class="rv">On the same data I compared a <b>fixed 21-day decision</b> with <b>checking daily and stopping</b>.</p>
<h3 class="rv">Doubt</h3>
<p class="rv">Watching p-values daily can end the test on a lucky low day, or <b>drop a launch</b> even when the effect is real.</p>
<h3 class="rv">Check</h3>
<p class="rv">Stopping on day 12 gave user-level p = <b>0.084</b>, meaning no launch; the <span class="hl">fixed 21-day decision</span> gave p = <b>0.0026</b>, +2.75%p.</p>
{fig([('Timeline', '21 days · one cell = one day', '<div id="f-days"></div>'),
      ('Decision', 'Same data · different rules', '<div class="cards2"><div class="c"><span class="label">D12 · Peek</span><p class="p">p = 0.084</p><small>Not significant at user level → no launch</small></div><div class="c"><span class="label">D21 · Fixed</span><p class="p">p = 0.0026</p><small>+2.75%p · no significant guardrail harm → staged rollout</small></div></div>'),
      ('p-value', 'Log scale · 0.05 line', '<div id="f-logp"></div>')], 'The post-ad period from day 8 was analysed separately and read as exploratory only.')}
<p class="rv">Of the 10.7%p observed gap, the experiment confirmed 2.75%p. I did not pin the observed gap on a single cause, and fixed the decision rule and unit of analysis before seeing results.</p>
{take('Decision rules come before results')}
</div>''',
 script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-gap'), w=>{
 const X=F.lin(0,10.7,4,w-92); let s='';
 s+=`<rect x="${X(0)}" y="14" width="${X(10.7)-X(0)}" height="22" fill="none" stroke="#141414"/>`;
 s+=`<rect x="${X(0)}" y="14" width="${X(2.75)-X(0)}" height="22" fill="#1F32A8"/>`;
 s+=F.T(X(10.7)+8,30,'10.7',{disp:true,fs:16})+F.T(X(10.7)+8,46,'Observed gap',{fs:10.5,c:'#686868'});
 [0,2,4,6,8,10].forEach(t=>s+=F.T(X(t),56,t,{a:'middle',fs:10.5,c:'#686868'}));
 s+=F.T(X(0),76,'+2.75 · confirmed by experiment',{fs:11.5,b:true,c:'#1F32A8'});
 return F.svg(w,82,s);});
mount(document.getElementById('f-ci'), F.ci({min:0,max:6,lo:.96,hi:4.54,est:2.75,mde:3,zeroLabel:'No effect'}));
mount(document.getElementById('f-days'), F.days({n:21,peek:12,ad:8,lab:[1,5,8,12,17,21]}));
mount(document.getElementById('f-logp'), F.logp({min:.001,max:1,ticks:[.001,.01,.05,.1,1],alpha:.05,pts:[{v:.0026,t:'D21'},{v:.084,t:'D12'}]}));
''')

def short(code, id_, title, sub, meta, figs, found, limit, gh=None):
    links = stag('GitHub', f'https://github.com/{gh}', '{GH}') if gh else ''
    return f'''<section class="sec" id="{id_}" style="padding-top:56px">
<div class="crumb label rv"><span>{code} · Short</span><span>/</span><span class="ko-t">{meta}</span></div>
<h2 class="ptitle rv" style="font-size:24px">{title}</h2><p class="psub rv">{sub}</p>
{'<div class="small-tags rv">' + links + '</div>' if links else ''}
<div class="body" style="margin-top:12px">{figs}
<h3 class="rv">Finding</h3><p class="rv">{found}</p>
<h3 class="rv">Limits</h3><p class="rv">{limit}</p></div>
</section>'''

PAGES['more.html'] = dict(title='P05–08', desc='Olist SQL · university decline · local extinction index · vacant-house regression diagnostics',
 prev=('p04.html', 'P04 A/B Testing'), next=('p01.html', 'P01 Deepfake Detection'),
 body='''<div class="crumb label rv"><a href="../projects.html">Projects</a><span>/</span><span>P05–08 · Short</span></div>
<h1 class="ptitle rv">Short projects</h1>''' +
 short('P05', 'p05', 'Join Fan-out', 'Olist e-commerce SQL analysis', "TOBIG'S SQL assignment · MySQL 8.0",
   fig([('A JOIN that turns one order into many rows', 'Orders → Items × Payments · example', '<div id="f-fan"></div>'), ('Over-count', '', '<div id="f-over"></div>')]),
   'The query ran without errors, yet one JOIN over-counted payments by <span class="hl">28.23%</span> (item sales by 4.48%). I compared row counts with distinct order counts for each table and <b>aggregated to order level first</b> for tables that attach several rows per order.',
   'Whether the −26.5% December revenue was a slump or a hangover from November promotions could not be checked without prior-year or traffic data.', gh='leebomin/tobigs-26th') +
 short('P06', 'p06', 'Effect Size', 'Decline of universities outside the capital region', 'Urban Research Methods · team of 5 · data analysis · R · 2023.03–06',
   fig([('Mean admission percentile (GS)', 'Lower = more preferred', '<div id="f-gs"></div>'), ('Preference ~ youth net migration', '81 districts · one cell = 1%', '<div class="waffles" style="grid-template-columns:140px 1fr"><div data-cells="100,11,10,f"></div><div><p class="w-v">R² ≈ 0.11</p><p class="fig-note">Only 11 cells are explained.</p></div></div>')]),
   'The percentile gap was clear (capital region 24.0 vs elsewhere 52.5, Welch p&lt;0.001), but it explained only <b>11%</b> of youth net migration. I reported significance and explanatory power separately.',
   'A correlational analysis of 2 years and 81 samples, so it cannot support causal claims.') +
 short('P07', 'p07', 'Definition Bias', 'Multivariate analysis of the local extinction index', 'Multivariate Statistics · solo · SAS · 2024.09–12',
   fig([('Scree · 9 components', 'Eigenvalues · one cell = 0.2', '<div id="f-scree"></div>'), ('Two variables sharing a formula', 'r = −0.908', '<div class="cards2"><div class="c"><small>Elderly living alone rate = <b>elderly alone</b> / <b>65+</b></small></div><div class="c"><small>Extinction index = <b>women 20–39</b> / <b>65+</b></small></div></div>')]),
   'Ran regression, PCA, factor analysis, LDA and MANOVA on 229 districts and 9 variables. Cutting variables from 9 to 5 kept adj R² at <b>0.857</b>, and four components explained <b>85.3%</b>.',
   'The elderly-alone rate and the response share a denominator (age 65+), so much of the −0.908 correlation may come from the formula itself.') +
 short('P08', 'p08', 'Influence', 'Regression diagnostics for vacant-house rates', 'Regression Analysis I · solo · SAS · 2024.03–06',
   fig([("Cook’s D", '261 districts · sorted · ■ = 12 above 4/n', '<div data-cells="261,12,29,f"></div>'), ('adj R²', 'With / without influential points', '<div id="f-r2"></div>')]),
   'All-subsets and stepwise selection chose the same 4 variables, adj R² <b>0.587</b>. Dropping 12 influential points moved it to 0.633, which I reported as <b>a measure of instability</b>, not a better model.',
   'The old-housing coefficient has the opposite sign from its simple correlation (+0.33), due to information shared with other variables, so I did not read it causally.'),
 script='''
const {mount}=PF, F=FIG;
mount(document.getElementById('f-fan'), F.fanout({}));
mount(document.getElementById('f-over'), F.hbars({min:0,max:32,ticks:[0,10,20,30],noteW:80,labelW:80,rows:[{k:'Payments',v:28.23,vt:'+28.23%'},{k:'Item sales',v:4.48,vt:'+4.48%',c:'#8C8C8C'}]}));
mount(document.getElementById('f-gs'), F.dotrows({min:0,max:70,ticks:[0,10,20,30,40,50,60,70],tf:0,rowH:58,rows:[{k:'Capital',sub:'',pts:[{v:24,t:'24.0'}]},{k:'Elsewhere',sub:'Δ 28.5 · p<0.001',pts:[{v:52.5,t:'52.5'}]}]}));
mount(document.getElementById('f-scree'), F.scree({ev:[5.28,1.22,.67,.49,.47,.38,.27,.17,.02],k:4,cum:'85.3%'}));
mount(document.getElementById('f-r2'), F.hbars({min:0,max:.8,ticks:[0,.2,.4,.6,.8],noteW:110,labelW:80,rows:[{k:'All',v:.587,vt:'0.587'},{k:'Without 12',v:.633,vt:'0.633',c:'#BABABA',note:'12 removed'}]}));
''')
