(() => {
  const BP = 768;
  const CSS_ATTR = 'data-css';
  const JS_ID = 'swiper-js';

  let type, swipers = [];

  const device = () => innerWidth <= BP ? 'm' : 'p';

  const css = t => t === 'm'
    ? [
        'https://trnservice2025-stack.github.io/shoppingnt/moassets/css/common.css',
        'https://trnservice2025-stack.github.io/shoppingnt/moassets/css/swiper.css',
        'https://trnservice2025-stack.github.io/shoppingnt/moassets/css/content.css'
      ]
    : [
        'https://trnservice2025-stack.github.io/shoppingnt/assets/css/common.css',
        'https://trnservice2025-stack.github.io/shoppingnt/assets/css/swiper.css',
        'https://trnservice2025-stack.github.io/shoppingnt/assets/css/content.css'
      ];

  const js = t => t === 'm'
    ? 'https://trnservice2025-stack.github.io/shoppingnt/moassets/js/swiper.min.js'
    : 'https://trnservice2025-stack.github.io/shoppingnt/assets/js/swiper.min.js';

  const rmCSS = () =>
    document.querySelectorAll(`link[${CSS_ATTR}]`).forEach(e => e.remove());

  const addCSS = t =>
    css(t).forEach(h => {
      const l = document.createElement('link');
      l.rel = 'stylesheet';
      l.href = h;
      l.setAttribute(CSS_ATTR, '');
      document.head.appendChild(l);
    });

  const rmJS = () => {
    document.getElementById(JS_ID)?.remove();
    delete window.Swiper;
  };

  const addJS = (t, cb) => {
    const s = document.createElement('script');
    s.id = JS_ID;
    s.src = js(t);
    s.onload = cb;
    document.body.appendChild(s);
  };

  const killSwiper = () =>
    swipers.forEach(sw => sw.destroy(true, true)) || (swipers = []);

  const initSwiper = () =>
    window.Swiper &&
    document.querySelectorAll('.swiper')
      .forEach(el => swipers.push(new Swiper(el)));

  const apply = () => {
  const t = device();
  if (t === type) return;

  // 👉 브레이크포인트를 넘은 경우: 새로고침
  if (type !== undefined) {
    location.reload();
    return;
  }

  type = t;

  killSwiper();
  rmCSS(); rmJS();
  addCSS(t);
  addJS(t, () => setTimeout(initSwiper, 30));
};

  apply();
  addEventListener('resize', () => setTimeout(apply, 150));
})();