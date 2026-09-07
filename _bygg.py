# Genererar undersidorna ur en gemensam mall, sa header, meny och sidfot
# ar identiska pa alla sidor. Kors om nar mallen andras.
import re, io, os

CSS_V = "20260908w"

KATEGORIER = [
    ("Attefallshus", "attefallshus.html"),
    ("Fritidshus", "fritidshus.html"),
    ("Fjällstugor", "fjallstugor.html"),
    ("Villor", "villor.html"),
    ("Proffs", "proffs.html"),
]

# Bild och en rad om varje kategori. En rullgardin med bara namn
# tvingar besokaren att gissa vad skillnaden ar.
KATEGORI_INFO = {
    "Attefallshus": ("generated-category-attefallshus-card.webp",
                     "Upp till 30 m², utan bygglov"),
    "Fritidshus": ("generated-category-fritidshus-card.webp",
                   "För helger och långa somrar"),
    "Fjällstugor": ("generated-category-fjallstuga-card.webp",
                    "Byggda för snölast och kyla"),
    "Villor": ("generated-house-gabled-01.webp",
               "Permanentboende, full planlösning"),
    "Proffs": ("generated-production-yard-01.webp",
               "Väggar, block och moduler"),
}

MENY = [
    ("Hem", "index.html"),
    ("__DROPDOWN__", None),
    ("Så fungerar det", "sa-fungerar-det.html"),
    ("Referensprojekt", "referensprojekt.html"),
    ("Om oss", "om-oss.html"),
    ("Kontakt", "kontakt.html"),
]


def dropdown(aktiv):
    rader = []
    for namn, fil in KATEGORIER:
        bild, text = KATEGORI_INFO[namn]
        rader.append(
            f'              <a href="{fil}">\n'
            f'                <img src="images/{bild}" alt="" loading="lazy" decoding="async">\n'
            f'                <span>\n'
            f'                  <strong>{namn}</strong>\n'
            f'                  <em>{text}</em>\n'
            f'                </span>\n'
            f'              </a>')
    rader.append('              <a class="main-nav__sub-alla" '
                 'href="attefallshus.html">Se alla modeller</a>')
    val = "\n".join(rader)
    klass = "main-nav__link main-nav__toggle"
    if aktiv == "Våra hus":
        klass = "main-nav__link main-nav__link--active main-nav__toggle"
    return (f'          <div class="main-nav__item" data-dropdown>\n'
            f'            <button class="{klass}" type="button" aria-expanded="false" '
            f'aria-controls="undermeny-hus">Våra hus<span class="main-nav__pil" aria-hidden="true"></span></button>\n'
            f'            <div class="main-nav__sub" id="undermeny-hus">\n{val}\n'
            f'            </div>\n          </div>')


def huvudmeny(aktiv):
    rader = []
    for namn, fil in MENY:
        if namn == "__DROPDOWN__":
            rader.append(dropdown(aktiv))
            continue
        k = "main-nav__link main-nav__link--active" if namn == aktiv else "main-nav__link"
        rader.append(f'          <a class="{k}" href="{fil}">{namn}</a>')
    return "\n".join(rader)


def mobilmeny():
    val = "\n".join(f'          <a href="{fil}">{namn}</a>' for namn, fil in KATEGORIER)
    rader = []
    for namn, fil in MENY:
        if namn == "__DROPDOWN__":
            rader.append('        <div class="mobile-nav__grupp">\n'
                         '          <span>Våra hus</span>\n' + val + '\n        </div>')
            continue
        rader.append(f'        <a href="{fil}">{namn}</a>')
    return "\n".join(rader)


def head(titel, beskrivning, forladdad=None):
    pre = f'\n    <link rel="preload" as="image" href="images/{forladdad}" fetchpriority="high">' if forladdad else ""
    return f'''<!doctype html>
<html lang="sv">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titel}</title>
    <meta name="description" content="{beskrivning}">
    <meta name="theme-color" content="#262c27">
    <link rel="icon" href="images/idealhus.svg" type="image/svg+xml">

    <meta property="og:type" content="website">
    <meta property="og:locale" content="sv_SE">
    <meta property="og:site_name" content="Idealhus">
    <meta property="og:title" content="{titel}">
    <meta property="og:description" content="{beskrivning}">
    <meta name="twitter:card" content="summary_large_image">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&family=Schibsted+Grotesk:wght@400;500;600&display=swap">{pre}
    <link rel="stylesheet" href="styles.css?v={CSS_V}">
  </head>
  <body>'''


