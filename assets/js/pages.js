/* Grand K — sub-page behaviour: filters (rooms, news) and the contact form */
(function () {
  const refresh = () => { if (window.ScrollTrigger) setTimeout(() => ScrollTrigger.refresh(), 60); };

  /* ---------- Generic chip filter: <div data-filter-for="#list"> chips[data-f] ; items[data-cat] ---------- */
  document.querySelectorAll('[data-filter-for]').forEach(bar => {
    const list = document.querySelector(bar.dataset.filterFor); if (!list) return;
    const items = [...list.querySelectorAll('[data-cat]')];
    const count = document.querySelector(bar.dataset.count || '');
    const chips = [...bar.querySelectorAll('[data-f]')];
    chips.forEach(c => {
      const f = c.dataset.f;
      const n = f === 'all' ? items.length : items.filter(i => i.dataset.cat.split(' ').includes(f)).length;
      const s = document.createElement('span'); s.className = 'n'; s.textContent = n; c.appendChild(s);
    });
    const apply = f => {
      let shown = 0;
      items.forEach(i => {
        const ok = f === 'all' || i.dataset.cat.split(' ').includes(f);
        i.classList.toggle('is-hidden', !ok);
        if (ok) {
          shown++;
          if (window.gsap) gsap.fromTo(i, { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: .7, ease: 'power3.out', delay: shown * .05, clearProps: 'transform' });
        }
      });
      if (count) count.textContent = `${shown} kết quả`;
      refresh();
    };
    bar.addEventListener('click', e => {
      const c = e.target.closest('[data-f]'); if (!c) return;
      chips.forEach(x => x.classList.toggle('on', x === c));
      apply(c.dataset.f);
    });
  });

  /* ---------- Room deep links: #deluxe etc. scroll with Lenis if present ---------- */
  document.querySelectorAll('[data-room-link]').forEach(a => a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href')); if (!t) return;
    e.preventDefault();
    if (window.GK && GK.lenis) GK.lenis.scrollTo(t, { offset: -110 }); else t.scrollIntoView({ behavior: 'smooth' });
  }));

  /* ---------- Contact form validation (prototype — no data leaves the page) ---------- */
  const form = document.querySelector('form.cform');
  if (form) {
    const rules = {
      name: v => v.trim().length >= 2 || 'Vui lòng nhập họ và tên.',
      email: v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) || 'Email chưa đúng định dạng.',
      phone: v => !v.trim() || /^[+0-9 ().-]{8,16}$/.test(v.trim()) || 'Số điện thoại chưa đúng.',
      topic: v => !!v || 'Vui lòng chọn chủ đề.',
      message: v => v.trim().length >= 10 || 'Lời nhắn cần tối thiểu 10 ký tự.'
    };
    const check = el => {
      const fn = rules[el.name]; if (!fn) return true;
      const r = fn(el.value); const box = el.closest('.fld');
      box.classList.toggle('bad', r !== true);
      box.querySelector('.err').textContent = r === true ? '' : r;
      return r === true;
    };
    form.querySelectorAll('input, select, textarea').forEach(el => {
      el.addEventListener('blur', () => check(el));
      el.addEventListener('input', () => el.closest('.fld')?.classList.contains('bad') && check(el));
    });
    form.addEventListener('submit', e => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll('input[name], select[name], textarea[name]').forEach(el => { if (!check(el)) ok = false; });
      const consent = form.querySelector('[name=consent]');
      const cbox = consent.closest('.consent'); cbox.classList.toggle('bad', !consent.checked);
      if (!consent.checked) ok = false;
      if (!ok) { form.querySelector('.bad')?.querySelector('input,select,textarea')?.focus(); return; }
      const btn = form.querySelector('button[type=submit]'); const old = btn.innerHTML;
      btn.innerHTML = 'Đang gửi…'; btn.disabled = true;
      setTimeout(() => {
        btn.innerHTML = old; btn.disabled = false;
        form.style.display = 'none';
        const okBox = document.querySelector('.form-ok'); okBox.classList.add('show');
        okBox.querySelector('[data-name]').textContent = form.name.value.trim();
        refresh();
      }, 900);
    });
    document.querySelector('[data-form-reset]')?.addEventListener('click', () => {
      form.reset(); form.style.display = ''; document.querySelector('.form-ok').classList.remove('show'); refresh();
    });
  }
})();

