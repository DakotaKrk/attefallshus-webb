# Bygger undersidorna. Kor: python _sidor.py
import _bygg as B

MODELLFILTER = '''
      (function () {
        var grid = document.querySelector('.model-grid');
        var filter = document.querySelector('.filter');
        if (!grid || !filter) return;

        var kort = Array.prototype.slice.call(grid.querySelectorAll('.model-card'));
        var raknare = document.querySelector('.category__count');
        var tomt = document.createElement('p');
        tomt.className = 'model-grid__tomt';
        tomt.hidden = true;
        tomt.textContent = 'Ingen modell i det spannet ännu. Prova ett annat, eller hör av dig så letar vi tillsammans.';
        grid.appendChild(tomt);

        function filtrera(min, max) {
          var kvar = 0;
          kort.forEach(function (k) {
            var yta = parseInt(k.getAttribute('data-yta'), 10);
            var med = isNaN(yta) || (yta >= min && yta <= max);
            k.hidden = !med;
            if (med) kvar++;
          });
          tomt.hidden = kvar > 0;
          if (raknare) raknare.textContent = kvar === 1 ? '1 modell' : kvar + ' modeller';
        }

        filter.addEventListener('click', function (e) {
          var knapp = e.target.closest('button');
          if (!knapp) return;
          filter.querySelectorAll('button').forEach(function (b) {
            b.setAttribute('aria-pressed', String(b === knapp));
          });
          filtrera(parseInt(knapp.dataset.min, 10) || 0,
                   parseInt(knapp.dataset.max, 10) || 99999);
        });
      })();
'''

KONTAKT_SEKTION = open("_kontaktsektion.inc", encoding="utf-8").read()


def hero(bild, rubrik, meta, alt):
    return f'''      <section class="subpage-hero">
        <img class="subpage-hero__image" src="images/{bild}" width="1600" height="900" fetchpriority="high" decoding="async" alt="{alt}">

        <div class="subpage-hero__content-wrap">
          <div class="subpage-hero__content">
            <h1 class="subpage-hero__title">{rubrik}</h1>
            <p class="subpage-hero__meta">{meta}</p>
          </div>
        </div>
      </section>
'''


def kategorisida(fil, namn, herobild, meta, rubrik, ingress, modeller, spann):
    guidelank = ('\n          <p class="category__guide">'
                 '<a href="attefallshus-regler.html">Reglerna för attefallshus ändrades i december 2025 — så fungerar de nu</a></p>'
                 ) if fil == 'attefallshus.html' else ''
    piller = "\n".join(
        f'          <a href="{f}"{" aria-current=\"page\"" if n == namn else ""}>{n}</a>'
        for n, f in B.KATEGORIER)

    knappar = "\n".join(
        f'          <button type="button" data-min="{a}" data-max="{b}"'
        f'{" aria-pressed=\"true\"" if i == 0 else " aria-pressed=\"false\""}>{txt}</button>'
        for i, (txt, a, b) in enumerate(spann))

    kort = "\n".join(f'''          <article class="model-card" data-yta="{yta}" data-rum="{rum}">
            <a class="model-card__media" href="huskort.html">
              <img src="images/{bild}" loading="lazy" decoding="async" alt="{titel}, {namn.lower()} i svensk natur">
              <span class="model-card__pill" aria-hidden="true">Se huskortet</span>
            </a>
            <div class="model-card__rad">
              <h3 class="model-card__title"><a href="huskort.html">{titel}</a></h3>
              <p class="model-card__yta">{yta}<span>m²</span></p>
            </div>
            <p class="model-card__facts"><span>{rum} rum</span><span>Leverans {lev} v</span></p>
            <p class="model-card__price">Från X kr</p>
          </article>''' for titel, bild, yta, rum, lev in modeller)

    kropp = f'''    <main id="innehall">
{hero(herobild, namn, meta, namn + " i svensk natur")}
      <section class="category">
        <div class="category__inner">
          <nav class="category-filter" aria-label="Huskategorier">
{piller}
          </nav>

          <div class="category__head">
            <h2>{rubrik}</h2>
            <p class="category__ingress">{ingress}</p>{guidelank}
            <p class="category__count">{len(modeller)} modeller</p>
          </div>

          <div class="filter" role="group" aria-label="Filtrera på boyta">
            <p class="filter__etikett">Boyta</p>
{knappar}
          </div>

          <div class="model-grid">
{kort}
          </div>

          <p class="category__prisrad">
            Priserna sätts i offert efter din tomt.
            <a href="priser.html">Så sätts priset</a>
          </p>
        </div>
      </section>

{KONTAKT_SEKTION}    </main>

'''
    ut = (B.head(f"{namn} | Idealhus",
                 f"{namn} från Idealhus. {ingress}", herobild, fil=fil)
          + "\n" + B.header("Våra hus") + "\n" + kropp + B.SIDFOT + "\n"
          + B.skript(MODELLFILTER))
    open(fil, "w", encoding="utf-8", newline="").write(ut.replace("\n", "\r\n"))
    return fil


