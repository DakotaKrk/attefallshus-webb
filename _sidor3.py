# -*- coding: utf-8 -*-
# Bygger integritetspolicyn och attefallsguiden. Kor: python _sidor3.py
#
# Reglerna i guiden ar kontrollerade 2026-09-08 mot Nykopings kommun och
# Bygglov24, som bada beskriver andringen som tradde i kraft 1 december
# 2025: den sarskilda anmalningsplikten och startbeskedet for
# komplementbyggnader och komplementbostadshus ar slopade, och areorna
# skiljer sig nu inom och utanfor detaljplan. Skriv inte om siffrorna
# har utan att kontrollera dem igen - de andras.
import io

import _bygg as B

from _guidetext import GUIDE, TOC_SKRIPT, faq_json  # noqa: E402

POLICY = '''    <main id="innehall">
      <section class="guide-topp">
        <div class="guide-topp__inner">
          <p class="section-label">Uppdaterad 8 september 2026</p>
          <h1 class="guide-topp__titel">Integritetspolicy</h1>
          <p class="guide-topp__lead">
            Här står vad som händer med uppgifterna du lämnar när du hör av
            dig till oss. Kort sagt: de går direkt till oss, de lagras inte
            på webbplatsen, och vi lämnar dem inte vidare.
          </p>
        </div>
      </section>

      <section class="guide">
        <div class="guide__inner">
          <aside class="guide__snabbsvar">
            <p class="guide__snabbsvar-etikett">Kort svar</p>
            <p>
              Webbplatsen sätter inga kakor och samlar ingen statistik.
              Kontaktformuläret skickas med ditt eget e-postprogram, så
              uppgifterna passerar aldrig någon tredje part.
            </p>
          </aside>

          <div class="guide__text">
            <h2>Vem som ansvarar</h2>
            <p>
              Idealhus AB, organisationsnummer 559123-4567, Stockholm, är
              personuppgiftsansvarig för behandlingen som beskrivs här. Du når
              oss på <a href="mailto:ahmed@idealhus.se">ahmed@idealhus.se</a>
              eller <a href="mailto:sahand@idealhus.se">sahand@idealhus.se</a>.
            </p>

            <h2>Vilka uppgifter vi behandlar</h2>
            <p>
              Om du fyller i kontaktformuläret lämnar du namn, e-postadress
              och, om du vill, telefonnummer, ort, vilken husmodell du är
              intresserad av och det du skriver i meddelandet. Vi behandlar
              bara det du själv skriver.
            </p>

            <h2>Hur formuläret fungerar</h2>
            <p>
              Formuläret skickas inte via någon formulärtjänst. När du trycker
              på skicka öppnas ditt eget e-postprogram med meddelandet ifyllt,
              och du skickar det som ett vanligt mejl. Uppgifterna sparas
              alltså inte på webbplatsen och passerar ingen tredje part på
              vägen. De hamnar i vår inkorg, hos vår e-postleverantör.
            </p>

            <h2>Varför vi behandlar dem</h2>
            <p>
              För att kunna svara på din fråga och lämna offert. Den lagliga
              grunden är vårt berättigade intresse av att besvara den som
              kontaktar oss, och ditt samtycke när du kryssar i rutan i
              formuläret. Du kan när som helst höra av dig och be oss sluta.
            </p>

            <h2>Hur länge vi sparar dem</h2>
            <p>
              Förfrågningar sparas i 12 månader efter senaste kontakten,
              och därefter raderas de. Blir det ett avtal sparas de uppgifter
              som hör till affären så länge bokförings- och garantiregler
              kräver det.
            </p>

            <h2>Vilka som kan se uppgifterna</h2>
            <p>
              Vi lämnar inte ut uppgifter till någon annan för deras egna
              ändamål, och vi säljer dem inte vidare. Vår e-postleverantör
              behandlar dem åt oss som personuppgiftsbiträde.
            </p>

            <h2>Kakor och statistik</h2>
            <p>
              Webbplatsen använder inga kakor, sparar ingenting i din
              webbläsare och har inget verktyg för besöksstatistik. Därför
              finns här inte heller någon ruta om kakor att klicka bort.
            </p>

            <h2>Uppgifter som lämnar din webbläsare ändå</h2>
            <p>
              Två saker sker automatiskt när du besöker sidan, som vi vill att
              du ska känna till:
            </p>
            <ul class="guide__lista">
              <li>Webbplatsen ligger hos GitHub Pages. Din IP-adress syns i
                deras loggar, som alla webbservrar har.</li>
              <li>Typsnitten hämtas från Google Fonts, vilket innebär att din
                IP-adress skickas till Google när sidan laddas.</li>
            </ul>

            <h2>Dina rättigheter</h2>
            <p>
              Du har rätt att få veta vilka uppgifter vi har om dig, att få dem
              rättade eller raderade, att invända mot behandlingen och att
              begära att den begränsas. Hör av dig till någon av adresserna
              ovan, så ordnar vi det. Är du inte nöjd med hur vi hanterar
              saken kan du vända dig till Integritetsskyddsmyndigheten, IMY.
            </p>
          </div>
        </div>
      </section>
    </main>

'''



