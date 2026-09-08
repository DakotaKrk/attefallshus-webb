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

FRAGOR = [
    ("Krävs det bygglov för ett attefallshus?",
     "Nej, inte inom måtten nedan. Sedan 1 december 2025 krävs varken bygglov "
     "eller anmälan för själva byggnaden. Men ska huset ha vatten, avlopp, "
     "ventilation eller eldstad krävs fortfarande en anmälan för de "
     "installationerna, och det gör de flesta hus som ska gå att bo i."),
    ("Hur stort får huset vara?",
     "Inom detaljplan högst 30 m² per byggnad och 45 m² sammanlagt på tomten, "
     "med en nockhöjd på 4,0 meter. Utanför detaljplan är gränserna 50 m² per "
     "byggnad, 65 m² sammanlagt och 4,5 meter i nockhöjd."),
    ("Hur nära tomtgränsen får huset stå?",
     "Minst 4,5 meter, om inte grannen ger sitt skriftliga medgivande. Utan "
     "medgivande krävs bygglov för en placering närmare gränsen."),
    ("Får jag bo i huset året om?",
     "Ja, om det byggs som komplementbostadshus. Då ska det uppfylla kraven "
     "på en fullvärdig bostad, med kök och badrum. Ett komplementbyggnad utan "
     "de kraven får användas som förråd, gäststuga, kontor eller bastu."),
    ("Finns det platser där reglerna inte gäller?",
     "Ja. Inom strandskyddat område krävs dispens även för en byggnad som "
     "annars är lovbefriad. I områden med särskilt kulturhistoriskt värde, "
     "inom vissa riksintressen och där detaljplanen säger annat krävs bygglov "
     "som vanligt. Kommunen avgör i det enskilda fallet."),
]

FAQ_LD = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": f,
         "acceptedAnswer": {"@type": "Answer", "text": s}}
        for f, s in FRAGOR
    ],
}


def faq_json():
    import json
    return json.dumps(FAQ_LD, ensure_ascii=False, indent=2)


def fragor_html():
    return "\n".join(f'''            <details class="fraga">
              <summary><span>{f}</span><span class="fraga__pil" aria-hidden="true"></span></summary>
              <p>{s}</p>
            </details>''' for f, s in FRAGOR)


