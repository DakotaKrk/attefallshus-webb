# Bygger undersidorna. Kor: python _sidor.py
import _bygg as B
import _modeller as M

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


def kategorisida(fil, namn, herobild, meta, rubrik, ingress, spann):
    modeller = M.modeller(fil)
    guidelank = ('\n          <p class="category__guide">'
                 '<a href="attefallshus-regler.html">Reglerna för attefallshus ändrades i december 2025: så fungerar de nu</a></p>'
                 ) if fil == 'attefallshus.html' else ''
    # Proffs skiljs av med en linje. Den som jamfor attefallshus mot
    # fritidshus jamfor inte utfackningsvaggar i samma rad.
    def pill(n, f):
        return f'          <a href="{f}"{" aria-current=\"page\"" if n == namn else ""}>{n}</a>'

    piller = "\n".join(
        [pill(n, f) for n, f in B.KATEGORIER_PRIVAT]
        + ['          <span class="category-filter__delare" aria-hidden="true"></span>']
        + [pill(n, f) for n, f in B.KATEGORIER_PROFFS])

    knappar = "\n".join(
        f'          <button type="button" data-min="{a}" data-max="{b}"'
        f'{" aria-pressed=\"true\"" if i == 0 else " aria-pressed=\"false\""}>{txt}</button>'
        for i, (txt, a, b) in enumerate(spann))

    # Varje kort barde tidigare till samma huskort.html utan parameter, sa
    # alla tjugofyra landade pa "Huskort 1". Adressen bar nu kategorin och
    # modellens nummer; huskortssidan slar upp resten i samma tabell.
    typ = M.slug(fil)
    kort = "\n".join(f'''          <article class="model-card" data-yta="{yta}" data-rum="{rum}">
            <a class="model-card__media" href="huskort.html?typ={typ}&amp;modell={i}">
              <img src="images/{bild}" loading="lazy" decoding="async" alt="{titel}, {namn.lower()} i svensk natur">
              <span class="model-card__pill" aria-hidden="true">Se huskortet</span>
            </a>
            <div class="model-card__rad">
              <h3 class="model-card__title"><a href="huskort.html?typ={typ}&amp;modell={i}">{titel}</a></h3>
              <p class="model-card__yta">{yta}<span>m²</span></p>
            </div>
            <p class="model-card__facts"><span>{rum} rum</span><span>Leverans {lev} v</span></p>
            <p class="model-card__price">Från X kr</p>
          </article>''' for i, (titel, bild, yta, rum, lev) in enumerate(modeller, 1))

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
    # Ingressen ar brodtext och blir 190-240 tecken i ett description-falt,
    # dar Google klipper vid ~160. Sidorna har darfor en egen kort text.
    kort_text = KORTA_BESKRIVNINGAR.get(fil, ingress)
    ut = (B.head(f"{namn} | Idealhus",
                 f"{namn} från Idealhus. {kort_text}", herobild, fil=fil)
          + "\n" + B.header("Våra hus") + "\n" + kropp + B.SIDFOT + "\n"
          + B.skript(MODELLFILTER))
    open(fil, "w", encoding="utf-8", newline="").write(ut.replace("\n", "\r\n"))
    return fil


KORTA_BESKRIVNINGAR = {
    "attefallshus.html":
        "Sedan december 2025 behövs varken bygglov eller anmälan för själva byggnaden – den snabbaste vägen till ett hus till på tomten.",
    "fritidshus.html":
        "Mer plats på tomten än ett attefallshus, byggda för att bo i över helger, lov och långa somrar. Kräver bygglov.",
    "fjallstugor.html":
        "Byggda för snölast, vind och stora temperaturskillnader – konstruktion och isolering anpassade för fjällklimat.",
    "villor.html":
        "Ritade för att bo i året om: full planlösning, plats för hela hushållet och kraven som ställs på ett permanentbostadshus.",
}

SPANN = [("Alla", 0, 99999), ("Under 30 m²", 0, 29), ("30–60 m²", 30, 60), ("Över 60 m²", 61, 99999)]

sidor = []

sidor.append(kategorisida(
    "fritidshus.html", "Fritidshus", "generated-category-fritidshus-wide-01.webp",
    "För helger och långa somrar · från X m²",
    "Modeller för fritidsboende",
    "Fritidshus ger mer plats på tomten än ett attefallshus och kräver bygglov. Här samlar vi modellerna som är gjorda för att bo i över helger, lov och långa somrar.",
    SPANN))

sidor.append(kategorisida(
    "fjallstugor.html", "Fjällstugor", "generated-category-fjallstuga-wide-01.webp",
    "Byggda för snölast och kalla vintrar · från X m²",
    "Modeller för fjällmiljö",
    "Fjällstugor byggs för hårdare klimat: snölast, vind och stora temperaturskillnader. Konstruktionen och isoleringen skiljer sig därför från våra övriga modeller.",
    SPANN))

sidor.append(kategorisida(
    "villor.html", "Villor", "generated-house-meadow-01.webp",
    "Permanentboende med full planlösning · från X m²",
    "Modeller för permanentboende",
    "Villorna är ritade för att bo i året om. Full planlösning, plats för hela hushållet och de tekniska krav som ställs på ett permanentbostadshus.",
    SPANN))

sidor.append(kategorisida(
    "attefallshus.html", "Attefallshus", "generated-category-attefallshus-wide-01.webp",
    "Bygglovsbefriat · upp till 30 m² · gästhus, kontor eller uthyrning",
    "Modeller i attefallsstorlek",
    "Sedan december 2025 krävs varken bygglov eller anmälan för själva byggnaden inom måtten, men installationer som vatten och avlopp anmäls fortfarande. Det gör dem till den snabbaste vägen till ett extra hus på tomten.",
    SPANN))

print("\n".join(sidor))
