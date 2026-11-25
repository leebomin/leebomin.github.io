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

  /* ───────── photo: click → turns into grey pixel art, sweeping in from the bottom-right ───────── */
  function pixelPhoto(box) {
    const canvas = document.createElement('canvas');
    box.prepend(canvas);
    box.setAttribute('role', 'button'); box.tabIndex = 0;
    const ctx = canvas.getContext('2d');
    const img = new Image();
    let W = 0, H = 0, dpr = 1, cols = 0, rows = 0, lum = null, thr = null, raf = 0;
    let t = 0, target = 0, last = 0;
    const C = 8, SPREAD = 0.35, DUR = 1700, PAPER = '#ECECE8';
    function layout() {
      const r = box.getBoundingClientRect();
      if (!r.width || !img.complete) return;
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = r.width; H = r.width * img.height / img.width;
      canvas.style.height = H + 'px';
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      cols = Math.ceil(W / C); rows = Math.ceil(H / C);
      const c = document.createElement('canvas'); c.width = cols; c.height = rows;
      const x = c.getContext('2d'); x.imageSmoothingQuality = 'high';
      x.drawImage(img, 0, 0, cols, rows);
      const d = x.getImageData(0, 0, cols, rows).data;
      lum = new Uint8Array(cols * rows); thr = new Float32Array(cols * rows);
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const k = j * cols + i, L = 0.299 * d[k * 4] + 0.587 * d[k * 4 + 1] + 0.114 * d[k * 4 + 2];
        lum[k] = Math.round(Math.min(255, Math.max(0, (L - 20) * 1.12)) / 255 * 6) / 6 * 232; /* 7 grey steps, no pure white */
        const n = Math.sin(k * 127.1 + 311.7) * 43758.5453, rnd = n - Math.floor(n);
        const diag = ((cols - 1 - i) / cols + (rows - 1 - j) / rows) / 2; /* 0 at bottom-right */
        thr[k] = diag * (1 - SPREAD) + rnd * SPREAD;
      }
      paint();
    }
    function paint() {
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      if (t <= 0) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const e = t * t * (3 - 2 * t); /* ease */
      for (let k = 0; k < cols * rows; k++) {
        if (thr[k] > e * 1.02) continue;
        const i = k % cols, j = (k / cols) | 0, x = i * C, y = j * C;
        ctx.fillStyle = PAPER; ctx.fillRect(x, y, C, C);
        const g = lum[k]; ctx.fillStyle = `rgb(${g},${g},${g})`;
        ctx.fillRect(x + .5, y + .5, C - 1, C - 1);
      }
    }
    function tick(now) {
      const dt = last ? now - last : 16; last = now;
      t += Math.sign(target - t) * dt / DUR;
      t = Math.min(1, Math.max(0, t));
      paint();
      raf = t !== target ? requestAnimationFrame(tick) : 0;
    }
    function toggle() {
      target = target ? 0 : 1;
      box.classList.toggle('px', !!target);
      if (reduce) { t = target; paint(); return; }
      if (!raf) { last = 0; raf = requestAnimationFrame(tick); }
    }
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
