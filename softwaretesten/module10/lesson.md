# Module 10 — Black-box testtechnieken

Tot nu toe heb je vooral geleerd *dat* je test. Deze module gaat over *hoe* je slim kiest wát je test. Want je kunt onmogelijk alles testen — er zijn meestal oneindig veel mogelijke invoeren. De kunst is om met een klein, slim gekozen aantal testgevallen toch de meeste fouten te vinden.

---

## 1. Black-box: testen zonder in de code te kijken

Bij **black-box testen** behandel je het programma als een zwarte doos: je weet wat erin gaat en wat eruit zou moeten komen, maar je kijkt niet naar de code binnenin. Je test of het gedrag klopt met wat er beloofd is — de specificatie.

Het tegenovergestelde is **white-box testen**, waarbij je juist wél naar de interne code kijkt om te bepalen wat je test. Beide hebben hun plek. Black-box is krachtig omdat je testgevallen blijven werken, zelfs als de code binnenin volledig wordt herschreven — zolang het beloofde gedrag hetzelfde blijft.

In deze module behandelen we vier veelgebruikte black-box technieken:
- Equivalentieklassen
- Grenswaarde-analyse
- Beslissingstabellen
- Toestandsovergangen

---

## 2. Equivalentieklassen: groepen die hetzelfde behandeld worden

Stel je voor: een website laat alleen mensen van 18 jaar of ouder een account aanmaken. De leeftijd kan van 0 tot pakweg 120 lopen. Moet je nu álle 121 leeftijden testen? Nee.

Het idee achter **equivalentieklassen** is dat het programma grote groepen invoer op precies dezelfde manier behandelt. Voor de leeftijdscontrole zijn er eigenlijk maar twee groepen:
- **te jong**: 0 tot en met 17 (wordt geweigerd)
- **oud genoeg**: 18 tot en met 120 (wordt toegelaten)

Binnen elke groep maakt het niet uit welke waarde je kiest — als 25 werkt, werkt 40 waarschijnlijk ook. Dus test je één waarde per groep. Bijvoorbeeld leeftijd 10 (te jong) en leeftijd 30 (oud genoeg). Twee testgevallen in plaats van 121.

Een **geldige klasse** bevat waarden die geaccepteerd moeten worden, een **ongeldige klasse** waarden die geweigerd moeten worden. Belangrijk: vergeet de ongeldige klassen niet. Een programma dat goede invoer netjes verwerkt maar crasht op slechte invoer, is nog steeds stuk.

---

## 3. Grenswaarde-analyse: fouten leven op de randen

Programmeurs maken de meeste fouten niet midden in een groep, maar op de **grenzen** ertussen. Is het `>= 18` of `> 18`? Dat verschil van één jaar is precies waar het vaak misgaat.

**Grenswaarde-analyse** richt zich daarom op de randen van een equivalentieklasse. Bij de leeftijdsgrens van 18 zijn de interessante waarden:
- **17** — net te jong (laatste waarde van de afgekeurde groep)
- **18** — net oud genoeg (eerste waarde van de goedgekeurde groep)

Door precies deze twee te testen, vang je de klassieke "net wel / net niet"-fout. Een programmeur die per ongeluk `> 18` schreef in plaats van `>= 18`, zou een 18-jarige onterecht weigeren — en jouw test op leeftijd 18 vangt dat.

Sommige testers nemen ook de waarde een stap verder mee (16, 17, 18 of 17, 18, 19) om nóg zekerder te zijn. Hoe meer randwaarden je meeneemt, hoe grondiger — maar ook hoe meer werk. Het is een afweging.

Let op: grenswaarde-analyse werkt alleen bij **geordende** invoer, waar "groter" en "kleiner" betekenis hebben — getallen, datums, bedragen. Bij ongeordende invoer (zoals een keuze tussen rood, groen of blauw) bestaat er geen rand.

---

## 4. Beslissingstabellen: als meerdere voorwaarden samenkomen

Soms hangt het gedrag van een programma af van een combinatie van voorwaarden. Een webwinkel geeft bijvoorbeeld korting volgens deze regels:
- Lid van de klantenclub? **én**
- Bestelling boven de 50 euro?

Met twee voorwaarden die allebei waar of onwaar kunnen zijn, zijn er vier combinaties. Een **beslissingstabel** zet die netjes op een rij:

| Lid? | Boven 50 euro? | Korting |
|------|----------------|---------|
| ja   | ja             | 10%     |
| ja   | nee            | 5%      |
| nee  | ja             | geen    |
| nee  | nee            | geen    |

Elke kolom (of rij, in deze indeling) is een aparte regel die je test. De kracht van een beslissingstabel is dat je systematisch álle combinaties langsloopt — ook de combinatie die je anders misschien zou vergeten. Bovendien dwingt het opstellen ervan je om scherp te krijgen of de regels eigenlijk wel volledig en zonder tegenspraak zijn.

Bij twee voorwaarden zijn er vier combinaties, bij drie al acht, bij vier zestien — het verdubbelt steeds. Bij veel voorwaarden wordt dat onwerkbaar, en kies je de belangrijkste combinaties op basis van risico.

---

## 5. Toestandsovergangen: gedrag dat van de geschiedenis afhangt

Sommige systemen gedragen zich anders afhankelijk van waar ze zich op dat moment in bevinden — hun **toestand**. Denk aan een eenvoudig verkeerslicht: rood → groen → oranje → rood. Of een online bestelling: *concept → geplaatst → verzonden → geleverd*.

Bij **toestandsovergangstesten** test je of het systeem netjes van de ene toestand naar de andere gaat als er iets gebeurt (een *gebeurtenis*), en — minstens zo belangrijk — of het *niet* overgaat bij verboden acties.

Voorbeeld: een bestelling die al verzonden is, mag je niet meer kunnen annuleren. Dat is een **ongeldige overgang**. Een goede tester probeert juist die verboden stappen uit, want daar zitten vaak de gevaarlijkste bugs: een systeem dat een verzonden pakket toch laat annuleren, kan tot echte problemen leiden.

Je test dus twee dingen:
- de **geldige overgangen**: gebeuren ze allemaal correct?
- de **ongeldige overgangen**: worden ze allemaal netjes geweigerd?

---

## 6. Welke techniek wanneer?

Geen enkele techniek is "de beste" — ze vullen elkaar aan:
- **Equivalentieklassen** als er groepen invoer zijn die hetzelfde behandeld worden.
- **Grenswaarde-analyse** zodra er geordende grenzen in het spel zijn (leeftijden, bedragen, datums).
- **Beslissingstabellen** als het gedrag van combinaties van voorwaarden afhangt.
- **Toestandsovergangen** als het gedrag afhangt van waar het systeem zich bevindt.

In de praktijk combineer je ze. Voor de leeftijdscontrole gebruik je equivalentieklassen én grenswaarden samen. Een ervaren tester voelt aan welke techniek bij welk probleem past — en dat gevoel ontwikkel je door te oefenen.

---

> **Op weg naar een certificaat?**
> Deze technieken vormen de kern van internationaal erkende testcertificeringen op instapniveau, zoals de ISTQB Foundation. TestGarden bereidt je op de concepten voor; het officiële examen leg je af via een erkende instantie (in Nederland en België de BNTQB). Bespreek met je begeleider en thuis of en wanneer die stap iets voor jou is.
