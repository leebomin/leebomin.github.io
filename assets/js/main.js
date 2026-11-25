/* LEE BOMIN — portfolio · shared behaviour */
(() => {
  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* seeded random so the graphics look the same on every visit */
  function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }
  function gauss(r) { let u = 0, v = 0; while (!u) u = r(); while (!v) v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  window.PF = { rng, gauss, css };

  /* running header */
  const run = document.querySelector('.run');
  const onScroll = () => run && run.classList.toggle('scrolled', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* section label + nav highlight */
  const where = document.querySelector('.run .where');
  const secs = [...document.querySelectorAll('[data-where]')];
  if (secs.length) {
    const io = new IntersectionObserver(es => {
      es.forEach(e => {
        if (!e.isIntersecting) return;
        if (where) where.textContent = e.target.dataset.where;
        const id = e.target.id;
        document.querySelectorAll('.run nav a').forEach(a => a.classList.toggle('on', a.getAttribute('href').endsWith('#' + id)));
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    secs.forEach(s => io.observe(s));
  }

  /* reveal on scroll */
  const rvs = document.querySelectorAll('.rv');
  if (reduce) rvs.forEach(e => e.classList.add('in'));
  else {
    const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io2.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    rvs.forEach(e => io2.observe(e));
  }

  /* ───────── pixel band: raw dots → aggregated cells → insight blocks ───────── */
  function band(canvas, opt = {}) {
    const ctx = canvas.getContext('2d');
    const reverse = !!opt.reverse, boxes = opt.boxes !== false;
    let base = null, W = 0, H = 0, cells = [], dpr = 1;
    function draw() {
      const r = canvas.getBoundingClientRect();
      if (!r.width) return;
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = r.width; H = r.height;
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
      const R = rng(opt.seed || 7);
      const ink = css('--ink'), acc = css('--accent');
      cells = [];
      const cy = H * (opt.cy || 0.5);
      let x = 0;
      let blues = 0;
      while (x < W) {
        let t = x / W; if (reverse) t = 1 - t;
        const pitch = Math.max(2.4, 2.2 + (opt.max || 30) * Math.pow(t, 1.8));
        const spread = H * (0.25 - 0.07 * t) * (opt.spread || 1);
        const dens = t < 0.5 ? 0.18 + 1.5 * t : 0.93 - 0.55 * (t - 0.5);
        for (let y = cy - spread * 2.4; y < cy + spread * 2.4; y += pitch) {
          const z = (y + pitch / 2 - cy) / spread;
          const p = Math.min(0.97, dens * Math.exp(-0.5 * z * z) * (opt.full ? 1.5 : 1));
          if (R() > p) continue;
          /* left = raw scattered observations, right = aggregated cells; blend smoothly */
          const raw = Math.max(0, 1 - t / 0.42);
          const gap = pitch > 10 ? 1.5 : pitch > 5 ? 1 : 0.6;
          const full = pitch - gap;
          const sz = raw > 0 ? Math.max(0.9, full * (1 - raw * 0.75) * (0.5 + R() * 0.5)) : full;
          const jx = raw * (R() - 0.5) * pitch * 2.4, jy = raw * (R() - 0.5) * pitch * 2.4;
          const lvl = Math.min(1, Math.max(0, 0.15 + 0.85 * Math.exp(-0.5 * z * z * 1.6) * (0.55 + R() * 0.6)));
          const g = Math.round(raw > 0.5 ? 20 + R() * 150 : 225 - lvl * 210);
          let col = `rgb(${g},${g},${g})`;
          const isBlue = blues < (opt.blues ?? 7) && t > 0.35 && t < 0.75 && R() < 0.012;
          if (isBlue) { col = acc; blues++; }
          ctx.fillStyle = col;
          ctx.fillRect(x + jx, y + jy, sz, sz);
          if (t > 0.72 && R() < 0.22 && lvl > 0.45) {
            ctx.fillStyle = '#EDEDE9';
            ctx.beginPath(); ctx.arc(x + full / 2, y + full / 2, pitch * 0.15, 0, 7); ctx.fill();
          }
          if (raw < 0.3) cells.push({ x, y, s: full, v: lvl });
        }
        x += pitch;
      }
      if (boxes && opt.labels) {
        ctx.lineWidth = 1; ctx.strokeStyle = acc; ctx.fillStyle = acc;
        ctx.font = `${W < 600 ? 10 : 12}px "IBM Plex Mono", monospace`;
        opt.labels.forEach(b => {
          const bx = W * b.x, by = H * b.y, bw = W * b.w, bh = H * b.h;
          ctx.strokeRect(Math.round(bx) + .5, Math.round(by) + .5, Math.round(bw), Math.round(bh));
          const tw = ctx.measureText(b.t).width;
          ctx.fillStyle = css('--paper'); ctx.fillRect(bx - 2, by - 19, tw + 6, 16);
          ctx.fillStyle = acc; ctx.fillText(b.t, bx, by - 6);
        });
      }
      base = ctx.getImageData(0, 0, canvas.width, canvas.height);
    }
    function hover(e) {
      if (!base || !cells.length) return;
      const r = canvas.getBoundingClientRect();
      const mx = e.clientX - r.left, my = e.clientY - r.top;
      let best = null, bd = 1e9;
      for (const c of cells) { const d = Math.abs(c.x + c.s / 2 - mx) + Math.abs(c.y + c.s / 2 - my); if (d < bd) { bd = d; best = c; } }
      ctx.putImageData(base, 0, 0);
      if (!best || bd > 40) return;
      ctx.strokeStyle = css('--ink'); ctx.lineWidth = 1;
      const pad = 4;
      ctx.strokeRect(Math.round(best.x - pad) + .5, Math.round(best.y - pad) + .5, Math.round(best.s + pad * 2), Math.round(best.s + pad * 2));
      ctx.font = '11px "IBM Plex Mono", monospace'; ctx.fillStyle = css('--ink');
      const tx = best.x + best.s + pad + 6, label = `v=${best.v.toFixed(2)}`;
      ctx.fillText(label, tx + 60 > W ? best.x - 60 : tx, best.y + 9);
    }
    draw();
    let tm; new ResizeObserver(() => { clearTimeout(tm); tm = setTimeout(draw, 120); }).observe(canvas);
    if (!opt.static) {
      canvas.addEventListener('pointermove', hover);
      canvas.addEventListener('pointerleave', () => base && ctx.putImageData(base, 0, 0));
    }
  }
  window.PF.band = band;

  /* ───────── pixel portrait from the photo ───────── */
  function pixelPortrait(canvas, src, cols = 24, rows = 32) {
    const img = new Image();
    img.onload = () => {
      const off = document.createElement('canvas'); off.width = cols; off.height = rows;
      const o = off.getContext('2d');
      const ar = img.width / img.height, tar = cols / rows;
      let sw = img.width, sh = img.height, sx = 0, sy = 0;
      if (ar > tar) { sw = img.height * tar; sx = (img.width - sw) / 2; } else { sh = img.width / tar; sy = (img.height - sh) / 2; }
      o.drawImage(img, sx, sy, sw, sh, 0, 0, cols, rows);
      const d = o.getImageData(0, 0, cols, rows).data;
      const P = 8; canvas.width = cols * P; canvas.height = rows * P;
      const c = canvas.getContext('2d');
      c.fillStyle = '#ECECE8'; c.fillRect(0, 0, canvas.width, canvas.height);
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const k = (j * cols + i) * 4, l = (0.3 * d[k] + 0.59 * d[k + 1] + 0.11 * d[k + 2]) / 255;
        const q = Math.round((1 - l) * 5) / 5; if (q < 0.15) continue;
        const g = Math.round(236 - q * 220);
        c.fillStyle = `rgb(${g},${g},${g})`; c.fillRect(i * P, j * P, P - 1, P - 1);
      }
    };
    img.src = src;
  }
  window.PF.pixelPortrait = pixelPortrait;

  /* tiny helper: re-render a figure on resize */
  window.PF.mount = (el, fn) => {
    if (!el) return;
    let last = 0;
    const go = () => { const w = Math.round(el.clientWidth); if (w && w !== last) { last = w; el.innerHTML = fn(w); } };
    go(); new ResizeObserver(go).observe(el);
  };
  window.PF.cells = (n, cls, cols) => `<div class="cells" style="grid-template-columns:repeat(${cols || n},1fr)">${Array.from({ length: n }, (_, i) => `<i class="${typeof cls === 'function' ? cls(i) : (cls || '')}"></i>`).join('')}</div>`;
})();