/* ---------- Detail pages: lightbox, share, table of contents ---------- */
(function () {
  /* Lightbox: <div data-lightbox> a[href=img][data-caption] … ; [data-lightbox-open] opens at 0 */
  const group = document.querySelector('[data-lightbox]');
  if (group) {
    const items = [...group.querySelectorAll('a[href]')].map(a => ({ src: a.getAttribute('href'), cap: a.dataset.caption || '' }));
    const lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Thư viện ảnh');
    lb.innerHTML = '<div class="lb-top"><span class="eyebrow" data-lb-count></span><button class="close-b" aria-label="Đóng">×</button></div><div class="lb-stage"><img alt=""><button class="nav-b prev-b" aria-label="Ảnh trước">‹</button><button class="nav-b next-b" aria-label="Ảnh sau">›</button></div><p class="lb-cap t-sm"></p>';
    document.body.appendChild(lb);
    const img = lb.querySelector('img'), cap = lb.querySelector('.lb-cap'), cnt = lb.querySelector('[data-lb-count]');
    let i = 0, last = null;
    const show = n => {
      i = (n + items.length) % items.length;
      img.classList.remove('ready');
      const it = items[i];
      const pre = new Image(); pre.onload = () => { img.src = it.src; img.alt = it.cap; requestAnimationFrame(() => img.classList.add('ready')); }; pre.src = it.src;
      cap.textContent = it.cap; cnt.textContent = `${String(i + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`;
    };
    const open = n => { last = document.activeElement; lb.classList.add('open'); show(n); window.GK?.lenis?.stop(); lb.querySelector('.close-b').focus(); };
    const close = () => { lb.classList.remove('open'); window.GK?.lenis?.start(); last?.focus(); };
    group.querySelectorAll('a[href]').forEach((a, k) => a.addEventListener('click', e => { e.preventDefault(); open(k); }));
    document.querySelectorAll('[data-lightbox-open]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); e.stopPropagation(); open(0); }));
    lb.querySelector('.close-b').addEventListener('click', close);
    lb.querySelector('.prev-b').addEventListener('click', () => show(i - 1));
    lb.querySelector('.next-b').addEventListener('click', () => show(i + 1));
    lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lb-stage')) close(); });
    document.addEventListener('keydown', e => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowRight') show(i + 1); if (e.key === 'ArrowLeft') show(i - 1);
    });
  }

  /* Copy link */
  document.querySelectorAll('[data-copy-link]').forEach(b => b.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(location.href.split('?')[0]); } catch (e) {}
    const old = b.textContent; b.classList.add('copied'); b.textContent = '✓';
    setTimeout(() => { b.classList.remove('copied'); b.textContent = old; }, 1600);
  }));

  /* Table of contents: highlight the section being read */
  const toc = document.querySelector('.toc');
  if (toc && 'IntersectionObserver' in window) {
    const links = [...toc.querySelectorAll('a[href^="#"]')];
    const heads = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) links.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id));
    }), { rootMargin: '-20% 0px -70% 0px' });
    heads.forEach(h => io.observe(h));
    links.forEach(a => a.addEventListener('click', e => {
      const t = document.querySelector(a.getAttribute('href')); if (!t) return;
      e.preventDefault();
      if (window.GK?.lenis) GK.lenis.scrollTo(t, { offset: -100 }); else t.scrollIntoView({ behavior: 'smooth' });
    }));
  }
})();
