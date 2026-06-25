(function() {
    'use strict';

    const POOL = ['209', '156', '192', '233', '175'];
    const INTERVAL = 8000;
    const DRIFT_PX = 20;
    const TRANSITION = 'opacity 1s ease, transform 1s ease';

    console.log('[HeroCarousel] Script loaded');

    // Session persistence
    let idx = parseInt(sessionStorage.getItem('heroBgIndex'), 10);
    if (isNaN(idx)) {
        idx = Math.floor(Math.random() * POOL.length);
        console.log('[HeroCarousel] First visit, random start:', POOL[idx]);
    } else {
        console.log('[HeroCarousel] Resumed from session, index:', idx, 'image:', POOL[idx]);
    }

    let lastChange = parseInt(sessionStorage.getItem('heroBgLast'), 10) || Date.now();
    let elapsed = Date.now() - lastChange;

    // Catch up if overdue
    while (elapsed > INTERVAL) {
        idx = (idx + 1) % POOL.length;
        elapsed -= INTERVAL;
        lastChange += INTERVAL;
    }

    const hero = document.querySelector('.hero');
    if (!hero) {
        console.error('[HeroCarousel] .hero not found');
        return;
    }
    console.log('[HeroCarousel] .hero found');

    // Create gradient overlay if absent
    let grad = hero.querySelector('.hero-gradient');
    if (!grad) {
        grad = document.createElement('div');
        grad.className = 'hero-gradient';
        hero.insertBefore(grad, hero.firstChild);
    }

    // Create layers if absent
    let a = hero.querySelector('.hero-bg-layer-a');
    let b = hero.querySelector('.hero-bg-layer-b');
    if (!a) {
        console.log('[HeroCarousel] Creating layers');
        a = document.createElement('div');
        a.className = 'hero-bg-layer hero-bg-layer-a';
        b = document.createElement('div');
        b.className = 'hero-bg-layer hero-bg-layer-b';
        hero.insertBefore(b, hero.firstChild);
        hero.insertBefore(a, hero.firstChild);
    } else {
        console.log('[HeroCarousel] Layers already exist');
    }

    // Set initial state — NO animation on load
    const currentId = POOL[idx];
    a.style.backgroundImage = "url('gallery/medium/" + currentId + "_medium.jpg')";
    a.style.opacity = '1';
    a.style.transform = 'translateX(0)';
    a.style.transition = 'none';
    a.classList.add('active');
    console.log('[HeroCarousel] Layer A set to:', currentId);

    b.style.opacity = '0';
    b.style.transform = 'translateX(0)';
    b.style.transition = 'none';
    console.log('[HeroCarousel] Layer B hidden');

    // Preload next
    const nextId = POOL[(idx + 1) % POOL.length];
    const preload = new Image();
    preload.src = "gallery/medium/" + nextId + "_medium.jpg";
    console.log('[HeroCarousel] Preloading:', nextId);

    // Start timer
    const delay = INTERVAL - elapsed;
    console.log('[HeroCarousel] First rotation in', delay, 'ms');

    setTimeout(function() {
        console.log('[HeroCarousel] Starting rotation');
        a.style.transition = TRANSITION;
        b.style.transition = TRANSITION;
        rotate();
        setInterval(rotate, INTERVAL);
    }, delay);

    function rotate() {
        var nextIdx = (idx + 1) % POOL.length;
        var nextId = POOL[nextIdx];
        var entering = a.classList.contains('active') ? b : a;
        var leaving = a.classList.contains('active') ? a : b;

        console.log('[HeroCarousel] Rotating to:', nextId, 'entering:', entering === a ? 'A' : 'B');

        // Alternate drift direction
        var direction = (nextIdx % 2 === 0) ? DRIFT_PX : -DRIFT_PX;

        // Prepare entering layer: position off-screen, no transition yet
        entering.style.transition = 'none';
        entering.style.backgroundImage = "url('gallery/medium/" + nextId + "_medium.jpg')";
        entering.style.opacity = '0';
        entering.style.transform = 'translateX(' + direction + 'px)';

        // Force reflow to apply the above instantly
        void entering.offsetWidth;

        // Now enable transition and animate in
        entering.style.transition = TRANSITION;
        entering.style.opacity = '1';
        entering.style.transform = 'translateX(0)';
        entering.classList.add('active');

        // Animate leaving layer out
        leaving.style.transition = TRANSITION;
        leaving.style.opacity = '0';
        leaving.classList.remove('active');

        idx = nextIdx;
        sessionStorage.setItem('heroBgIndex', idx);
        sessionStorage.setItem('heroBgLast', Date.now());

        // Preload next+1
        var preloadNext = POOL[(idx + 1) % POOL.length];
        var img = new Image();
        img.src = "gallery/medium/" + preloadNext + "_medium.jpg";
    }
})();
