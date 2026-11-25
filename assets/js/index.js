(() => {
  const { band, pixelPortrait, rng, gauss } = window.PF;

  band(document.getElementById('band'), {
    seed: 11,
    labels: [
      { x: 0.20, y: 0.56, w: 0.12, h: 0.16, t: '(1) outlier?' },
      { x: 0.47, y: 0.38, w: 0.13, h: 0.18, t: '(2) leakage' },
      { x: 0.79, y: 0.28, w: 0.16, h: 0.22, t: '(3) signal' },
    ],
  });
  band(document.getElementById('band2'), { seed: 23, reverse: true, boxes: false, blues: 4, spread: 2, full: true, static: true, max: 26 });

  pixelPortrait(document.getElementById('pxPortrait'), 'assets/img/portrait.png');
  pixelPortrait(document.getElementById('pxCard'), 'assets/img/portrait.png');

  /* ───────── project network (coordinates follow the INDEX slide) ───────── */
  const P = [
    { n: 1, x: 1174, y: 194, s: 130, t: 'DEEPFAKE DETECTION', v: '0.907', d: '외부 데이터 AUC', g: 34, acc: true, href: 'works/p01.html' },
    { n: 2, x: 1574, y: 144, s: 130, t: 'PREDICTIVE MAINTENANCE', v: '0.119', d: '정비 전 고장 확률', g: 30, href: 'works/p02.html' },
    { n: 3, x: 1574, y: 504, s: 130, t: 'PILL FINDER', v: '20/20', d: '응급 질문 감지', g: 24, href: 'works/p03.html' },
    { n: 4, x: 1174, y: 584, s: 130, t: 'A/B TESTING', v: '+2.75%p', d: '상세 전환율 상승', g: 14, href: 'works/p04.html' },
    { n: 5, x: 814, y: 374, s: 106, t: 'JOIN FAN-OUT', v: '28.23%', d: '결제금액 과대 집계', g: 16, href: 'works/more.html#p05' },
    { n: 6, x: 854, y: 714, s: 106, t: 'EFFECT SIZE', v: 'R² 0.11', d: '청년 순이동 설명력', g: 12, href: 'works/more.html#p06' },
    { n: 7, x: 1294, y: 804, s: 106, t: 'DEFINITION BIAS', v: '0.857', d: '변수 5개 모델 adj R²', g: 9, href: 'works/more.html#p07' },
    { n: 8, x: 1634, y: 804, s: 106, t: 'INFLUENCE', v: '0.587', d: '회귀 모델 adj R²', g: 7, href: 'works/more.html#p08' },
  ];
  const E = [[1, 2, 'BOOTSTRAP CI'], [1, 3, 'EVAL SET'], [1, 4, 'PRE-REG'], [5, 4, 'SRM'], [5, 6, 'GROUPING'], [2, 7, 'BAYES'], [4, 3, 'GUARDRAIL'], [6, 7, 'T-TEST'], [7, 8, 'VIF']];
  const svg = document.getElementById('net');
  const c = p => [p.x + p.s / 2, p.y + p.s / 2];
  let h = '';
  E.forEach(([a, b], i) => {
    const A = c(P[a - 1]), B = c(P[b - 1]);
    h += `<line class="edge" data-a="${a}" data-b="${b}" x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}"/>`;
  });
  E.forEach(([a, b, t]) => {
    const A = c(P[a - 1]), B = c(P[b - 1]), mx = (A[0] + B[0]) / 2, my = (A[1] + B[1]) / 2, w = t.length * 9.6 + 16;
    h += `<g class="m"><rect x="${mx - w / 2}" y="${my - 12}" width="${w}" height="24"/><text x="${mx}" y="${my + 5}" font-size="14" text-anchor="middle">${t}</text></g>`;
  });
  P.forEach(p => {
    const R = rng(p.n * 97), g = p.g, cs = (p.s - 12) / g;
    let px = '';
    for (let j = 0; j < g; j++) for (let i = 0; i < g; i++) {
      const dx = (i + .5) / g - .5, dy = (j + .5) / g - .5, r2 = dx * dx + dy * dy;
      const pr = Math.exp(-r2 / 0.06) * 0.95 + gauss(R) * 0.08;
      if (R() > pr) continue;
      const v = Math.max(0, Math.min(1, pr + (R() - 0.5) * 0.5));
      const col = v > 0.7 ? '#141414' : v > 0.45 ? '#4A4A47' : v > 0.25 ? '#8C8C86' : '#C6C6C0';
      const gap = g > 20 ? 0.6 : 1.2;
      px += `<rect x="${(p.x + 6 + i * cs).toFixed(1)}" y="${(p.y + 6 + j * cs).toFixed(1)}" width="${(cs - gap).toFixed(1)}" height="${(cs - gap).toFixed(1)}" fill="${col}"/>`;
    }
    const lab = `(${String(p.n).padStart(2, '0')}) ${p.t}`;
    h += `<a href="${p.href}"><g class="node" data-p="${p.n}">
      <rect x="${p.x}" y="${p.y}" width="${p.s}" height="${p.s}" fill="#ECECE8"/>${px}
      <rect class="frame" x="${p.x}" y="${p.y}" width="${p.s}" height="${p.s}" ${p.acc ? 'style="stroke:var(--accent)"' : ''}/>
      <text x="${p.x}" y="${p.y + p.s + 22}" font-size="14" ${p.acc ? 'style="fill:var(--accent)"' : ''}>${lab}</text>
      <text x="${p.x}" y="${p.y + p.s + 52}" font-size="27" style="font-family:Inter,sans-serif;font-weight:600">${p.v}</text>
      <text x="${p.x + p.v.length * 17 + 14}" y="${p.y + p.s + 50}" font-size="12" style="font-family:'Gothic A1',sans-serif;fill:var(--mute)">${p.d}</text>
    </g></a>`;
  });
  svg.innerHTML = h;

  /* sync hover between list and map */
  const hot = (n, on) => {
    document.querySelectorAll(`#tracks a[data-p="${n}"]`).forEach(a => a.classList.toggle('hot', on));
    svg.querySelectorAll(`.node[data-p="${n}"]`).forEach(g => g.classList.toggle('hot', on));
    svg.querySelectorAll('.edge').forEach(l => { if (l.dataset.a == n || l.dataset.b == n) l.classList.toggle('hot', on); });
  };
  document.querySelectorAll('#tracks a').forEach(a => {
    a.addEventListener('mouseenter', () => hot(a.dataset.p, true));
    a.addEventListener('mouseleave', () => hot(a.dataset.p, false));
  });
  svg.querySelectorAll('.node').forEach(g => {
    g.addEventListener('mouseenter', () => hot(g.dataset.p, true));
    g.addEventListener('mouseleave', () => hot(g.dataset.p, false));
  });

  /* ───────── skills matrix ───────── */
  const cols = ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'CareerFit'];
  const rows = [
    ['Python', 'pandas · sklearn · PyTorch', [2, 2, 2, 2, 1, 0, 0, 0, 2]],
    ['SQL', 'MySQL · SQLite', [0, 0, 1, 0, 2, 0, 0, 0, 1]],
    ['R · SAS', 'R · SAS · Jamovi', [0, 0, 0, 0, 0, 2, 2, 2, 0]],
    ['통계 검정 · 회귀', 't-test · 회귀 · VIF', [1, 1, 0, 2, 0, 2, 2, 2, 0]],
    ['실험 설계', 'SRM · MDE · CI', [1, 0, 1, 2, 0, 0, 0, 0, 0]],
    ['ML · DL', 'CLIP · 1D-CNN', [2, 2, 0, 0, 0, 0, 1, 0, 0]],
    ['LLM · RAG', 'RAG · MCP · ChromaDB · Ollama', [0, 0, 2, 0, 0, 0, 0, 0, 2]],
  ];
  const links = ['works/p01.html', 'works/p02.html', 'works/p03.html', 'works/p04.html', 'works/more.html#p05', 'works/more.html#p06', 'works/more.html#p07', 'works/more.html#p08'];
  const sym = ['–', '○', '●'];
  document.getElementById('matrix').innerHTML =
    `<thead><tr><th></th><th></th>${cols.map((c, i) => `<th class="${i === 8 ? 'cf' : ''}">${i < 8 ? `<a class="chip" href="${links[i]}">${c}</a>` : `<span class="chip">${c}</span>`}</th>`).join('')}</tr></thead>` +
    `<tbody>${rows.map(r => `<tr><td>${r[0]}</td><td class="tools">${r[1]}</td>${r[2].map(v => `<td><span class="d ${v ? '' : 'z'}">${sym[v]}</span></td>`).join('')}</tr>`).join('')}</tbody>`;
})();