def header(aktiv):
    return f'''    <header class="site-header">
      <div class="site-header__inner">
        <a class="logo" href="index.html" aria-label="Till Idealhus startsida">
          <img class="logo__svg" src="images/idealhus_logo.svg" width="1024" height="279" alt="Idealhus">
        </a>

        <nav class="main-nav" aria-label="Huvudmeny">
{huvudmeny(aktiv)}
        </nav>

        <div class="site-header__actions">
          <a class="header-button" href="kontakt.html">Begär offert</a>

          <button class="menu-button" type="button" aria-label="Öppna meny" aria-expanded="false" aria-controls="mobile-nav">
            <span class="menu-button__line"></span>
            <span class="menu-button__line"></span>
            <span class="menu-button__line"></span>
          </button>
        </div>
      </div>

      <nav class="mobile-nav" id="mobile-nav" aria-label="Meny" hidden>
{mobilmeny()}
        <a class="mobile-nav__cta" href="kontakt.html">Begär offert</a>
      </nav>
    </header>
'''


SIDFOT = '''    <footer class="site-footer">
      <div class="site-footer__inner">
        <div>
          <img class="site-footer__logo" src="images/idealhus_logo.svg" width="1024" height="279" loading="lazy" decoding="async" alt="Idealhus">
          <p class="site-footer__text">
            Attefallshus &amp; komplementhus med skandinavisk design och hög kvalitet.
          </p>
          <div class="site-footer__social">
            <a href="#" aria-label="Idealhus på Facebook" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false">
                <path d="M13.4 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.25-1.45 1.55-1.45h1.65V3.68c-.29-.04-1.27-.13-2.42-.13-2.4 0-4.03 1.46-4.03 4.15v2.2H7.45V13h2.7v8h3.25z"/>
              </svg>
            </a>
            <a href="#" aria-label="Idealhus på Instagram" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" focusable="false">
                <rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/>
                <circle cx="12" cy="12" r="3.9"/>
                <circle cx="17.1" cy="6.9" r="1.1" fill="currentColor" stroke="none"/>
              </svg>
            </a>
          </div>
        </div>

        <div>
          <h3 class="site-footer__heading">Navigation</h3>
          <nav class="site-footer__nav" aria-label="Sidfot navigation">
            <a href="index.html">Hem</a>
            <a href="attefallshus.html">Våra hus</a>
            <a href="sa-fungerar-det.html">Så fungerar det</a>
            <a href="referensprojekt.html">Referensprojekt</a>
            <a href="om-oss.html">Om oss</a>
            <a href="kontakt.html">Kontakt</a>
          </nav>
        </div>

        <div>
          <h3 class="site-footer__heading">Våra hus</h3>
          <nav class="site-footer__nav" aria-label="Sidfot husmodeller">
''' + "\n".join(f'            <a href="{fil}">{namn}</a>' for namn, fil in KATEGORIER) + '''
          </nav>
        </div>

        <div>
          <h3 class="site-footer__heading">Kontakta oss</h3>
          <p class="site-footer__text">
            <a href="mailto:ahmed@idealhus.se">ahmed@idealhus.se</a><br>
            <a href="mailto:sahand@idealhus.se">sahand@idealhus.se</a><br>
            <a href="tel:+46701234567">070-123 45 67</a><br>
            Stockholm, Sverige
          </p>
          <a class="site-footer__button" href="kontakt.html">Boka rådgivning</a>
        </div>
      </div>

      <div class="site-footer__bottom">
        <span>© 2026 Idealhus AB. Alla rättigheter förbehållna.</span>
      </div>
    </footer>
'''