# ---------------------------------------------------------------------------
# Prissidan. FYLL I HÄR när priserna är satta - inget annat på sidan behöver
# röras. Skriv hela strängen, till exempel "Från 450 000 kr".
# ---------------------------------------------------------------------------
PRISER = [
    ("Attefallshus", "attefallshus.html", "15–30 m²", "Från X kr"),
    ("Fritidshus", "fritidshus.html", "40–120 m²", "Från X kr"),
    ("Fjällstugor", "fjallstugor.html", "38–80 m²", "Från X kr"),
    ("Villor", "villor.html", "95–170 m²", "Från X kr"),
]

INGAR = [
    ("Ritningar och underlag", "Det vi tar fram för att du ska kunna anmäla eller söka lov."),
    ("Själva huset", "Tillverkat i Sverige, under tak, med de material och den nivå ni kommit överens om."),
    ("Leverans till tomten", "Transport och lyft på plats, när framkomligheten är löst."),
    ("Montage", "Huset monteras av oss när det kommit fram."),
    ("Slutbesiktning", "Genomgång av huset, punktlista och överlämning."),
]

TILLKOMMER = [
    ("Grunden", "Platta eller plintar ska vara gjuten innan huset kommer. Vad den kostar beror på marken."),
    ("El, vatten och avlopp", "Framdragning till huset, och anslutningsavgifter till kommunen eller föreningen."),
    ("Markarbete", "Röjning, schakt och infart om det behövs för att lastbil och kran ska komma fram."),
    ("Kommunens avgifter", "Avgift för anmälan eller bygglov, och för eventuell strandskyddsdispens."),
    ("Tillval", "Ändringar i planlösning, ytskikt och inredning utöver det som ingår."),
]

STYR = [
    ("Storleken", "Den enskilt största posten. Priset per kvadratmeter sjunker något med större hus, men totalen stiger."),
    ("Planlösningen", "Fler väggar, fler våtrum och fler öppningar kostar mer än en öppen yta."),
    ("Nivån på material", "Kök, badrum och ytskikt är där spannet mellan lägsta och högsta nivå är störst."),
    ("Tomten", "Lutning, mark och framkomlighet för lastbil och kranbil avgör både grund och montage."),
    ("Avståndet", "Transporten är en verklig kostnad, och den växer med milen."),
]


def rader(lista):
    return "\n".join(f'''              <div class="prisrad">
                <h3>{a}</h3>
                <p>{b}</p>
              </div>''' for a, b in lista)


def pristabell():
    return "\n".join(f'''                  <tr>
                    <th scope="row"><a href="{lank}">{namn}</a></th>
                    <td>{yta}</td>
                    <td>{pris}</td>
                  </tr>''' for namn, lank, yta, pris in PRISER)


