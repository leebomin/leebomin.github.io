/* LEE BOMIN — portfolio · shared behaviour */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* reveal on scroll */
  const rvs = document.querySelectorAll('.rv');
  if (reduce || !('IntersectionObserver' in window)) rvs.forEach(e => e.classList.add('in'));
  else {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -6% 0px' });
    rvs.forEach(e => io.observe(e));
  }

  /* sidebar nav: underline the section in view */
  const links = [...document.querySelectorAll('.side nav a[href^="#"]')];
  if (links.length) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) links.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id));
    }), { rootMargin: '-35% 0px -60% 0px' });
    links.forEach(a => { const s = document.querySelector(a.getAttribute('href')); if (s) io.observe(s); });
  }

  /* ───────── photo: hover → pixels around the cursor · click → whole photo sweeps into grey pixel art ───────── */
  function pixelPhoto(box) {
    const canvas = document.createElement('canvas');
    box.prepend(canvas);
    box.setAttribute('role', 'button'); box.tabIndex = 0;
    const ctx = canvas.getContext('2d');
    const img = new Image();
    let W = 0, H = 0, dpr = 1, cols = 0, rows = 0, rgb = null, rgb2 = null, lum = null, thr = null, heat = null, noise = null, raf = 0;
    let t = 0, target = 0, last = 0, px = -1e4, py = -1e4, inside = false;
    const C = 8, SPREAD = 0.35, DUR = 1700, R0 = 24, R1 = 72, PAPER = '#ECECE8';
    function sample(n) {
      const c = document.createElement('canvas'); c.width = Math.ceil(cols / n); c.height = Math.ceil(rows / n);
      const x = c.getContext('2d'); x.imageSmoothingQuality = 'high';
      x.drawImage(img, 0, 0, c.width, c.height);
      return x.getImageData(0, 0, c.width, c.height).data;
    }
    function layout() {
      const r = box.getBoundingClientRect();
      if (!r.width || !img.complete) return;
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = r.width; H = r.width * img.height / img.width;
      canvas.style.height = H + 'px';
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      cols = Math.ceil(W / C); rows = Math.ceil(H / C);
      rgb = sample(1); rgb2 = sample(2);
      const N = cols * rows;
      lum = new Uint8Array(N); thr = new Float32Array(N); heat = new Float32Array(N); noise = new Float32Array(N);
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const k = j * cols + i, L = 0.299 * rgb[k * 4] + 0.587 * rgb[k * 4 + 1] + 0.114 * rgb[k * 4 + 2];
        lum[k] = Math.round(Math.min(255, Math.max(0, (L - 20) * 1.12)) / 255 * 6) / 6 * 232; /* 7 grey steps */
        const n = Math.sin(k * 127.1 + 311.7) * 43758.5453, rnd = n - Math.floor(n);
        noise[k] = rnd;
        const diag = ((cols - 1 - i) / cols + (rows - 1 - j) / rows) / 2; /* 0 at bottom-right */
        thr[k] = diag * (1 - SPREAD) + rnd * SPREAD;
      }
      paint();
    }
    function paint() {
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const e = t * t * (3 - 2 * t), c2 = Math.ceil(cols / 2);
      for (let k = 0; k < cols * rows; k++) {
        const i = k % cols, j = (k / cols) | 0, x = i * C, y = j * C;
        if (e > 0 && thr[k] <= e * 1.02) { /* pixel-art state: grey steps on a grid */
          let g = lum[k];
          const h = heat[k]; if (h > 0.3) g = Math.max(0, g - 40 * h); /* hover still answers in pixel-art mode */
          ctx.fillStyle = PAPER; ctx.fillRect(x, y, C, C);
          ctx.fillStyle = `rgb(${g},${g},${g})`; ctx.fillRect(x + .5, y + .5, C - 1, C - 1);
          continue;
        }
        const h = heat[k];
        if (h < 0.04 || h < noise[k] * 0.85) continue; /* hover: colour pixels around the cursor */
        if (h > 0.82) {
          if ((i & 1) || (j & 1)) continue;
          const q = ((j >> 1) * c2 + (i >> 1)) * 4;
          ctx.fillStyle = `rgb(${rgb2[q]},${rgb2[q + 1]},${rgb2[q + 2]})`; ctx.fillRect(x, y, C * 2 - .6, C * 2 - .6);
        } else {
          ctx.fillStyle = `rgb(${rgb[k * 4]},${rgb[k * 4 + 1]},${rgb[k * 4 + 2]})`; ctx.fillRect(x, y, C - .6, C - .6);
        }
      }
    }
    function tick(now) {
      const dt = last ? Math.min(now - last, 50) : 16; last = now;
      if (t !== target) t = Math.min(1, Math.max(0, t + Math.sign(target - t) * dt / DUR));
      let live = false;
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const k = j * cols + i;
        if (inside) {
          const d = Math.hypot((i + .5) * C - px, (j + .5) * C - py);
          const v = d <= R0 ? 1 : d >= R1 ? 0 : 1 - (d - R0) / (R1 - R0);
          if (v > heat[k]) heat[k] = v;
        }
        heat[k] *= 0.93; if (heat[k] > 0.04) live = true;
      }
      paint();
      raf = (live || inside || t !== target) ? requestAnimationFrame(tick) : 0;
    }
    function run() { if (!raf && heat) { last = 0; raf = requestAnimationFrame(tick); } }
    function move(e) {
      const r = canvas.getBoundingClientRect();
      px = e.clientX - r.left; py = e.clientY - r.top; inside = true;
      if (reduce) return; run();
    }
    function toggle() {
      target = target ? 0 : 1;
      box.classList.toggle('px', !!target);
      if (reduce) { t = target; paint(); return; }
      run();
    }
    box.addEventListener('pointermove', move);
    box.addEventListener('pointerleave', () => { inside = false; });
    box.addEventListener('pointerup', e => { if (e.pointerType !== 'mouse') inside = false; });
    box.addEventListener('click', toggle);
    box.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
    img.onload = layout;
    img.src = box.dataset.src;
    let tm; new ResizeObserver(() => { clearTimeout(tm); tm = setTimeout(layout, 100); }).observe(box);
  }
  document.querySelectorAll('.photo[data-src]').forEach(pixelPhoto);

  /* tiny helpers shared with figs.js */
  window.PF = {
    mount(el, fn) {
      if (!el) return;
      let last = 0;
      const go = () => { const w = Math.round(el.clientWidth); if (w && w !== last) { last = w; el.innerHTML = fn(w); } };
      go(); new ResizeObserver(go).observe(el);
    },
    cells: (n, cls, cols) => `<div class="cells" style="grid-template-columns:repeat(${cols || n},1fr)">${Array.from({ length: n }, (_, i) => `<i class="${typeof cls === 'function' ? cls(i) : (cls || '')}"></i>`).join('')}</div>`,
  };
  document.querySelectorAll('[data-cells]').forEach(el => {
    const [n, k, cols, cls] = el.dataset.cells.split(',');
    el.innerHTML = window.PF.cells(+n, i => i < +k ? (cls || 'f') : '', +cols);
  });
})();
