# Bygger referensprojekt.html. Kor: python _referens.py
import _bygg as B

# (bild, plats, kategori, kort text, alt)
PROJEKT = [
    ("generated-house-coast-01.webp", "Stockholms skärgård", "Attefallshus",
     "Placerat på berget med hela glaspartiet mot vattnet. Altanen följer "
     "bergets lutning i stället för att bygga bort den.",
     "Litet hus vid svenska klippor och vatten"),
    ("generated-house-winter-01.webp", "Fjällen", "Fjällstuga",
     "Byggd för snölast och kalla vintrar. Taket och isoleringen skiljer sig "
     "från våra övriga modeller.",
     "Attefallshus i ljus svensk vintermiljö"),
    ("generated-house-forest-01.webp", "Tallskog", "Fritidshus",
     "Stora glaspartier mot skogen, mörk fasad som försvinner in i stammarna.",
     "Modernt hus med glasparti i svensk tallskog"),
    ("generated-house-garden-01.webp", "Villaträdgård", "Attefallshus",
     "Gästhus och kontor i samma byggnad, med egen uteplats bort från "
     "huvudbyggnaden.",
     "Kompakt gästhus med uteplats i trädgård"),
    ("generated-house-meadow-01.webp", "Öppet landskap", "Villa",
     "Permanentboende i öppet läge. Byggnadens riktning styrs av var solen "
     "står på eftermiddagen.",
     "Villa i öppet landskap"),
    ("generated-house-gabled-01.webp", "Inlandet", "Villa",
     "Sadeltak och traditionell form, med planlösning och teknik från våra "
     "nyare modeller.",
     "Villa med sadeltak i svensk trädgårdsmiljö"),
    ("generated-interior-01.webp", "Interiör", "Attefallshus",
     "Trettio kvadratmeter som rymmer sovplats, arbetsplats och matplats utan "
     "att kännas trångt.",
     "Ljus interiör i ett litet hus med smart planering"),
]

kort = "\n".join(f'''          <article class="referens">
            <div class="referens__media">
              <img src="images/{bild}" loading="lazy" decoding="async" alt="{alt}">
            </div>
            <div class="referens__text">
              <p class="referens__kategori">{kategori}</p>
              <h3>{plats}</h3>
              <p>{text}</p>
            </div>
          </article>''' for bild, plats, kategori, text, alt in PROJEKT)

KROPP = f'''    <main>
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
             "generated-house-coast-01.webp")
      + "\n" + B.header("Referensprojekt") + "\n" + KROPP + B.SIDFOT + "\n" + B.skript())

open("referensprojekt.html", "w", encoding="utf-8", newline="").write(ut.replace("\n", "\r\n"))
print("referensprojekt.html")
