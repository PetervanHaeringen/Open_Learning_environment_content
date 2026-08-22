# Module 3 — Van wens naar softwareprobleem

In module 1 onderzocht je wat verschillende AI-systemen maken.

In module 2 onderzocht je wat code **doet**.

Nu zetten we een stap terug. Voordat je code laat maken, is er namelijk een andere vraag:

> **Wat moet er eigenlijk veranderen?**

Een gebruikerswens en een softwarewijziging zijn niet hetzelfde.

---

## 1. Een eenvoudige wens

Stel dat iemand zegt:

> Voeg een knop toe waarmee ik de begroeting kan veranderen.

Dat klinkt als één kleine wijziging.

```html
<button id="verander">Verander begroeting</button>
<p id="tekst">Welkom in TestGarden</p>
```

```javascript
const knop = document.getElementById("verander");
const tekst = document.getElementById("tekst");

knop.addEventListener("click", function () {
    tekst.textContent = "Fijn dat je er bent!";
});
```

Probeer de knop.

Wat moest er allemaal aanwezig zijn om deze kleine wens te laten werken? Denk niet alleen aan de regel die de tekst verandert.

---

## 2. Wens of oplossing?

De wens was: *Ik wil de begroeting kunnen veranderen.*

Een AI zou meteen een knop, invoerveld, database, gebruikersprofiel, API of instellingenpagina kunnen voorstellen. Dat zijn **mogelijke oplossingen**, niet de wens zelf.

Vraag vóór het programmeren:

1. Wie wil iets kunnen doen?
2. Wat wil die persoon bereiken?
3. Wat gebeurt er nu?
4. Wat moet er daarna anders zijn?
5. Welke bestaande onderdelen kunnen geraakt worden?

---

## 3. Vraag AI nog niet om code

Geef een AI:

> Een gebruiker wil in een bestaande webapp een begroeting kunnen veranderen. Schrijf nog geen code. Noem eerst welke onderdelen van de bestaande software je zou willen onderzoeken voordat je een oplossing voorstelt.

Markeer in het antwoord:
- wat de AI uit de opdracht kan afleiden;
- wat de AI nog niet kan weten;
- wat de AI aanneemt.

Een AI kan een nuttige **hypothese** over een systeem geven zonder dat die hypothese waar hoeft te zijn.

---

## 4. Een kleine verandering kan een lang pad hebben

Stel dat de wens is:

> Wanneer een docent een nieuwe leerlijn toevoegt, moet die automatisch beschikbaar worden voor cursisten.

Waar zou jij zoeken? Schrijf eerst zelf een mogelijk pad op.

Bekijk daarna dit voorbeeld uit een echte verandering in TestGarden:

```text
track
  ↓
menu
  ↓
route
  ↓
module
  ↓
toewijzen
  ↓
Mijn Tuin
  ↓
vragen
  ↓
antwoorden
  ↓
docent
  ↓
beoordeling
  ↓
voortgang
```

Het zichtbare probleem leek eerst alleen het **menu** te zijn. Maar een nieuwe leerlijn is pas bruikbaar wanneer de relevante paden daarna ook werken.

> **Een feature is zelden alleen de plek waar je haar op het scherm ziet.**

---

## 5. Onderzoek afhankelijkheden

Voorspel eerst de uitvoer:

```javascript
const gebruiker = {
    naam: "Samira",
    punten: 3
};

function begroeting() {
    return `Welkom ${gebruiker.naam}`;
}

function voortgang() {
    return `${gebruiker.naam} heeft ${gebruiker.punten} punten`;
}

console.log(begroeting());
console.log(voortgang());
```

Verander daarna alleen `"Samira"` in `"Alex"`.

Waarom verandert één wijziging op twee plaatsen in de uitvoer?

De functies zijn verschillend, maar gebruiken dezelfde gegevens. Dat is een eenvoudige vorm van een **afhankelijkheid**.

---

## 6. Wat gebeurt er als de structuur verandert?

Stel dat een AI dit voorstelt:

```javascript
const gebruiker = {
    profiel: {
        naam: "Samira"
    },
    punten: 3
};

function begroeting() {
    return `Welkom ${gebruiker.naam}`;
}

function voortgang() {
    return `${gebruiker.naam} heeft ${gebruiker.punten} punten`;
}

console.log(begroeting());
console.log(voortgang());
```

Vraag vóór het uitvoeren:

> Welke bestaande code verwacht nog `gebruiker.naam`?

Voer daarna uit. Herstel vervolgens de functies zodat ze `gebruiker.profiel.naam` gebruiken.

**Een lokaal verstandige wijziging kan elders gevolgen hebben.**

---

## 7. De browser als bron van bewijs

Open de ontwikkelaarstools van je browser, bijvoorbeeld met **F12**, en zoek de **Console**.

Kijk wat je daar ziet terwijl je een oefening uitvoert.

De oefeningen van TestGarden draaien geïsoleerd. Daardoor kan uitvoer in het oefenvenster duidelijker zichtbaar zijn dan in de hoofdconsole. Dat is óók informatie over de infrastructuur.

We gaan DevTools hier nog niet uitgebreid gebruiken. Ontdek alleen:

> **De gebruikersinterface is niet de enige plek waar software informatie over haar gedrag laat zien.**

Later gebruiken we dit veel gerichter bij foutopsporing.

---

## 8. Eerst een kaart, dan een wijziging

Stel dat je in een bestaand project deze opdracht krijgt:

> Voeg een tweede taal toe aan een module.

Vraag AI niet meteen: *Maak dit.*

Vraag bijvoorbeeld:

> Ik wil een tweede taal toevoegen aan een bestaande module. Help me eerst onderzoeken welke onderdelen hierdoor geraakt kunnen worden. Geef hypotheses en vragen, nog geen code.

Maak daarna een eenvoudige kaart, bijvoorbeeld:

```text
lesbestand
   ↓
taalkeuze
   ↓
loader
   ↓
route
   ↓
template
   ↓
weergave
```

Jouw kaart mag anders zijn. Het doel is niet vooraf alles te weten, maar **bewust te onderzoeken voordat je verandert**.

---

## 9. Wanneer mag AI gaan bouwen?

Als je beter begrijpt wat de wens is, wat het systeem nu doet, welke onderdelen waarschijnlijk geraakt worden en welke aannames nog gecontroleerd moeten worden, kun je gerichter om implementatie vragen:

> Dit is de gewenste verandering. Dit zijn de onderdelen die we hebben gevonden. Deze bestaande werking moet behouden blijven. Stel de kleinste wijziging voor die dit mogelijk maakt. Leg uit welke bestaande paden we daarna opnieuw moeten testen.

Dat is geen magische prompt.

Het is het resultaat van **beter begrijpen wat je aan het bouwen bent**.

---

## Tot slot

Softwareontwikkeling begint niet bij code. Tussen een menselijke wens en een werkende wijziging zit onderzoek.

AI kan helpen met vragen, mogelijke afhankelijkheden, hypotheses, code lezen en oplossingen voorstellen.

Maar het bestaande systeem levert uiteindelijk het bewijs.

**Eerst de tuin bekijken. Dan pas bepalen waar je gaat graven.**