def skript(extra=""):
    return '''    <script>
      (function () {
        var item = document.querySelector('[data-dropdown]');
        if (!item) return;
        var knapp = item.querySelector('.main-nav__toggle');
        var stangTimer;
        function satt(oppen) {
          item.classList.toggle('main-nav__item--open', oppen);
          knapp.setAttribute('aria-expanded', String(oppen));
        }
        knapp.addEventListener('click', function () {
          satt(!item.classList.contains('main-nav__item--open'));
        });
        item.addEventListener('mouseenter', function () {
          window.clearTimeout(stangTimer);
          if (window.matchMedia('(hover: hover)').matches) satt(true);
        });
        item.addEventListener('mouseleave', function () {
          if (!window.matchMedia('(hover: hover)').matches) return;
          stangTimer = window.setTimeout(function () { satt(false); }, 160);
        });
        document.addEventListener('keydown', function (e) {
          if (e.key === 'Escape' && item.classList.contains('main-nav__item--open')) {
            satt(false); knapp.focus();
          }
        });
        document.addEventListener('click', function (e) {
          if (!item.contains(e.target)) satt(false);
        });
      })();

      (function () {
        var knapp = document.querySelector('.menu-button');
        var panel = document.getElementById('mobile-nav');
        if (!knapp || !panel) return;
        knapp.addEventListener('click', function () {
          var oppen = knapp.getAttribute('aria-expanded') === 'true';
          knapp.setAttribute('aria-expanded', String(!oppen));
          knapp.setAttribute('aria-label', oppen ? 'Öppna meny' : 'Stäng meny');
          knapp.classList.toggle('menu-button--open', !oppen);
          panel.hidden = oppen;
        });
      })();

      (function () {
        if (!window.IntersectionObserver) return;
        var valjare = ['.subpage-hero__content', '.category-filter', '.filter', '.category__head',
          '.model-card', '.process__head', '.process__lista li', '.team-kort',
          '.galleri figure', '.segment__block', '.contact-page-hero__inner',
          '.contact-person', '.textsida > *', '.contact-section__intro', '.contact-form'].join(',');
        var element = Array.prototype.slice.call(document.querySelectorAll(valjare));
        if (!element.length) return;
        document.documentElement.classList.add('js-reveal');
        var raknare = new Map();
        element.forEach(function (el) {
          el.classList.add('reveal');
          var f = el.parentElement;
          var i = raknare.get(f) || 0;
          raknare.set(f, i + 1);
          if (i) el.style.setProperty('--reveal-delay', (i * 0.06).toFixed(2) + 's');
        });
        element.forEach(function (el) {
          if (el.getBoundingClientRect().top < window.innerHeight) {
            el.style.setProperty('--reveal-delay', '0s');
            el.classList.add('reveal--inne');
          }
        });
        var obs = new IntersectionObserver(function (poster) {
          poster.forEach(function (p) {
            if (!p.isIntersecting) return;
            p.target.classList.add('reveal--inne');
            obs.unobserve(p.target);
          });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
        element.forEach(function (el) { obs.observe(el); });
        var vantar = false;
        window.addEventListener('scroll', function () {
          if (vantar) return;
          vantar = true;
          window.requestAnimationFrame(function () {
            vantar = false;
            for (var i = element.length - 1; i >= 0; i--) {
              var el = element[i];
              if (el.classList.contains('reveal--inne')) continue;
              var r = el.getBoundingClientRect();
              if (r.top < window.innerHeight && r.bottom > 0) {
                el.classList.add('reveal--inne');
                obs.unobserve(el);
              }
            }
          });
        }, { passive: true });
      })();

      (function () {
        var rad = document.querySelector('.category-filter');
        if (!rad) return;
        function uppdatera() {
          var mer = rad.scrollWidth - rad.clientWidth - rad.scrollLeft > 8;
          rad.classList.toggle('category-filter--mer', mer);
        }
        uppdatera();
        rad.addEventListener('scroll', uppdatera, { passive: true });
        window.addEventListener('resize', uppdatera);
      })();
''' + extra + '''    </script>
  </body>
</html>
'''
