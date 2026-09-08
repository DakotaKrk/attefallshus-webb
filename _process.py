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

TECKNINGAR = ['<svg viewBox="0 0 320 150" aria-hidden="true" focusable="false">\n          <!-- Ritningen pa bordet -->\n          <rect class="linje" x="54" y="26" width="176" height="106" rx="5"/>\n          <path class="linje" d="M78 52h128v56H78z"/>\n          <path class="linje" d="M142 52v56M142 82h64"/>\n          <path class="hartunn" d="M78 68h26M170 52v12M78 118h60"/>\n          <!-- Pennan -->\n          <g class="skede__penna">\n            <path class="accentfyll" d="M232 108l44-44 13 13-44 44-19 6z"/>\n            <path class="linje" d="M226 127l19-6"/>\n          </g>\n        </svg>', '<svg viewBox="0 0 320 150" aria-hidden="true" focusable="false">\n          <!-- Taket over verkstaden -->\n          <path class="linje" d="M20 56L160 14l140 42"/>\n          <path class="hartunn" d="M26 56v76M294 56v76M20 132h280"/>\n          <!-- Huset som byggs, tydligt innanfor -->\n          <path class="linje" d="M102 128V90l58-24 58 24v38"/>\n          <path class="hartunn" d="M130 128v-30M160 128V88M190 128v-30"/>\n          <!-- Grunden -->\n          <path class="accentlinje" d="M88 128h144"/>\n        </svg>', '<svg viewBox="0 0 320 150" aria-hidden="true" focusable="false">\n          <!-- Huset -->\n          <path class="linje" d="M96 132V80l64-30 64 30v52"/>\n          <path class="linje" d="M142 132v-32h36v32"/>\n          <path class="hartunn" d="M196 68V48h13v26"/>\n          <!-- Roken kommer nar man pekar pa kortet -->\n          <path class="rok accentlinje" d="M202 40c7-7 0-14 7-21"/>\n          <!-- Mark -->\n          <path class="linje" d="M22 132h276"/>\n          <!-- Granar -->\n          <path class="hartunn" d="M52 132v-30M38 106l14-20 14 20M42 118l10-14 10 14"/>\n          <path class="hartunn" d="M270 132v-22M259 114l11-16 11 16"/>\n        </svg>']

FASER = [('Innan bygget', (1, 3), 'Vi ritar, räknar och tar fram underlaget. Du är byggherre och lämnar in till kommunen — vi säger vad som ska med.'), ('Medan huset byggs', (4, 5), 'Huset växer fram inomhus, i jämn temperatur. Under tiden ska marken vara redo när det kommer.'), ('På plats', (6, 7), 'Huset kommer på lastbil och monteras. Sedan går vi igenom det tillsammans, rum för rum.')]


def fas(namn, spann, ingress, teckning, steg):
    kort = "\n".join(f'''            <li class="fassteg__kort">
              <span class="fassteg__nr">{i:02d}</span>
              <div class="fassteg__kropp">
                <div class="fassteg__topp">
                  <h3>{rubrik}</h3>
                  <span class="process__vem process__vem--{klass}">{vem}</span>
                </div>
                <p>{text}</p>
              </div>
            </li>''' for i, (rubrik, vem, klass, text) in steg)

    return f'''        <section class="fas">
          <div class="fas__huvud">
            <span class="fas__bild">
{teckning}
            </span>

            <div>
              <p class="fas__spann">Steg {spann[0]:02d}–{spann[1]:02d}</p>
              <h2 class="fas__titel">{namn}</h2>
              <p class="fas__text">{ingress}</p>
            </div>
          </div>

          <ol class="fassteg">
{kort}
          </ol>
        </section>'''


faser = "\n\n".join(
    fas(namn, spann, ingress, TECKNINGAR[n],
        [(i, STEG[i - 1]) for i in range(spann[0], spann[1] + 1)])
    for n, (namn, spann, ingress) in enumerate(FASER))

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

      <section class="process process--faser">
        <div class="process__inre">
          <p class="process__teckenforklaring">
            <span><i class="prick prick--vi"></i>Vi gör det</span>
            <span><i class="prick prick--du"></i>Du gör det</span>
            <span><i class="prick prick--bada"></i>Tillsammans</span>
          </p>

{faser}
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
