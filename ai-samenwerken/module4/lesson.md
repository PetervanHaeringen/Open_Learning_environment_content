# De kleinste werkende verandering

Leer AI-wijzigingen klein, begrijpelijk en controleerbaar te houden. Onderzoek eerst welke bouwstenen al bestaan voordat je nieuwe code laat maken.

In module 3 onderzocht je eerst **wat** er in een bestaand systeem geraakt kan worden.

Nu gaan we daadwerkelijk iets veranderen.

Maar voordat we code toevoegen, stellen we een andere vraag:

> **Bestaat wat we nodig hebben misschien al?**

Een kleine verandering betekent namelijk niet alleen: zo weinig mogelijk regels schrijven.

Het betekent ook:

> **Gebruik waar mogelijk de eenvoudigste bestaande bouwsteen die het gewenste gedrag al heeft.**

---

## 1. Iets dat eruitziet als een knop

Stel dat je deze wens aan een AI geeft:

> Maak een knop met de tekst `Begroet` die na een klik `Welkom!` toont.

AI zou bijvoorbeeld dit kunnen maken:

```html
<div id="begroet" class="knop">Begroet</div>
<p id="uitvoer"></p>
```

```javascript
const knop = document.getElementById("begroet");
const uitvoer = document.getElementById("uitvoer");

knop.addEventListener("click", function () {
    uitvoer.textContent = "Welkom!";
});
```

Met CSS kan de `div` er zelfs precies als een knop uitzien.

Probeer het. Werkt het? Waarschijnlijk wel.

Maar stel nu een tweede vraag:

> **Heeft HTML misschien al een element dat bedoeld is om een knop te zijn?**

Ja:

```html
<button id="begroet">Begroet</button>
<p id="uitvoer"></p>
```

De JavaScript-code kan hetzelfde blijven.

Beide oplossingen kunnen werken. Toch zijn ze niet hetzelfde.

---

## 2. Werkend is niet het einde van de beoordeling

Een `div` is een algemene container.

Een `button` heeft een specifieke betekenis: **dit is een knop**.

De browser weet daardoor al meer over het element. Een echte button heeft bijvoorbeeld standaardgedrag voor toetsenbordbediening en focus, semantische betekenis voor toegankelijkheid, formuliergedrag en ondersteuning voor `disabled`.

Bij een `div` moet je gedrag dat je nodig hebt vaak zelf toevoegen.

Daarom is de vraag niet alleen:

> **Werkt de code?**

maar ook:

> **Gebruikt de code een passende bouwsteen voor wat we proberen te maken?**

Dit is belangrijk bij het beoordelen van AI-code. AI kan een oplossing maken die zichtbaar werkt zonder dat het de meest passende oplossing is.

---

## 3. `div` is niet fout

We moeten hier geen nieuwe absolute regel van maken.

> Gebruik nooit een `div`.

zou net zo onzorgvuldig zijn.

Een `div` is juist nuttig wanneer je een algemene container nodig hebt waarvoor geen specifieker HTML-element bedoeld is.

```html
<div class="kaart">
    <h2>Module 4</h2>
    <p>De kleinste werkende verandering</p>
</div>
```

De betere vraag is:

> **Wat is dit onderdeel en bestaat daar al een passende bouwsteen voor?**

Bijvoorbeeld:

- een actieknop → `<button>`
- een verwijzing naar een andere pagina → `<a>`
- navigatie → `<nav>`
- een invoerveld → `<input>`
- een kop → `<h1>` tot en met `<h6>`
- een algemene container → vaak `<div>`

Je hoeft deze lijst niet uit je hoofd te leren. Je moet leren **de vraag te stellen**.

---

## 4. Onderzoek de keuze van AI

Geef een AI deze opdracht:

> Maak in HTML en JavaScript een klikbaar element met de tekst `Volgende module`. Als erop wordt geklikt, moet `We gaan verder` op het scherm verschijnen.

Bekijk de oplossing voordat je haar uitvoert.

Vraag jezelf af:

