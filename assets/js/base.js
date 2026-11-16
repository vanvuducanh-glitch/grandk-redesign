/* Grand K redesign prototype — shared behaviour */
(function () {
  const root = document.documentElement;
  const qs = new URLSearchParams(location.search);
  const SHOT = qs.has('shot'); // screenshot/QA mode: no reveal animation
  if (!SHOT && !root.classList.contains('motion')) root.classList.add('js');
  if (SHOT) document.addEventListener('DOMContentLoaded', () => { const y = +qs.get('y') || 0; document.body.style.transform = `translateY(${-y}px)`; document.body.classList.toggle('shot-scrolled', y > 40); });

  /* ---------- Icons (line, 24px grid) ---------- */
  const P = {
    arrow: '<path d="M4 12h15M13 6l6 6-6 6"/>',
    'arrow-left': '<path d="M20 12H5M11 6l-6 6 6 6"/>',
    chevron: '<path d="M9 6l6 6-6 6"/>',
    'chevron-left': '<path d="M15 6l-6 6 6 6"/>',
    menu: '<path d="M4 8h16M4 16h16"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>',
    phone: '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a1 1 0 01-1 1A16 16 0 014 5a1 1 0 011-1z"/>',
    mail: '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/>',
    pin: '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    star: '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z" fill="currentColor" stroke="none"/>',
    play: '<path d="M8 5v14l11-7z" fill="currentColor" stroke="none"/>',
    pool: '<path d="M3 17c1.5 0 1.5 1 3 1s1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1M3 21c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1"/><path d="M8 15V5a2 2 0 014 0M16 15V5a2 2 0 00-4 0M8 9h8M8 12.5h8"/>',
    bar: '<path d="M6 4h12l-6 8z"/><path d="M12 12v7M8 20h8"/><path d="M8.5 7h7"/>',
    dining: '<path d="M7 3v7a2 2 0 002 2v9M11 3v7a2 2 0 01-2 2M9 3v6"/><path d="M17 21V3c-2 1-3 3.5-3 7h3"/>',
    meeting: '<rect x="3" y="4" width="18" height="11" rx="1"/><path d="M12 15v3M7 21l5-3 5 3"/>',
    kids: '<circle cx="12" cy="6" r="2.5"/><path d="M12 9v6M8 12h8M9 21l3-6 3 6"/>',
    car: '<path d="M4 16v-4l2-5h12l2 5v4"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="13" r=".8" fill="currentColor"/><circle cx="16.5" cy="13" r=".8" fill="currentColor"/>',
    bed: '<path d="M3 18V7M21 18v-6a3 3 0 00-3-3h-8v6M3 15h18"/><circle cx="6.5" cy="11.5" r="1.5"/>',
    area: '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
    view: '<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="2.5"/>',
    user: '<circle cx="12" cy="8" r="3.5"/><path d="M5 20a7 7 0 0114 0"/>',
    wifi: '<path d="M2.5 9a14 14 0 0119 0M5.5 12.5a9.5 9.5 0 0113 0M8.5 16a5 5 0 017 0"/><circle cx="12" cy="19" r=".8" fill="currentColor"/>',
    building: '<path d="M5 21V4h9v17M14 9h5v12M3 21h18M8 8h3M8 12h3M8 16h3"/>',
    plane: '<path d="M10.5 13.5L3 11l1.5-1.5 8 1L17 6a2 2 0 013 3l-4.5 4.5 1 8L15 23l-2.5-7.5L9 19v3l-1.5 1-1-3.5L3 18l1-1.5h3z" transform="scale(.9) translate(1.2 0)"/>',
    stadium: '<ellipse cx="12" cy="9" rx="9" ry="4"/><path d="M3 9v6c0 2.2 4 4 9 4s9-1.8 9-4V9"/>',
    landmark: '<path d="M3 21h18M5 21v-9M9.5 21v-9M14.5 21v-9M19 21v-9M2.5 12h19L12 4z"/>',
    spa: '<path d="M12 20c-4 0-8-2.5-8-7 3 0 6 1.5 8 4 2-2.5 5-4 8-4 0 4.5-4 7-8 7z"/><path d="M12 17c-2-3-2-7 0-12 2 5 2 9 0 12z"/>',
    gym: '<path d="M6 7v10M18 7v10M3 9.5v5M21 9.5v5M6 12h12"/>',
    kitchen: '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M4 10h16M8 6.5h1M8 13v4"/>',
    quote: '<path d="M10 7H6.5A2.5 2.5 0 004 9.5V13h5v5H4M20 7h-3.5A2.5 2.5 0 0014 9.5V13h5v5h-5" />',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    calendar: '<rect x="3.5" y="5" width="17" height="15" rx="1"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'
  };
  document.querySelectorAll('i[data-icon]').forEach(el => {
    const d = P[el.dataset.icon]; if (!d) return;
    el.outerHTML = `<svg class="ic ${el.className || ''}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
  });

  /* ---------- Header state on scroll ---------- */
  const header = document.querySelector('[data-header]');
  if (header) {
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40 || (SHOT && +qs.get('y') > 40));
    onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mobile menu ---------- */
  document.querySelectorAll('[data-menu-toggle]').forEach(b =>
    b.addEventListener('click', () => document.body.classList.toggle('menu-open')));
  document.querySelectorAll('.drawer nav a').forEach(a =>
    a.addEventListener('click', () => document.body.classList.remove('menu-open')));

  /* ---------- Reveal on scroll ---------- */
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => {
    es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: .12, rootMargin: '0px 0px -40px 0px' }) : null;
  document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('in'));

  /* ---------- Fader (hero slideshow) ---------- */
  document.querySelectorAll('[data-fader]').forEach(f => {
    const slides = [...f.querySelectorAll('[data-slide]')];
    const dots = [...f.querySelectorAll('[data-dot]')];
    let i = 0, t;
    const go = n => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle('is-active', k === i));
      dots.forEach((d, k) => d.classList.toggle('is-active', k === i));
      const c = f.querySelector('[data-count]'); if (c) c.textContent = String(i + 1).padStart(2, '0');
    };
    const play = () => { clearInterval(t); t = setInterval(() => go(i + 1), +(f.dataset.fader || 6000)); };
    dots.forEach((d, k) => d.addEventListener('click', () => { go(k); play(); }));
    f.querySelector('[data-fprev]')?.addEventListener('click', () => { go(i - 1); play(); });
    f.querySelector('[data-fnext]')?.addEventListener('click', () => { go(i + 1); play(); });
    go(0); play();
  });

  /* ---------- Tabs / slides (one visible at a time) ---------- */
  document.querySelectorAll('[data-slides]').forEach(w => {
    const items = [...w.querySelectorAll('[data-item]')];
    const tabs = [...w.querySelectorAll('[data-tab]')];
    let i = 0;
    const go = n => {
      i = (n + items.length) % items.length;
      items.forEach((s, k) => s.classList.toggle('is-active', k === i));
      tabs.forEach((s, k) => s.classList.toggle('is-active', k === i));
      const c = w.querySelector('[data-count]'); if (c) c.textContent = String(i + 1).padStart(2, '0');
    };
    tabs.forEach((t, k) => t.addEventListener('click', () => go(k)));
    w.querySelectorAll('[data-prev]').forEach(b => b.addEventListener('click', () => go(i - 1)));
    w.querySelectorAll('[data-next]').forEach(b => b.addEventListener('click', () => go(i + 1)));
    go(0);
  });

  /* ---------- Horizontal scrollers with arrows + progress ---------- */
  document.querySelectorAll('[data-scroller]').forEach(s => {
    const id = s.id; if (!id) return;
    const step = () => (s.firstElementChild?.getBoundingClientRect().width || 300) + parseFloat(getComputedStyle(s).columnGap || 0);
    document.querySelectorAll(`[data-scroll-prev="${id}"]`).forEach(b => b.addEventListener('click', () => s.scrollBy({ left: -step(), behavior: 'smooth' })));
    document.querySelectorAll(`[data-scroll-next="${id}"]`).forEach(b => b.addEventListener('click', () => s.scrollBy({ left: step(), behavior: 'smooth' })));
    const bar = document.querySelector(`[data-progress="${id}"]`);
    if (bar) {
      const upd = () => {
        const max = s.scrollWidth - s.clientWidth;
        const vis = s.clientWidth / s.scrollWidth;
        bar.style.width = (vis * 100) + '%';
        bar.style.transform = `translateX(${max > 0 ? (s.scrollLeft / max) * ((1 - vis) / vis) * 100 : 0}%)`;
      };
      upd(); s.addEventListener('scroll', upd, { passive: true }); window.addEventListener('resize', upd);
    }
  });

  /* ---------- Booking defaults ---------- */
  const fmt = d => d.toISOString().slice(0, 10);
  const d1 = new Date(); d1.setDate(d1.getDate() + 1);
  const d2 = new Date(); d2.setDate(d2.getDate() + 3);
  document.querySelectorAll('input[data-checkin]').forEach(i => { i.value = fmt(d1); i.min = fmt(new Date()); });
  document.querySelectorAll('input[data-checkout]').forEach(i => { i.value = fmt(d2); i.min = fmt(d1); });
  document.querySelectorAll('form.booking').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const b = f.querySelector('button[type=submit]');
    const old = b.innerHTML; b.innerHTML = 'Đang kiểm tra…';
    setTimeout(() => { b.innerHTML = old; alert('Prototype: bước này sẽ chuyển sang công cụ đặt phòng (Booking Engine).'); }, 600);
  }));

  /* ---------- Dev grid overlay: press G ---------- */
  const ov = document.createElement('div'); ov.className = 'grid-overlay'; ov.setAttribute('aria-hidden', 'true');
  ov.innerHTML = '<div class="container"><div class="g12">' + '<i></i>'.repeat(12) + '</div></div>';
  document.body.appendChild(ov);
  const fitOverlay = () => { const n = parseInt(getComputedStyle(root).getPropertyValue('--cols')) || 12; ov.querySelectorAll('i').forEach((c, k) => c.style.display = k < n ? '' : 'none'); };
  fitOverlay(); window.addEventListener('resize', fitOverlay);
  document.addEventListener('keydown', e => { if ((e.key === 'g' || e.key === 'G') && !e.target.closest('input,select,textarea')) root.classList.toggle('show-grid'); });
  if (qs.has('grid')) root.classList.add('show-grid');

  /* ---------- Prototype option switcher ---------- */
  const here = location.pathname.split('/').pop() || 'index.html';
  const sw = document.createElement('nav');
  sw.className = 'opt-switch'; sw.setAttribute('aria-label', 'Chuyển phương án');
  const m = here.match(/^option-(\d)(-[a-z0-9-]+)?\.html$/);
  const cur = m ? +m[1] : 0, suffix = m && m[2] ? m[2] : '';
  const group = suffix.startsWith('-room-') ? '-rooms' : suffix.startsWith('-news-') ? '-news' : suffix;
  const pages = [['', 'Trang chủ'], ['-rooms', 'Phòng'], ['-news', 'Tin tức'], ['-contact', 'Liên hệ']];
  sw.innerHTML = '<a href="index.html">Tất cả</a>' + [1, 4, 5].map(n =>
    `<a href="option-${n}${suffix}.html" class="${cur === n ? 'on' : ''}">0${n}</a>`).join('') +
    (cur ? '<span class="sep" aria-hidden="true"></span>' + pages.map(([s2, t]) => `<a href="option-${cur}${s2}.html" class="pg${s2 === group ? ' cur' : ''}">${t}</a>`).join('') : '');
  if (qs.has('measure')) window.addEventListener('load', () => {
    const vw = document.documentElement.clientWidth, out = [];
    document.querySelectorAll('body *').forEach(e => { const r = e.getBoundingClientRect(); if (r.right > vw + 1 && r.width > 0 && !e.closest('.hscroll,.drawer')) out.push(`${e.tagName}.${[...e.classList].join('.')} w=${Math.round(r.width)} right=${Math.round(r.right)}`); });
    const pre = document.createElement('pre'); pre.id = 'measure'; pre.textContent = `vw=${vw} inner=${innerWidth}\n` + out.slice(0, 25).join('\n'); document.body.appendChild(pre);
  });
  if (here !== 'index.html' && here !== '' && !(SHOT && window.self !== window.top)) document.body.appendChild(sw);
})();
