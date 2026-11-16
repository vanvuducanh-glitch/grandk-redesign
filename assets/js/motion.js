/* ==========================================================
   Grand K — Motion system v1 (GSAP 3.13 + ScrollTrigger + SplitText + Lenis)
   One vocabulary shared by every page:
     data-hero="media|split|script|fade"  page-load intro (in DOM order)
     data-split           heading: lines rise from a mask
     data-script          Tangerine accent: drawn left → right (clip)
     data-fade            fade + rise 32px (batched)
     data-stagger         children fade + rise in sequence
     data-img="up|left"   image frame wipes open, image settles 1.2 → 1
     data-parallax="8"    image travels ±n% inside a .px frame (scrub)
     data-float="60"      element drifts n px against the scroll (scrub)
     data-counter="262"   number counts up when visible
     data-line            divider draws from the left
     data-marquee         row loops horizontally
   Timing: text 1–1.2s power3/4.out · images 1.4s expo.out · stagger .08–.12
   ========================================================== */
(function () {
  const root = document.documentElement;
  if (!root.classList.contains('motion')) return;
  if (!window.gsap || !window.ScrollTrigger) { root.classList.remove('motion'); return; }

  const hasSplit = !!window.SplitText;
  gsap.registerPlugin(ScrollTrigger);
  if (hasSplit) gsap.registerPlugin(SplitText);

  const CLIP_HIDE = 'inset(-30% 100% -30% 0%)';
  const CLIP_SHOW = 'inset(-30% 0% -30% 0%)';
  const mm = gsap.matchMedia();
  const isTouch = matchMedia('(hover: none)').matches;

  /* ---------- Smooth scroll ---------- */
  let lenis = null;
  if (window.Lenis && !isTouch) {
    lenis = new Lenis({ duration: 1.15, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const id = a.getAttribute('href'); if (id.length < 2) return;
      const target = document.querySelector(id); if (!target) return;
      e.preventDefault(); document.body.classList.remove('menu-open');
      lenis.scrollTo(target, { offset: -72, duration: 1.4 });
    }));
    document.querySelectorAll('[data-menu-toggle]').forEach(b => b.addEventListener('click', () =>
      document.body.classList.contains('menu-open') ? lenis.stop() : lenis.start()));
  }
  window.GK = { lenis };

  /* ---------- Helpers ---------- */
  const fixMasks = s => { if (s && s.masks) gsap.set(s.masks, { paddingTop: '.16em', marginTop: '-.16em', paddingBottom: '.1em', marginBottom: '-.1em' }); };
  const splitLines = (el, opts = {}) => SplitText.create(el, Object.assign({ type: 'lines', mask: 'lines', linesClass: 'split-line' }, opts));

  /* ---------- Hero intro (runs after loader) ---------- */
  function heroIntro() {
    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
    gsap.utils.toArray('[data-hero]').forEach((el, i) => {
      const type = el.dataset.hero || 'fade';
      gsap.set(el, { autoAlpha: 1 });
      if (type === 'media') {
        tl.fromTo(el, { scale: 1.18 }, { scale: 1, duration: 2.6, ease: 'expo.out', clearProps: 'transform' }, 0);
      } else if (type === 'split' && hasSplit) {
        const s = splitLines(el); fixMasks(s);
        tl.from(s.lines, { yPercent: 115, duration: 1.25, ease: 'power4.out', stagger: .1 }, i === 0 ? .1 : '-=0.95');
        tl.add(() => s.revert());
      } else if (type === 'script') {
        tl.fromTo(el, { clipPath: CLIP_HIDE, x: -14 }, { clipPath: CLIP_SHOW, x: 0, duration: 1.6, ease: 'power2.inOut', clearProps: 'clipPath,transform' }, i === 0 ? .15 : '-=1.1');
      } else {
        tl.from(el, { y: 26, autoAlpha: 0, duration: 1 }, i === 0 ? .2 : '-=0.8');
      }
    });
    return tl;
  }

  /* ---------- Scroll reveals ---------- */
  function scrollReveals() {
    // Headings — line mask reveal
    gsap.utils.toArray('[data-split]').forEach(el => {
      gsap.set(el, { autoAlpha: 1 });
      if (!hasSplit) { gsap.from(el, { y: 30, autoAlpha: 0, duration: 1, scrollTrigger: { trigger: el, start: 'top 88%', once: true } }); return; }
      splitLines(el, {
        autoSplit: true,
        onSplit(self) {
          fixMasks(self);
          return gsap.from(self.lines, { yPercent: 115, duration: 1.15, ease: 'power4.out', stagger: .09,
            scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
        }
      });
    });

    // Script accents — handwriting wipe
    gsap.utils.toArray('[data-script]').forEach(el => {
      gsap.set(el, { autoAlpha: 1, clipPath: CLIP_HIDE, x: -14 });
      gsap.to(el, { clipPath: CLIP_SHOW, x: 0, duration: 1.7, ease: 'power2.inOut', clearProps: 'clipPath,transform',
        scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
    });

    // Fades — batched so items entering together cascade
    const fades = gsap.utils.toArray('[data-fade]');
    gsap.set(fades, { autoAlpha: 0, y: 32 });
    ScrollTrigger.batch(fades, { start: 'top 92%', once: true,
      onEnter: b => gsap.to(b, { autoAlpha: 1, y: 0, duration: 1, ease: 'power3.out', stagger: .1, overwrite: true, clearProps: 'transform' }) });

    // Stagger groups
    gsap.utils.toArray('[data-stagger]').forEach(g => {
      const kids = [...g.children];
      gsap.set(kids, { autoAlpha: 0, y: 40 });
      gsap.to(kids, { autoAlpha: 1, y: 0, duration: 1.05, ease: 'power3.out', stagger: .12, clearProps: 'transform',
        scrollTrigger: { trigger: g, start: 'top 86%', once: true } });
    });

    // Image frames — wipe open + settle
    gsap.utils.toArray('[data-img]').forEach(el => {
      const dir = el.dataset.img || 'up';
      const from = dir === 'left' ? 'inset(0% 100% 0% 0%)' : dir === 'right' ? 'inset(0% 0% 0% 100%)' : 'inset(100% 0% 0% 0%)';
      const img = el.matches('img') ? null : el.querySelector('img:not([data-parallax])');
      gsap.set(el, { autoAlpha: 1, clipPath: from });
      const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 86%', once: true } });
      tl.to(el, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.4, ease: 'expo.out', clearProps: 'clipPath' });
      if (img) tl.fromTo(img, { scale: 1.22 }, { scale: 1, duration: 1.9, ease: 'expo.out', clearProps: 'transform' }, 0);
    });

    // Dividers
    gsap.utils.toArray('[data-line]').forEach(el => gsap.fromTo(el, { scaleX: 0, transformOrigin: 'left center' },
      { scaleX: 1, duration: 1.4, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 92%', once: true } }));

    // Counters
    gsap.utils.toArray('[data-counter]').forEach(el => {
      const end = parseFloat(el.dataset.counter); const o = { v: 0 };
      el.textContent = '0';
      gsap.to(o, { v: end, duration: 2, ease: 'power2.out', onUpdate: () => { el.textContent = Math.round(o.v).toLocaleString('vi-VN'); },
        scrollTrigger: { trigger: el, start: 'top 92%', once: true } });
    });

    // Parallax + float (lighter on small screens)
    mm.add({ big: '(min-width: 768px)', small: '(max-width: 767px)' }, ctx => {
      const k = ctx.conditions.big ? 1 : .5;
      gsap.utils.toArray('[data-parallax]').forEach(img => {
        const s = (parseFloat(img.dataset.parallax) || 8) * k;
        gsap.fromTo(img, { yPercent: -s }, { yPercent: s, ease: 'none',
          scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
      });
      gsap.utils.toArray('[data-float]').forEach(el => {
        const d = (parseFloat(el.dataset.float) || 60) * k;
        gsap.fromTo(el, { y: d / 2 }, { y: -d / 2, ease: 'none',
          scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: true } });
      });
    });

    // Marquee
    gsap.utils.toArray('[data-marquee]').forEach(row => {
      row.innerHTML += row.innerHTML;
      gsap.to(row, { xPercent: -50, duration: 28, ease: 'none', repeat: -1 });
    });

    // Header: hide on scroll down, show on scroll up
    const hdr = document.querySelector('[data-header]');
    if (hdr) ScrollTrigger.create({ start: 0, end: 'max', onUpdate: self => {
      const hide = self.direction === 1 && self.scroll() > 480 && !document.body.classList.contains('menu-open');
      hdr.classList.toggle('hdr-hide', hide);
    } });

    // Reading progress
    const bar = document.createElement('div'); bar.className = 'progress-top'; document.body.appendChild(bar);
    gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: .3 } });

    // Re-measure after tab/slider changes and once images are in
    document.addEventListener('click', e => { if (e.target.closest('[data-tab],[data-prev],[data-next]')) setTimeout(() => ScrollTrigger.refresh(), 80); });
    window.addEventListener('load', () => ScrollTrigger.refresh());
  }

  /* ---------- Loader → intro → scroll ---------- */
  function start() {
    const loader = document.querySelector('.loader');
    let seen = false; try { seen = sessionStorage.getItem('gk-intro') === '1'; sessionStorage.setItem('gk-intro', '1'); } catch (e) {}
    const tl = gsap.timeline();
    if (loader && !seen) {
      tl.to(loader.querySelector('img'), { autoAlpha: 1, duration: .6, ease: 'power2.out' })
        .to(loader.querySelector('.bar i'), { scaleX: 1, duration: .9, ease: 'power2.inOut' }, '<')
        .to(loader, { clipPath: 'inset(0% 0% 100% 0%)', duration: 1.1, ease: 'expo.inOut' }, '+=.05')
        .set(loader, { display: 'none' });
      tl.add(heroIntro(), '-=0.6');
    } else {
      if (loader) loader.style.display = 'none';
      tl.add(heroIntro(), 0);
    }
    scrollReveals();
  }

  /* QA hook: ?qa&y=1800 → after the intro, jump to y so headless screenshots show settled reveals */
  const qa = new URLSearchParams(location.search);
  if (qa.has('qa')) setTimeout(() => {
    const y = +qa.get('y') || 0;
    if (lenis) lenis.scrollTo(y, { immediate: true, force: true }); else window.scrollTo(0, y);
    ScrollTrigger.update();
  }, 3200);

  let started = false;
  const go = () => { if (!started) { started = true; start(); } };
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(go);
  setTimeout(go, 1500);
})();