GUIDE = f'''    <main id="innehall">
      <section class="guide-topp">
        <div class="guide-topp__inner">
          <p class="section-label">Guide · uppdaterad 8 september 2026</p>
          <h1 class="guide-topp__titel">Attefallshus: vad som gäller efter&nbsp;regeländringen</h1>
          <p class="guide-topp__lead">
            Den 1 december 2025 skrevs reglerna om. Begreppen attefallshus och
            friggebod finns inte längre i lagen, anmälningsplikten för själva
            byggnaden är borta, och du får bygga större utanför detaljplan än
            inom. Här är vad det betyder i praktiken.
          </p>
        </div>
      </section>

      <section class="guide">
        <div class="guide__inner">
          <aside class="guide__snabbsvar">
            <p class="guide__snabbsvar-etikett">Kort svar</p>
            <p>
              Inom måtten behövs varken bygglov eller anmälan för byggnaden.
              Ska den ha vatten, avlopp, ventilation eller eldstad krävs
              ändå anmälan för installationerna — och det gör nästan alla hus
              man ska kunna bo i.
            </p>
          </aside>

          <div class="guide__text">
            <h2>Vad som ändrades</h2>
            <p>
              Fram till december 2025 var ordningen den att ett attefallshus
              krävde en anmälan till kommunen och ett startbesked innan bygget
              fick börja. Både anmälningsplikten och startbeskedet är nu
              slopade för komplementbyggnader och komplementbostadshus. Orden
              attefallshus och friggebod är samtidigt borta ur lagtexten och
              ersatta av <em>komplementbyggnad</em> och
              <em>komplementbostadshus</em>.
            </p>
            <p>
              Vi använder ändå ordet attefallshus på den här sajten, eftersom
              det är det ordet alla söker på och känner igen. Det är samma
              sorts hus som avses.
            </p>

            <h2>Måtten</h2>
            <p>
              Den stora nyheten är att gränsen skiljer sig åt beroende på om
              tomten ligger inom detaljplan eller inte. Sammanlagt-kolumnen är
              en gemensam pott för alla lovfria komplementbyggnader på tomten,
              inte per hus.
            </p>

            <div class="matt">
              <table>
                <thead>
                  <tr>
                    <th scope="col">Mått</th>
                    <th scope="col">Inom detaljplan</th>
                    <th scope="col">Utanför detaljplan</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">Per byggnad</th>
                    <td>30 m²</td>
                    <td>50 m²</td>
                  </tr>
                  <tr>
                    <th scope="row">Sammanlagt på tomten</th>
                    <td>45 m²</td>
                    <td>65 m²</td>
                  </tr>
                  <tr>
                    <th scope="row">Nockhöjd</th>
                    <td>4,0 m</td>
                    <td>4,5 m</td>
                  </tr>
                  <tr>
                    <th scope="row">Till tomtgräns</th>
                    <td colspan="2">4,5 m, eller närmare med grannens skriftliga medgivande</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>När det ändå krävs en anmälan</h2>
            <p>
              Anmälningsplikten är borta för byggnaden — men inte för det som
              händer inuti den. Anmälan krävs fortfarande om åtgärden berör
              den bärande konstruktionen, påverkar brandskyddet väsentligt,
              innehåller eldstad eller rökkanal, eller berör installationer
              för vatten, avlopp eller ventilation.
            </p>
            <p>
              Det sista är värt att stanna vid: ett komplementbostadshus med
              kök och badrum har per definition vatten och avlopp. I praktiken
              betyder det att de flesta hus som ska gå att bo i ändå passerar
              kommunen — men för installationerna, inte för byggnaden.
            </p>

            <h2>När det krävs bygglov som vanligt</h2>
            <ul class="guide__lista">
              <li>Om huset placeras närmare tomtgränsen än 4,5 meter utan att grannen har gett sitt medgivande.</li>
              <li>I områden med särskilt kulturhistoriskt värde och inom vissa riksintressen.</li>
              <li>Om detaljplanen för området säger att bygglov krävs.</li>
              <li>Inom strandskyddat område krävs dessutom strandskyddsdispens, även för en byggnad som annars är lovbefriad. Strandskyddet påverkas inte av regeländringen.</li>
            </ul>

            <h2>Komplementbyggnad eller komplementbostadshus?</h2>
            <p>
              Skillnaden ligger i vad huset ska vara, inte i hur stort det får
              vara. Ett <strong>komplementbostadshus</strong> är en fullvärdig
              bostad med kök och badrum, och får bos i året om. En
              <strong>komplementbyggnad</strong> saknar de kraven och används
              som gäststuga, kontor, förråd eller bastu. Måtten och avstånden
              är desamma.
            </p>

            <h2>Vanliga frågor</h2>
            <div class="fragor">
{fragor_html()}
            </div>

            <h2>Vem gör vad</h2>
            <p>
              Vi tar fram ritningar och underlag och säger vad som gäller för
              just din tomt. Det är du som är byggherre och som står för
              kontakten med kommunen när något ska anmälas. Hela ordningen,
              steg för steg, finns på
              <a href="sa-fungerar-det.html">Så fungerar det</a>.
            </p>

            <p class="guide__kallor">
              Uppgifterna är kontrollerade den 8 september 2026 mot kommunala
              och branschgemensamma sammanställningar av regeländringen.
              Reglerna kan ändras och kommunen avgör i det enskilda fallet —
              stäm alltid av med din byggnadsnämnd innan du börjar bygga.
            </p>

            <p class="guide__vidare">
              <a class="model-price__button" href="attefallshus.html">Se våra attefallshus</a>
              <a class="site-footer__button" href="kontakt.html">Fråga oss om din tomt</a>
            </p>
          </div>
        </div>
      </section>
    </main>

'''

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
              Idealhus AB, organisationsnummer [fylls i], Stockholm, är
              personuppgiftsansvarig för behandlingen som beskrivs här. Du når
              oss på <a href="mailto:ahmed@idealhus.se">ahmed@idealhus.se</a>
              eller <a href="mailto:sahand@idealhus.se">sahand@idealhus.se</a>.
            </p>

            <h2>Vilka uppgifter vi behandlar</h2>
            <p>
              Om du fyller i kontaktformuläret lämnar du namn, e-postadress
              och — om du vill — telefonnummer, ort, vilken husmodell du är
              intresserad av och det du skriver i meddelandet. Vi behandlar
              bara det du själv skriver.
            </p>

            <h2>Hur formuläret fungerar</h2>
            <p>
              Formuläret skickas inte via någon formulärtjänst. När du trycker
              på skicka öppnas ditt eget e-postprogram med meddelandet ifyllt,
              och du skickar det som ett vanligt mejl. Uppgifterna sparas
              alltså inte på webbplatsen och passerar ingen tredje part på
              vägen — de hamnar i vår inkorg, hos vår e-postleverantör.
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
              Förfrågningar sparas i [antal] månader efter senaste kontakten,
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


def bygg():
    ut = []

    sida = (B.head("Attefallshus: reglerna efter 1 december 2025 | Idealhus",
                   "Vad som gäller för attefallshus efter regeländringen: mått "
                   "inom och utanför detaljplan, när anmälan krävs och när det "
                   "behövs bygglov.",
                   None, fil="attefallshus-regler.html")
            + "\n" + B.header("Våra hus") + "\n" + GUIDE + B.SIDFOT + "\n"
            + B.skript(""))
    sida = sida.replace("  </body>",
                        '    <script type="application/ld+json">\n'
                        + faq_json() + "\n    </script>\n  </body>")
    io.open("attefallshus-regler.html", "w", encoding="utf-8",
            newline="").write(sida.replace("\n", "\r\n"))
    ut.append("attefallshus-regler.html")

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