PRISSIDA = f'''    <main id="innehall">
      <section class="subpage-hero">
        <img class="subpage-hero__image" src="images/generated-materials-01.webp" width="1600" height="900" fetchpriority="high" decoding="async" alt="Materialprover med träpanel och fönsterdetalj">

        <div class="subpage-hero__content-wrap">
          <div class="subpage-hero__content">
            <h1 class="subpage-hero__title">Vad ett hus kostar</h1>
            <p class="subpage-hero__meta">Vad som ingår, vad som tillkommer och vad som styr summan</p>
          </div>
        </div>
      </section>

      <section class="guide">
        <div class="guide__inner">
          <aside class="guide__rail">
            <div class="guide__snabbsvar">
              <p class="guide__snabbsvar-etikett">Kort svar</p>
              <p>
                Husets pris är en del av totalen. Grund, anslutningar och
                markarbete ligger utanför och betalas till andra än oss.
                Räkna med dem från början, så blir det inga överraskningar.
              </p>
            </div>

            <nav class="guide__toc" aria-label="Innehåll på sidan">
              <p class="guide__toc-etikett">På den här sidan</p>
              <ol>
                <li><a href="#prisnivaer">Prisnivåer</a></li>
                <li><a href="#ingar">Det här ingår</a></li>
                <li><a href="#tillkommer">Det här tillkommer</a></li>
                <li><a href="#styr">Vad som styr priset</a></li>
                <li><a href="#offert">När du får ett pris</a></li>
              </ol>
            </nav>
          </aside>

          <div class="guide__text">
            <p class="guide__ingress">
              Ett hus har inget listpris på samma sätt som en bil. Men det går
              att säga vad som ingår, vad som tillkommer och vad som får
              summan att röra sig, så att du vet vad du jämför när du får
              offerten.
            </p>

            <section class="guide__sektion" id="prisnivaer">
              <h2>Prisnivåer</h2>
              <p>
                Priserna nedan är startpriser för respektive kategori. Vad just
                ditt hus kostar står i offerten, och den skriver vi när vi vet
                hur tomten ser ut.
              </p>

              <div class="matt">
                <table>
                  <thead>
                    <tr>
                      <th scope="col">Kategori</th>
                      <th scope="col">Storlek</th>
                      <th scope="col">Pris</th>
                    </tr>
                  </thead>
                  <tbody>
{pristabell()}
                  </tbody>
                </table>
              </div>
            </section>

            <section class="guide__sektion" id="ingar">
              <h2>Det här ingår</h2>
              <div class="prisrader">
{rader(INGAR)}
              </div>
            </section>

            <section class="guide__sektion" id="tillkommer">
              <h2>Det här tillkommer</h2>
              <p>
                Posterna nedan hör till bygget men betalas till andra än oss.
                Vi säger vad som krävs och när, så att ingenting står och
                väntar på varandra.
              </p>
              <div class="prisrader prisrader--tillkommer">
{rader(TILLKOMMER)}
              </div>
            </section>

            <section class="guide__sektion" id="styr">
              <h2>Vad som styr priset</h2>
              <div class="prisrader">
{rader(STYR)}
              </div>
            </section>

            <section class="guide__sektion" id="offert">
              <h2>När du får ett pris</h2>
              <p>
                Efter första samtalet och valet av modell skriver vi en offert
                där det står vad som ingår och vad som tillkommer, post för
                post. Hela ordningen finns på
                <a href="sa-fungerar-det.html">Så fungerar det</a>.
              </p>

              <p class="guide__vidare">
                <a class="knapp-fylld" href="kontakt.html">Begär offert</a>
                <a class="knapp-linje" href="attefallshus.html">Se husmodellerna</a>
              </p>
            </section>
          </div>
        </div>
      </section>

''' + io.open("_kontaktsektion.inc", encoding="utf-8").read() + '''    </main>

'''


def bygg():
    ut = []

    sida = (B.head("Attefallshus: reglerna efter 1 december 2025 | Idealhus",
                   "Vad som gäller för attefallshus efter regeländringen: mått "
                   "inom och utanför detaljplan, när anmälan krävs och när det "
                   "behövs bygglov.",
                   None, fil="attefallshus-regler.html")
            + "\n" + B.header("Våra hus") + "\n" + GUIDE + B.SIDFOT + "\n"
            + B.skript(TOC_SKRIPT))
    sida = sida.replace("  </body>",
                        '    <script type="application/ld+json">\n'
                        + faq_json() + "\n    </script>\n  </body>")
    io.open("attefallshus-regler.html", "w", encoding="utf-8",
            newline="").write(sida.replace("\n", "\r\n"))
    ut.append("attefallshus-regler.html")

    sida = (B.head("Priser | Idealhus",
                   "Vad ett hus fr\u00e5n Idealhus kostar: vad som ing\u00e5r, vad som "
                   "tillkommer och vad som styr priset.",
                   "generated-materials-01.webp", fil="priser.html")
            + "\n" + B.header("Priser") + "\n" + PRISSIDA + B.SIDFOT + "\n"
            + B.skript(TOC_SKRIPT))
    io.open("priser.html", "w", encoding="utf-8",
            newline="").write(sida.replace("\n", "\r\n"))
    ut.append("priser.html")

    sida = (B.head("Integritetspolicy | Idealhus",
                   "Så behandlar Idealhus personuppgifter. Inga kakor, ingen "
                   "besöksstatistik, och kontaktformuläret skickas med ditt "
                   "eget e-postprogram.",
                   None, fil="integritetspolicy.html")
            + "\n" + B.header("") + "\n" + POLICY + B.SIDFOT + "\n"
            + B.skript(""))
    io.open("integritetspolicy.html", "w", encoding="utf-8",
            newline="").write(sida.replace("\n", "\r\n"))
    ut.append("integritetspolicy.html")

    return ut


if __name__ == "__main__":
    print("\n".join(bygg()))