1. Welk HTML-element heeft AI gekozen?
2. Waarom zou AI dat element gekozen kunnen hebben?
3. Bestaat er een specifieker element voor deze functie?
4. Welke verantwoordelijkheid neemt de code zelf over?
5. Welke functionaliteit zou de browser al kunnen leveren?

Vraag daarna aan AI waarom het dit element heeft gekozen en welke standaard HTML-elementen nog meer geschikt zouden kunnen zijn.

Accepteer het antwoord niet automatisch. Gebruik het als **hypothese die je kunt onderzoeken**.

---

## 5. Van wens naar kleinste passende oplossing

De wens is:

> De gebruiker voert een naam in en klikt op `Begroet`. Daarna verschijnt `Welkom` gevolgd door de naam.

Een passende basis:

```html
<label for="naam">Naam:</label>
<input id="naam" value="Samira">
<button id="begroet">Begroet</button>
<p id="uitvoer"></p>
```

```javascript
const naam = document.getElementById("naam");
const knop = document.getElementById("begroet");
const uitvoer = document.getElementById("uitvoer");

knop.addEventListener("click", function () {
    uitvoer.textContent = `Welkom ${naam.value}!`;
});
```

Probeer het. Verander de naam. Klik meerdere keren.

Voordat we iets aanpassen:

> **Wat werkt er nu al?**

Dat is onze uitgangssituatie.

---

## 6. Een kleine nieuwe wens

De gebruiker vraagt:

> Als het naamveld leeg is, wil ik niet `Welkom !` zien maar `Vul eerst je naam in.`

Vraag AI om de **kleinst mogelijke wijziging**:

> Hieronder staat werkende JavaScript-code. Als het naamveld leeg is, moet `Vul eerst je naam in.` verschijnen. Verander zo weinig mogelijk. Verander geen HTML en voeg geen andere functies toe. Laat duidelijk zien welke regels je wijzigt.

Vraag daarna:

> **Wat heeft AI veranderd en was iedere verandering noodzakelijk voor de wens?**

---

## 7. Voorspel vóór je uitvoert

Stel dat AI dit voorstelt:

```javascript
const naam = document.getElementById("naam");
const knop = document.getElementById("begroet");
const uitvoer = document.getElementById("uitvoer");

knop.addEventListener("click", function () {
    if (naam.value.trim() === "") {
        uitvoer.textContent = "Vul eerst je naam in.";
        return;
    }

    uitvoer.textContent = `Welkom ${naam.value}!`;
});
```

Voer nog niet meteen uit. Voorspel eerst:

1. Wat gebeurt er met een leeg naamveld?
2. Wat gebeurt er met `Alex`?
3. Wat gebeurt er met alleen een paar spaties?
4. Blijft de oorspronkelijke begroeting werken?

Test daarna pas.

> **Werkt de nieuwe functie én werkt het oude gedrag nog?**

Dat laatste wordt later belangrijk bij regressietesten.

---

## 8. Waarom `trim()`?

Als je deze regel niet begrijpt:

```javascript
if (naam.value.trim() === "") {
```

neem hem dan niet gedachteloos over.

Vraag AI wat `trim()` doet en welk probleem het hier probeert op te lossen. Onderzoek het daarna zelf:

```javascript
console.log("   ".trim());
console.log("  Samira  ".trim());
```

Nu heb je de uitleg niet alleen gekregen, maar ook **onderzocht**.

---

## 9. Nog een manier om klein te kijken: een diff

Bij softwareontwikkeling en AI-programmeertools kom je vaak een **diff** tegen.

Een diff laat vooral zien wat veranderd is:

```diff
 knop.addEventListener("click", function () {
+    if (naam.value.trim() === "") {
+        uitvoer.textContent = "Vul eerst je naam in.";
+        return;
+    }
+
     uitvoer.textContent = `Welkom ${naam.value}!`;
 });
```

Een regel met `+` is toegevoegd. Een regel met `-` zou verwijderd zijn.

Een diff helpt dus bij de vraag:

> **Wat is er precies veranderd?**

Maar er zit een valkuil in.

---

## 10. Een diff is geen volledig programma

Kopieer je alleen het gewijzigde fragment naar een lege JavaScript-omgeving, dan kun je bijvoorbeeld krijgen:

