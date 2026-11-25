/* figures drawn from the real numbers; each builder returns an SVG string for a given width */
(() => {
  const INK = '#141414', INK2 = '#3A3A3A', MUTE = '#686868', LINE = '#C8C8C8', CELL = '#BABABA', ACC = '#1F32A8', PAPER = '#FFFFFF';
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const EN = document.documentElement.lang === 'en', TR = (k, e) => EN ? e : k;
  const KO = /[\uAC00-\uD7A3]/;
  const T = (x, y, s, o = {}) => (o.ko === undefined && KO.test(s) && (o = { ...o, ko: true }), 0) || `<text x="${x}" y="${y}" font-size="${o.fs || 11}" ${o.a ? `text-anchor="${o.a}"` : ''} ${o.cls ? `class="${o.cls}"` : ''} style="${o.ko ? "font-family:'Gothic A1',sans-serif;font-weight:500;" : ''}${o.disp ? 'font-family:Inter Tight,sans-serif;font-weight:600;' : ''}${o.b ? 'font-weight:700;' : ''}fill:${o.c || INK};letter-spacing:${o.ls ?? 0.02}em">${esc(s)}</text>`;
  const svg = (w, h, inner) => `<svg class="svgfig" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">${inner}</svg>`;
  const lin = (min, max, a, b) => v => a + (v - min) / (max - min) * (b - a);
  const narrow = w => w < 520;

  /* horizontal bars with a reference line */
  function hbars(o) {
    return w => {
      const n = narrow(w), L = o.labelW ?? (n ? 58 : 72), right = n ? 64 : (o.noteW ?? 220);
      const rowH = n ? 46 : 38, top = 26, H = top + o.rows.length * rowH + 26;
      const X = lin(o.min, o.max, L, w - right);
      let s = '';
      o.ticks.forEach(t => { s += `<line x1="${X(t)}" x2="${X(t)}" y1="${top - 6}" y2="${H - 22}" stroke="${LINE}" stroke-width=".6"/>` + T(X(t), H - 6, t, { a: 'middle', c: MUTE, fs: 10.5 }); });
      if (o.ref != null) s += `<line x1="${X(o.ref)}" x2="${X(o.ref)}" y1="${top - 12}" y2="${H - 22}" stroke="${INK}" stroke-dasharray="3 3"/>` + T(X(o.ref), top - 16, o.refLabel, { a: 'middle', fs: 10.5, ko: true });
      o.rows.forEach((r, i) => {
        const y = top + i * rowH + 6;
        s += T(0, y + 12, r.k, { fs: n ? 10 : 11 });
        const x0 = X(o.base ?? o.min), x1 = X(r.v);
        s += `<rect x="${x0}" y="${y}" width="${Math.max(1.5, x1 - x0)}" height="16" fill="${r.c || INK}"/>`;
        s += T(x1 + 8, y + 14, r.vt ?? r.v, { disp: true, fs: n ? 15 : 18, c: r.vc || INK });
        if (r.note) s += n ? T(L, y + 32, r.note, { fs: 10, c: MUTE, ko: true }) : T(x1 + 8 + (String(r.vt ?? r.v).length * 10.5) + 10, y + 13, r.note, { fs: 11, c: MUTE, ko: true });
      });
      return svg(w, H, s);
    };
  }

  /* dot rows on a shared axis */
  function dotrows(o) {
    return w => {
      const n = narrow(w), L = o.inline ? (o.labelW || 120) : n ? 0 : 150, right = (!n && o.notes) ? 90 : 16;
      const rowH = o.rowH || 78, top = 34, H = top + o.rows.length * rowH + 28;
      const X = lin(o.min, o.max, L + 12, w - right);
      let s = '';
      if (o.band) s += `<rect x="${X(o.band[0])}" y="${top - 8}" width="${X(o.band[1]) - X(o.band[0])}" height="${H - top - 22}" fill="${LINE}" opacity=".55"/>`;
      o.ticks.forEach(t => { s += `<line x1="${X(t)}" x2="${X(t)}" y1="${top - 8}" y2="${H - 22}" stroke="${LINE}" stroke-width=".6"/>` + T(X(t), H - 6, t.toFixed(o.tf ?? 1), { a: 'middle', c: MUTE, fs: 10.5 }); });
      if (o.ref != null) s += `<line x1="${X(o.ref)}" x2="${X(o.ref)}" y1="${top - 12}" y2="${H - 22}" stroke="${INK}" stroke-dasharray="2 3"/>` + T(X(o.ref), top - 16, o.refLabel, { a: 'middle', fs: 10.5, ko: true });
      o.rows.forEach((r, i) => {
        const yc = top + i * rowH + rowH / 2 - (o.inline ? 0 : n ? -14 : 4);
        if (o.inline) { s += T(n ? 0 : 0, yc + 4, r.k, { fs: 11, b: !!r.sel, c: r.sel ? INK : INK2, ko: true }); }
        else if (n) { s += T(0, yc - 40, r.k, { fs: 10.5, b: true }) + T(0, yc - 27, r.sub || '', { fs: 10, c: MUTE, ko: true }); }
        else { s += T(0, yc - 2, r.k, { fs: 11, b: true }) + T(0, yc + 14, r.sub || '', { fs: 10.5, c: MUTE, ko: true }); }
        if (i > 0 && !o.inline) s += `<line x1="0" x2="${w}" y1="${top + i * rowH - 4}" y2="${top + i * rowH - 4}" stroke="${LINE}" stroke-width=".6"/>`;
        const vs = r.pts.map(p => p.v);
        if (r.range && vs.length > 1) s += `<line x1="${X(Math.min(...vs))}" x2="${X(Math.max(...vs))}" y1="${yc}" y2="${yc}" stroke="${INK2}" stroke-width="1.2"/>`;
        r.pts.forEach(p => {
          s += `<circle cx="${X(p.v)}" cy="${yc}" r="${p.r || 5}" fill="${p.c || INK}"/>`;
          const dy = o.inline ? 4 : p.below ? 20 : -11;
          s += T(X(p.v) + (p.dx || 0), yc + dy, p.t ?? p.v, { a: p.a || 'middle', disp: true, fs: n ? 12 : 14, c: p.c || INK });
        });
        if (!n && o.notes && r.note) r.note.split('\n').forEach((ln, j) => { s += T(w, yc - 4 + j * 15, ln, { a: 'end', fs: 11, ko: true, c: INK2 }); });
      });
      return svg(w, H, s);
    };
  }

  /* simple numeric bar with a target line (coverage) */
  function target(o) {
    return w => {
      const n = narrow(w), vw = n ? 70 : 110, X = lin(0, 1, 0, w - vw - 16), H = 70, y = 22;
      let s = `<rect x="0" y="${y}" width="${X(1)}" height="14" fill="${LINE}"/><rect x="0" y="${y}" width="${X(o.v)}" height="14" fill="${INK2}"/>`;
      s += `<line x1="${X(o.t)}" x2="${X(o.t)}" y1="${y - 10}" y2="${y + 22}" stroke="${INK}" stroke-width="1.2"/>` + T(X(o.t), y - 13, o.tl, { a: 'middle', fs: 10.5, ko: true });
      s += T(0, y + 36, '0%', { fs: 10, c: MUTE }) + T(X(1), y + 36, '100%', { a: 'end', fs: 10, c: MUTE });
      s += T(w, y + 14, o.vt, { a: 'end', disp: true, fs: n ? 22 : 28 });
      return svg(w, H, s);
    };
  }

  /* confidence interval on an axis */
  function ci(o) {
    return w => {
      const H = 118, y = 64, X = lin(o.min, o.max, 14, w - 14);
      let s = `<line x1="${X(o.min)}" x2="${X(o.max)}" y1="${y + 18}" y2="${y + 18}" stroke="${INK2}" stroke-width=".8"/>`;
      for (let t = o.min; t <= o.max; t++) s += `<line x1="${X(t)}" x2="${X(t)}" y1="${y + 14}" y2="${y + 22}" stroke="${INK2}"/>` + T(X(t), y + 38, t, { a: 'middle', fs: 10.5, c: MUTE });
      s += `<line x1="${X(0)}" x2="${X(0)}" y1="${y - 46}" y2="${y + 18}" stroke="${MUTE}" stroke-width="1.5"/>` + T(X(0) + 6, y - 38, o.zeroLabel, { fs: 10.5, ko: true, c: MUTE });
      if (o.mde != null) s += `<line x1="${X(o.mde)}" x2="${X(o.mde)}" y1="${y - 30}" y2="${y + 18}" stroke="${INK}" stroke-dasharray="2 3"/>` + T(X(o.mde) + 5, y - 22, `MDE ${o.mde}`, { fs: 10.5 });
      s += `<line x1="${X(o.lo)}" x2="${X(o.hi)}" y1="${y}" y2="${y}" stroke="${INK}" stroke-width="3"/>`;
      s += `<line x1="${X(o.lo)}" x2="${X(o.lo)}" y1="${y - 6}" y2="${y + 6}" stroke="${INK}" stroke-width="1.5"/><line x1="${X(o.hi)}" x2="${X(o.hi)}" y1="${y - 6}" y2="${y + 6}" stroke="${INK}" stroke-width="1.5"/>`;
      s += T(X(o.lo), y - 12, o.lo, { a: 'middle', fs: 11 }) + T(X(o.hi), y - 12, o.hi, { a: 'middle', fs: 11 });
      s += `<rect x="${X(o.est) - 6}" y="${y - 6}" width="12" height="12" fill="${ACC}"/>` + T(X(o.est), y - 14, `+${o.est}`, { a: 'middle', disp: true, fs: 15, c: ACC });
      return svg(w, H, s);
    };
  }

  /* p-values on a log axis */
  function logp(o) {
    return w => {
      const H = 96, y = 50, lg = Math.log10, X = v => 16 + (lg(v) - lg(o.min)) / (lg(o.max) - lg(o.min)) * (w - 32);
      let s = `<line x1="${X(o.min)}" x2="${X(o.max)}" y1="${y}" y2="${y}" stroke="${INK2}" stroke-width=".8"/>`;
      o.ticks.forEach(t => { s += `<line x1="${X(t)}" x2="${X(t)}" y1="${y - 4}" y2="${y + 4}" stroke="${INK2}"/>` + T(X(t), y + 22, t, { a: 'middle', fs: 10.5, c: t === o.alpha ? INK : MUTE, b: t === o.alpha }); });
      s += `<line x1="${X(o.alpha)}" x2="${X(o.alpha)}" y1="${y - 36}" y2="${y + 8}" stroke="${INK}" stroke-dasharray="2 3"/>` + T(X(o.alpha) - 6, y - 28, TR('← 유의', '← significant'), { a: 'end', fs: 10.5, ko: true });
      o.pts.forEach(p => { s += `<rect x="${X(p.v) - 5}" y="${y - 5}" width="10" height="10" fill="${p.c || INK}"/>` + T(X(p.v), y - 14, p.t, { a: 'middle', fs: 10.5, c: p.c || INK }); });
      return svg(w, H, s);
    };
  }

  /* 21-day timeline, one cell = one day */
  function days(o) {
    return w => {
      const n = o.n, gap = 3, cw = (w - gap * (n - 1)) / n, y = 34, H = y + cw + 44;
      let s = '';
      for (let i = 0; i < n; i++) {
        const x = i * (cw + gap), seen = i < o.peek;
        s += `<rect x="${x + .5}" y="${y + .5}" width="${cw - 1}" height="${cw - 1}" fill="${seen ? CELL : 'none'}" stroke="${seen ? '#8C8C8C' : '#8C8C8C'}" stroke-width=".8"/>`;
        if (o.lab.includes(i + 1)) s += T(x, y + cw + 16, 'D' + (i + 1), { fs: w < 520 ? 8.5 : 10.5, c: MUTE });
      }
      const xa = (o.ad - 1) * (cw + gap) + cw / 2;
      s += T(xa, y - 8, TR('광고', 'ad'), { a: 'middle', fs: 10.5, ko: true });
      const xp = o.peek * (cw + gap) - gap / 2;
      s += `<line x1="${xp}" x2="${xp}" y1="${y - 26}" y2="${y + cw + 4}" stroke="${INK}" stroke-width="1.4"/>` + T(xp + 5, y - 16, TR('PEEK · 중단', 'PEEK · stop'), { fs: 10.5, ko: true, b: true });
      const xf = w - .7;
      s += `<line x1="${xf}" x2="${xf}" y1="${y - 26}" y2="${y + cw + 22}" stroke="${INK}" stroke-width="1.4"/>` + T(xf, y + cw + 36, TR('FIXED · 판정', 'FIXED · decide'), { a: 'end', fs: 10.5, ko: true, b: true });
      return svg(w, H, s);
    };
  }

  /* scree plot, bars stacked from cells (one cell = 0.2 eigenvalue) */
  function scree(o) {
    return w => {
      const n = o.ev.length, L = 26, B = 24, H = 250, ch = 6, unit = 0.2;
      const bw = (w - L) / n, top = 34;
      const Y = v => H - B - v / unit * ch;
      let s = '';
      [0, 1, 2, 3, 4, 5].forEach(t => { s += `<line x1="${L}" x2="${w}" y1="${Y(t)}" y2="${Y(t)}" stroke="${LINE}" stroke-width=".5"/>` + T(L - 6, Y(t) + 3.5, t, { a: 'end', fs: 10, c: MUTE }); });
      o.ev.forEach((v, i) => {
        const k = Math.round(v / unit), x = L + i * bw + bw * 0.18, cwid = bw * 0.64, on = i < o.k;
        for (let j = 0; j < k; j++) s += `<rect x="${x}" y="${H - B - (j + 1) * ch + 1}" width="${cwid}" height="${ch - 1.2}" fill="${on ? INK : CELL}"/>`;
        if (k === 0) s += `<rect x="${x}" y="${H - B - 1.5}" width="${cwid}" height="1.5" fill="${CELL}"/>`;
        s += T(x + cwid / 2, Y(v) - 6, v.toFixed(2), { a: 'middle', fs: 9.5, c: on ? INK : MUTE });
        s += T(x + cwid / 2, H - 6, 'PC' + (i + 1), { a: 'middle', fs: w < 520 ? 8.5 : 10, c: on ? INK : MUTE });
      });
      const xk = L + o.k * bw;
      s += `<line x1="${xk}" x2="${xk}" y1="${top - 20}" y2="${H - B}" stroke="${INK}" stroke-dasharray="2 3"/>` + T(xk + 6, top - 8, TR(`PC1–${o.k} 누적 ${o.cum}`, `PC1–${o.k} cumulative ${o.cum}`), { fs: 11, ko: true, b: true });
      return svg(w, H, s);
    };
  }

  /* JOIN fan-out schematic: 12 orders become 16 rows */
  function fanout(o) {
    return w => {
      const n = narrow(w), rows = 16, ord = 12, rh = 13, top = 26, H = top + rows * rh + 10;
      const cols = n ? 6 : 9, cw = n ? 7 : 9, colW = cols * (cw + 1.5);
      const xr = w - colW - 4;
      const map = [0, 1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9, 10, 11]; /* order index for each joined row */
      const dup = new Set(map.filter((v, i) => map.indexOf(v) !== i || map.lastIndexOf(v) !== i));
      let s = T(0, 12, `ORDER (${ord})`, { fs: 10.5, b: true }) + T(xr, 12, `AFTER JOIN (${rows})`, { fs: 10.5, b: true });
      const cellRow = (x, y, k, fillN) => { let r = ''; for (let c = 0; c < k; c++) r += `<rect x="${x + c * (cw + 1.5)}" y="${y}" width="${cw}" height="${rh - 4}" fill="${c < fillN ? INK : CELL}"/>`; return r; };
      for (let i = 0; i < ord; i++) { const y = top + (i * rows / ord) * rh; s += cellRow(0, y, cols, 2); }
      map.forEach((oi, j) => {
        const y = top + j * rh, d = dup.has(oi);
        const yo = top + (oi * rows / ord) * rh + (rh - 4) / 2;
        s += `<line x1="${colW + 2}" y1="${yo}" x2="${xr - 4}" y2="${y + (rh - 4) / 2}" stroke="${d ? INK : LINE}" stroke-width="${d ? 1 : .7}"/>`;
        s += cellRow(xr, y, cols, d ? cols : 2);
      });
      return svg(w, H, s);
    };
  }

  window.FIG = { hbars, dotrows, target, ci, logp, days, scree, fanout, svg, T, lin };
})();
