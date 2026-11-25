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

  /* ───────── photo: only the area around the cursor turns into pixels ───────── */
  function pixelPhoto(box) {
    const src = box.dataset.src;
    const canvas = document.createElement('canvas');
    box.prepend(canvas);
    const ctx = canvas.getContext('2d');
    const img = new Image();
    let W = 0, H = 0, dpr = 1, C = 9, cols = 0, rows = 0, small = null, small2 = null, heat = null, noise = null, raf = 0;
    let px = -1e4, py = -1e4, inside = false;
    const R0 = 26, R1 = 78; /* full pixel radius, fade-out radius (CSS px) */

    function sample(scale) {
      const c = document.createElement('canvas');
      c.width = Math.ceil(cols / scale); c.height = Math.ceil(rows / scale);
      const x = c.getContext('2d');
      x.imageSmoothingQuality = 'high';
      x.drawImage(canvas, 0, 0, c.width, c.height);
      return x.getImageData(0, 0, c.width, c.height).data;
    }
    function layout() {
      const r = box.getBoundingClientRect();
      if (!r.width || !img.complete) return;
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = r.width; H = r.width * img.height / img.width;
      canvas.style.height = H + 'px';
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      cols = Math.ceil(W / C); rows = Math.ceil(H / C);
      small = sample(1); small2 = sample(2);
      heat = new Float32Array(cols * rows);
      noise = new Float32Array(cols * rows).map((_, i) => { const n = Math.sin(i * 127.1 + 311.7) * 43758.5453; return n - Math.floor(n); });
      paint();
    }
    function paint() {
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const c2 = Math.ceil(cols / 2);
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const h = heat[j * cols + i];
        if (h < 0.04 || h < noise[j * cols + i] * 0.85) continue;
        let k, s = C, x = i * C, y = j * C;
        if (h > 0.82) { /* coarser blocks at the centre */
          const bi = i >> 1, bj = j >> 1; k = (bj * c2 + bi) * 4; s = C * 2; x = bi * s; y = bj * s;
          if ((i & 1) || (j & 1)) continue;
          ctx.fillStyle = `rgb(${small2[k]},${small2[k + 1]},${small2[k + 2]})`;
        } else {
          k = (j * cols + i) * 4;
          ctx.fillStyle = `rgb(${small[k]},${small[k + 1]},${small[k + 2]})`;
        }
        ctx.fillRect(x, y, s - 0.6, s - 0.6);
      }
    }
    function tick() {
      let live = false;
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const idx = j * cols + i;
        if (inside) {
          const dx = (i + .5) * C - px, dy = (j + .5) * C - py, d = Math.hypot(dx, dy);
          const t = d <= R0 ? 1 : d >= R1 ? 0 : 1 - (d - R0) / (R1 - R0);
          if (t > heat[idx]) heat[idx] = t;
        }
        heat[idx] *= 0.93;
        if (heat[idx] > 0.04) live = true;
      }
      paint();
      raf = live || inside ? requestAnimationFrame(tick) : 0;
    }
    function move(e) {
      const r = canvas.getBoundingClientRect();
      px = e.clientX - r.left; py = e.clientY - r.top; inside = true;
      box.classList.add('touched');
      if (!raf && !reduce) raf = requestAnimationFrame(tick);
      if (reduce) { heat.fill(0); tick(); }
    }
    box.addEventListener('pointermove', move);
    box.addEventListener('pointerdown', move);
    box.addEventListener('pointerleave', () => { inside = false; });
    box.addEventListener('pointerup', e => { if (e.pointerType !== 'mouse') inside = false; });
    img.onload = layout;
    img.src = src;
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