```text
Fout: knop is not defined
```

Waarom?

Omdat ergens anders stond:

```javascript
const naam = document.getElementById("naam");
const knop = document.getElementById("begroet");
const uitvoer = document.getElementById("uitvoer");
```

Het fragment is afhankelijk van **context**.

> **Een wijziging kan logisch zijn zonder dat het losse wijzigingsfragment zelfstandig uitvoerbaar is.**

Kort gezegd:

**code ≠ wijziging ≠ context ≠ uitvoering**

Gebruik een diff om een verandering te begrijpen. Gebruik de volledige software om te onderzoeken of die verandering werkelijk werkt.

---

## 11. Wat als AI veel meer bouwt?

Stel dat je alleen om controle van een leeg naamveld vraagt en AI daarnaast nieuwe CSS toevoegt, een `div` als foutmelding maakt, een aparte `validateName()`-functie bouwt, live-validatie toevoegt en de HTML herstructureert.

Misschien zijn sommige voorstellen nuttig. Maar waren ze nodig?

Verdeel de veranderingen in:

**A — noodzakelijk voor de wens**  
**B — mogelijk nuttig, maar niet noodzakelijk**  
**C — staat los van de opdracht**

Dit is geen verbod op verbetering. Het maakt de **scope** zichtbaar.

---

## 12. Meer code is meer verantwoordelijkheid

Wanneer je bestaande browserfunctionaliteit gebruikt, hoef je die functionaliteit niet zelf opnieuw te bouwen.

Vraag daarom breder:

> **Bestaat hiervoor al iets betrouwbaars in de taal, het platform, het framework of onze bestaande code?**

Iedere zelfgebouwde oplossing brengt verantwoordelijkheid mee: begrijpen, testen, documenteren, onderhouden, beveiligen en toegankelijk houden.

Daarom betekent *kleinste werkende verandering* niet:

> schrijf altijd zo weinig mogelijk tekens.

Het betekent eerder:

> **Voeg zo weinig mogelijk nieuwe verantwoordelijkheid toe om de wens goed op te lossen.**

---

## 13. Laat AI eerst kijken voordat het bouwt

Probeer:

> Onderzoek eerst welke bestaande HTML-elementen, browserfuncties en bestaande code deze functionaliteit al ondersteunen. Stel daarna de kleinste passende wijziging voor. Noem eventuele andere verbeteringen afzonderlijk, maar voer die nog niet door.

Vergelijk dat met:

> Bouw deze functie.

Krijg je een ander soort antwoord?

Welke opdracht helpt jou het beste te begrijpen **waarom** iets wordt gebouwd?

---

## 14. Wat zou je committen?

Welke beschrijving vertelt een collega het duidelijkst wat je hebt veranderd?

**A.** `code verbeterd`

**B.** `formulier aangepast`

**C.** `toon melding wanneer naamveld leeg is`

Een goede wijziging heeft niet alleen een beperkte technische omvang. Ze heeft ook een **begrijpelijk doel**.

---

## Tot slot

AI kan heel snel nieuwe software construeren.

Daardoor wordt een andere vaardigheid steeds belangrijker:

> **Herkennen wanneer iets helemaal niet opnieuw gebouwd hoeft te worden.**

Een oplossing is niet automatisch goed omdat ze werkt.

Vraag daarom:

- Wat proberen we werkelijk te bereiken?
- Wat bestaat er al?
- Welke bouwsteen past bij de bedoeling?
- Wat voegt AI toe?
- Is dat allemaal nodig?
- Welke nieuwe verantwoordelijkheid ontstaat hierdoor?
- Wat moet na de verandering nog steeds werken?

En wanneer AI een wijziging voorstelt:

> **Bekijk de diff, maar vergeet de context niet.**

De cyclus wordt:

**wens → onderzoeken wat al bestaat → passende bouwsteen → kleinste wijziging → voorspellen → uitvoeren → diff bekijken → context controleren → testen**

In de volgende module voegen we daar een belangrijke vraag aan toe:

> **Wat moet na onze wijziging nog steeds werken?**