SPANN = [("Alla", 0, 99999), ("Under 30 m²", 0, 29), ("30–60 m²", 30, 60), ("Över 60 m²", 61, 99999)]

sidor = []

sidor.append(kategorisida(
    "fritidshus.html", "Fritidshus", "generated-category-fritidshus-wide-01.webp",
    "För helger och långa somrar · från X m²",
    "Modeller för fritidsboende",
    "Fritidshus ger mer plats på tomten än ett attefallshus och kräver bygglov. Här samlar vi modellerna som är gjorda för att bo i över helger, lov och långa somrar.",
    [("Huskort 1", "generated-category-fritidshus-card.webp", 45, 2, 12),
     ("Huskort 2", "generated-house-forest-01.webp", 55, 3, 14),
     ("Huskort 3", "generated-house-coast-01.webp", 62, 3, 14),
     ("Huskort 4", "generated-house-garden-01.webp", 70, 4, 16),
     ("Huskort 5", "generated-house-meadow-01.webp", 78, 4, 16),
     ("Huskort 6", "generated-house-gabled-01.webp", 85, 4, 18)], SPANN))

sidor.append(kategorisida(
    "fjallstugor.html", "Fjällstugor", "generated-category-fjallstuga-wide-01.webp",
    "Byggda för snölast och kalla vintrar · från X m²",
    "Modeller för fjällmiljö",
    "Fjällstugor byggs för hårdare klimat: snölast, vind och stora temperaturskillnader. Konstruktionen och isoleringen skiljer sig därför från våra övriga modeller.",
    [("Huskort 1", "generated-category-fjallstuga-card.webp", 38, 2, 14),
     ("Huskort 2", "generated-house-winter-01.webp", 48, 2, 14),
     ("Huskort 3", "generated-category-fjallstuga-01.webp", 56, 3, 16),
     ("Huskort 4", "generated-house-forest-01.webp", 64, 3, 16),
     ("Huskort 5", "generated-house-gabled-01.webp", 72, 4, 18),
     ("Huskort 6", "generated-house-coast-01.webp", 80, 4, 18)], SPANN))

sidor.append(kategorisida(
    "villor.html", "Villor", "generated-house-meadow-01.webp",
    "Permanentboende med full planlösning · från X m²",
    "Modeller för permanentboende",
    "Villorna är ritade för att bo i året om. Full planlösning, plats för hela hushållet och de tekniska krav som ställs på ett permanentbostadshus.",
    [("Huskort 1", "generated-house-gabled-01.webp", 95, 4, 20),
     ("Huskort 2", "generated-house-garden-01.webp", 110, 5, 20),
     ("Huskort 3", "generated-house-meadow-01.webp", 125, 5, 22),
     ("Huskort 4", "generated-house-coast-01.webp", 140, 6, 22),
     ("Huskort 5", "generated-house-forest-01.webp", 155, 6, 24),
     ("Huskort 6", "generated-house-winter-01.webp", 170, 7, 24)], SPANN))

sidor.append(kategorisida(
    "attefallshus.html", "Attefallshus", "generated-category-attefallshus-wide-01.webp",
    "Bygglovsbefriat · upp till 30 m² · gästhus, kontor eller uthyrning",
    "Modeller i attefallsstorlek",
    "Sedan december 2025 krävs varken bygglov eller anmälan för själva byggnaden inom måtten — men installationer som vatten och avlopp anmäls fortfarande. Det gör dem till den snabbaste vägen till ett extra hus på tomten.",
    [("Huskort 1", "generated-category-attefallshus-card.webp", 25, 1, 10),
     ("Huskort 2", "generated-house-forest-01.webp", 27, 2, 10),
     ("Huskort 3", "generated-house-coast-01.webp", 28, 2, 12),
     ("Huskort 4", "generated-house-garden-01.webp", 30, 2, 12),
     ("Huskort 5", "generated-category-attefallshus-02.webp", 30, 2, 14),
     ("Huskort 6", "generated-house-winter-01.webp", 30, 3, 14)], SPANN))

print("\n".join(sidor))
