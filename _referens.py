# Bygger referensprojekt.html. Kor: python _referens.py
import _bygg as B

# (bild, plats, kategori, styrde, text, alt, form)
#
# form styr rytmen i listan: "bred" och "vand" gar over hela bredden med
# bilden at var sitt hall, tomma strangen ligger i tvakolumnsrutnatet.
# Sju lika stora rutor blir en katalog - vaxlingen ger en lasordning.
PROJEKT = [
    ("generated-house-coast-01.webp", "Stockholms skärgård", "Attefallshus",
     "Berget, inte ritningen",
     "Huset är placerat på berget med hela glaspartiet mot vattnet. Altanen "
     "följer bergets lutning i stället för att bygga bort den, vilket sparade "
     "både sprängning och en meter höjd mot omgivningen.",
     "Litet hus vid svenska klippor och vatten", "bred"),

    ("generated-house-winter-01.webp", "Fjällen", "Fjällstuga",
     "Snölasten",
     "Byggd för snölast och kalla vintrar. Taket och isoleringen skiljer sig "
     "från våra övriga modeller, och entrén ligger i lä från den vanligaste "
     "vindriktningen.",
     "Attefallshus i ljus svensk vintermiljö", ""),

    ("generated-house-forest-01.webp", "Tallskog", "Fritidshus",
     "Ljuset mellan stammarna",
     "Stora glaspartier mot skogen och en mörk fasad som försvinner in i "
     "stammarna. Fönstersättningen följer var ljuset faktiskt når in mellan "
     "tallarna, inte fasadens symmetri.",
     "Modernt hus med glasparti i svensk tallskog", ""),

    ("generated-house-meadow-01.webp", "Öppet landskap", "Villa",
     "Eftermiddagssolen",
     "Permanentboende i öppet läge, där ingenting skuggar och allting syns. "
     "Byggnadens riktning styrs av var solen står på eftermiddagen, eftersom "
     "det är då rummen faktiskt används.",
     "Villa i öppet landskap", "vand"),

    ("generated-house-garden-01.webp", "Villaträdgård", "Attefallshus",
     "Avståndet till huvudbyggnaden",
     "Gästhus och kontor i samma byggnad, med egen uteplats vänd bort från "
     "huvudbyggnaden. Två funktioner som sällan används samtidigt får dela "
     "samma yta.",
     "Kompakt gästhus med uteplats i trädgård", ""),

    ("generated-house-gabled-01.webp", "Inlandet", "Villa",
     "Den befintliga bebyggelsen",
     "Sadeltak och traditionell form, med planlösning och teknik från våra "
     "nyare modeller. Huset skulle passa in på gatan utan att se ut som en "
     "kopia av grannarna.",
     "Villa med sadeltak i svensk trädgårdsmiljö", ""),

    ("generated-interior-01.webp", "Interiör", "Attefallshus",
     "Var väggarna står",
     "Trettio kvadratmeter som rymmer sovplats, arbetsplats och matplats utan "
     "att kännas trångt. Det handlar mindre om antalet kvadratmeter och mer om "
     "vad man ser när man kommer in genom dörren.",
     "Ljus interiör i ett litet hus med smart planering", "bred"),
]

kort = "\n".join(f'''          <article class="referens{(" referens--" + form) if form else ""}">
            <div class="referens__media">
              <img src="images/{bild}" loading="lazy" decoding="async" alt="{alt}">
            </div>
            <div class="referens__text">
              <p class="referens__kategori">{kategori}</p>
              <h3>{plats}</h3>
              <p>{text}</p>
              <dl class="referens__styrde">
                <dt>Styrde formen</dt>
                <dd>{styrde}</dd>
              </dl>
            </div>
          </article>''' for bild, plats, kategori, styrde, text, alt, form in PROJEKT)

KROPP = f'''    <main id="innehall">
      <section class="subpage-hero">
        <img class="subpage-hero__image" src="images/generated-house-coast-01.webp" width="1600" height="900" fetchpriority="high" decoding="async" alt="Modernt hus på svenska klippor vid havet">

        <div class="subpage-hero__content-wrap">
          <div class="subpage-hero__content">
            <h1 class="subpage-hero__title">Referensprojekt</h1>
            <p class="subpage-hero__meta">Hus vi ritat och byggt</p>
          </div>
        </div>
      </section>

      <section class="kontakt-topp">
        <div>
          <h2>Samma modell, <em>olika hus</em>.</h2>
          <p class="kontakt-topp__lead">
            Platsen avgör mer än modellvalet. Väderstreck, lutning och utsikt
            gör att två hus av samma modell sällan blir lika.
          </p>
          <p class="kontakt-topp__brod">
            Här är ett urval. För varje projekt står vad som styrde besluten,
            eftersom det oftast är mer användbart än en bild utan sammanhang.
          </p>
        </div>

        <div class="kontakt-direkt">
          <div class="kontakt-direkt__rad">
            <span class="kontakt-direkt__namn">Skärgård</span>
            <span class="kontakt-direkt__roll">Berg och vatten</span>
            <span class="kontakt-direkt__lankar">
              <a href="attefallshus.html">Se attefallshusen</a>
            </span>
          </div>

          <div class="kontakt-direkt__rad">
            <span class="kontakt-direkt__namn">Fjäll</span>
            <span class="kontakt-direkt__roll">Snölast och kyla</span>
            <span class="kontakt-direkt__lankar">
              <a href="fjallstugor.html">Se fjällstugorna</a>
            </span>
          </div>

          <div class="kontakt-direkt__rad">
            <span class="kontakt-direkt__namn">Inland</span>
            <span class="kontakt-direkt__roll">Permanentboende</span>
            <span class="kontakt-direkt__lankar">
              <a href="villor.html">Se villorna</a>
            </span>
          </div>
        </div>
      </section>

      <section class="referens-lista">
        <div class="referens-lista__grid">
{kort}
        </div>
      </section>

''' + open("_kontaktsektion.inc", encoding="utf-8").read() + '''    </main>

'''

ut = (B.head("Referensprojekt | Idealhus",
             "Hus vi ritat och byggt. Se hur platsen styr besluten i varje projekt.",
             "generated-house-coast-01.webp", fil="referensprojekt.html")
      + "\n" + B.header("Referensprojekt") + "\n" + KROPP + B.SIDFOT + "\n" + B.skript())

open("referensprojekt.html", "w", encoding="utf-8", newline="").write(ut.replace("\n", "\r\n"))
print("referensprojekt.html")
