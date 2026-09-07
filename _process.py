# Bygger sa-fungerar-det.html. Kor: python _process.py
import _bygg as B

# (rubrik, vem, klass, text)
STEG = [
    ("Första samtalet", "Tillsammans", "bada",
     "Du berättar om tomten, hur huset ska användas och ungefär när du vill "
     "vara i gång. Vi säger vad som är möjligt och vad som inte är det. "
     "Kostar ingenting och förpliktigar inte till något."),
    ("Modell och anpassning", "Tillsammans", "bada",
     "Vi går igenom modellerna och gör de anpassningar som betyder något för "
     "just din plats. Du får en offert där det står vad som ingår och vad som "
     "tillkommer."),
    ("Bygglov eller anmälan", "Du lämnar in", "du",
     "Attefallshus kräver anmälan, övriga hus bygglov. Vi tar fram ritningar "
     "och underlag, men det är du som är byggherre och lämnar in till din "
     "kommun. Handläggningstiden varierar mellan kommuner."),
    ("Tillverkning", "Vi", "vi",
     "Huset byggs i Sverige, under tak. Väggar, golv och tak monteras i jämn "
     "temperatur och fuktnivå i stället för ute i väder och vind. Du får veta "
     "var i processen huset befinner sig."),
    ("Grund och anslutningar", "Du ordnar", "du",
     "Grunden ska vara gjuten och el, vatten och avlopp framdragna innan huset "
     "kommer. Vi säger vad som krävs och när det ska vara klart, så att inget "
     "står och väntar på varandra."),
    ("Leverans och montage", "Vi", "vi",
     "Huset transporteras till tomten och monteras. Framkomlighet för lastbil "
     "och kranbil är det vanligaste som behöver lösas i förväg."),
    ("Slutbesiktning", "Tillsammans", "bada",
     "Genomgång av huset, punktlista på det som ska rättas, och överlämning. "
     "Du har haft samma kontakt hela vägen och vet vem du ringer."),
]

steg = "\n".join(f'''            <li class="stegspar__rad">
              <span class="stegspar__nr">{i:02d}</span>
              <div class="stegspar__kort">
                <div class="stegspar__topp">
                  <h3>{rubrik}</h3>
                  <span class="process__vem process__vem--{klass}">{vem}</span>
                </div>
                <p>{text}</p>
              </div>
            </li>''' for i, (rubrik, vem, klass, text) in enumerate(STEG, 1))

KROPP = f'''    <main id="innehall">
      <section class="subpage-hero">
        <img class="subpage-hero__image" src="images/generated-craft-cladding-01.webp" width="1600" height="900" fetchpriority="high" decoding="async" alt="Händer som arbetar med träpanel i verkstad">

        <div class="subpage-hero__content-wrap">
          <div class="subpage-hero__content">
            <h1 class="subpage-hero__title">Så fungerar det</h1>
            <p class="subpage-hero__meta">Från första samtalet till inflyttning</p>
          </div>
        </div>
      </section>

      <section class="kontakt-topp">
        <div>
          <h2>Sju steg, <em>i ordning</em>.</h2>
          <p class="kontakt-topp__lead">
            Ordningen spelar roll. Du kan inte bygga innan bygglovet är klart,
            och vi kan inte tillverka innan modellen är bestämd.
          </p>
          <p class="kontakt-topp__brod">
            Vi har markerat vem som gör vad i varje steg, för det är den fråga
            de flesta faktiskt har. En del ligger på oss, en del på dig, och en
            del gör vi tillsammans. Ingenting av det ska komma som en
            överraskning halvvägs in.
          </p>
        </div>

        <div class="kontakt-direkt">
          <div class="kontakt-direkt__rad">
            <span class="kontakt-direkt__namn">Anmälan</span>
            <span class="kontakt-direkt__roll">Attefallshus</span>
            <span class="kontakt-direkt__lankar">
              <a href="attefallshus.html">Upp till 30 m², inget bygglov</a>
            </span>
          </div>

          <div class="kontakt-direkt__rad">
            <span class="kontakt-direkt__namn">Bygglov</span>
            <span class="kontakt-direkt__roll">Övriga hus</span>
            <span class="kontakt-direkt__lankar">
              <a href="villor.html">Fritidshus, fjällstugor och villor</a>
            </span>
          </div>

          <div class="kontakt-direkt__rad">
            <span class="kontakt-direkt__namn">En kontakt</span>
            <span class="kontakt-direkt__roll">Hela vägen</span>
            <span class="kontakt-direkt__lankar">
              <a href="kontakt.html">Ahmed eller Sahand</a>
            </span>
          </div>
        </div>
      </section>

      <section class="process process--spar">
        <div class="process__grid">
          <div class="process__rail">
            <p class="section-label">Steg för steg</p>
            <p class="process__rail-text">
              Färgen visar vem som håller i steget. Ordningen är densamma
              oavsett vilket hus det gäller.
            </p>

            <div class="process__matare" aria-hidden="true"><span></span></div>

            <ul class="process__legend">
              <li><span class="prick prick--vi"></span>Vi gör det</li>
              <li><span class="prick prick--du"></span>Du gör det</li>
              <li><span class="prick prick--bada"></span>Tillsammans</li>
            </ul>
          </div>

          <ol class="stegspar">
{steg}
          </ol>
        </div>
      </section>

      <section class="segment">
        <article class="segment__block">
          <div>
            <h2>Under tak, inte under presenning</h2>
            <p>
              Ett hus som byggs utomhus möter regn, kyla och fukt medan det
              växer fram. Våra hus byggs inomhus, i jämn temperatur, och kommer
              färdiga till tomten. Det är därför montaget tar dagar i stället
              för månader.
            </p>
            <p>
              Det ger också jämnare kvalitet mellan husen. Samma modell blir
              samma hus, oavsett vilken vecka på året det tillverkades.
            </p>
            <a class="model-price__button" href="proffs.html">Se produktionen</a>
          </div>
          <div class="segment__media">
            <img src="images/generated-production-yard-01.webp" loading="lazy" decoding="async" alt="Svensk produktionsmiljö med attefallshus och trävirke">
          </div>
        </article>
      </section>

''' + open("_kontaktsektion.inc", encoding="utf-8").read() + '''    </main>

'''

ut = (B.head("Så fungerar det | Idealhus",
             "Från första samtalet till inflyttning. Sju steg, och vem som gör "
             "vad i varje steg.",
             "generated-craft-cladding-01.webp", fil="sa-fungerar-det.html")
      + "\n" + B.header("Så fungerar det") + "\n" + KROPP + B.SIDFOT + "\n" + B.skript())

open("sa-fungerar-det.html", "w", encoding="utf-8", newline="").write(ut.replace("\n", "\r\n"))
print("sa-fungerar-det.html")
