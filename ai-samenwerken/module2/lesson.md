# Module 2 — Begrijp wat je laat bouwen

In module 1 heb je twee AI-systemen dezelfde opdracht gegeven.

Je hebt gekeken, voorspeld, uitgevoerd en vergeleken.

Misschien formuleerde je voor jezelf een regel zoals:

> *Lees AI-code eerst voordat je haar gebruikt.*

In deze module gaan we onderzoeken wat **lezen en begrijpen** eigenlijk betekent.

---

## 1. Nog niet uitvoeren

Bekijk deze code.

**Verander nog niets. Voorspel eerst wat er in de console zal verschijnen.**

```javascript
const getallen = [4, 7, 2];

for (const getal of getallen) {
    console.log(getal);
}
```

Schrijf je voorspelling op.

Kijk daarna pas naar de uitvoer in TestGarden.

Klopte je voorspelling?

Als dat zo is: probeer uit te leggen *waarom*.

Als dat niet zo is: probeer te vinden welke aanname niet klopte.

---

## 2. Wat begrijp je nog niet?

Bekijk dezelfde code opnieuw.

Misschien begrijp je alles. Misschien niet.

Woorden of tekens die vragen kunnen oproepen zijn bijvoorbeeld:

- `const`
- `[4, 7, 2]`
- `for`
- `of`
- `{ }`
- `console.log()`

Kies **één** onderdeel waarvan je niet precies weet wat het doet.

Vraag een AI:

> In deze JavaScript-code staat `[jouw gekozen onderdeel]`.  
> Leg alleen uit wat dit onderdeel hier doet. Verander de code nog niet.

Lees de uitleg.

Maar we stoppen daar niet.

### Hoe zou je kunnen controleren of de uitleg klopt?

Bedenk een klein experiment.

Als je bijvoorbeeld wilt onderzoeken wat `of` doet, kun je de waarden veranderen en kijken welke waarden achtereenvolgens in `getal` terechtkomen.

**Uitleg is nuttig. Waarneming geeft je extra bewijs.**

---

## 3. Eén verandering

Bekijk deze code:

```javascript
const getallen = [4, 7, 2];

for (const getal of getallen) {
    console.log(getal * 2);
}
```

Nog niet meteen kijken naar de uitvoer.

Wat verwacht je nu?

Wat is er veranderd ten opzichte van het vorige programma?

Voer daarna uit.

Kun je het verschil verklaren?

---

## 4. Van regels naar een mentaal model

Nu een iets groter voorbeeld:

```javascript
const prijzen = [10, 20, 30];

let totaal = 0;

for (const prijs of prijzen) {
    totaal = totaal + prijs;
}

console.log("Totaal:", totaal);
```

Voorspel opnieuw de uitvoer.

Probeer daarna het programma **met je eigen woorden** te beschrijven zonder de code regel voor regel te vertalen.

Bijvoorbeeld:

> Het programma begint met ...

Dat noemen we hier een **mentaal model**: jouw voorstelling van wat de software doet.

Een mentaal model hoeft niet perfect te zijn. Je kunt het verbeteren door te testen.

---

## 5. Onderzoek een belangrijke regel

Kijk naar:

```javascript
totaal = totaal + prijs;
```

Vraag een AI om deze regel uit te leggen.

Bedenk daarna een experiment waarmee je die uitleg kunt controleren.

Je zou bijvoorbeeld één prijs kunnen veranderen, een prijs kunnen verwijderen of `totaal` met een andere beginwaarde laten starten.

**Voorspel eerst. Verander daarna. Kijk vervolgens wat werkelijk gebeurt.**

---

## 6. AI kan ook overtuigend uitleggen

Een duidelijke uitleg klinkt prettig.

Maar duidelijke taal bewijst nog niet dat de uitleg klopt.

Wanneer een AI code uitlegt, kun je daarom dezelfde houding gebruiken als bij gegenereerde code:

1. lees de uitleg;
2. vergelijk haar met de code;
3. maak een voorspelling;
4. voer een klein experiment uit;
5. kijk of waarneming en uitleg bij elkaar passen.

Je hoeft AI niet te wantrouwen.

Je hoeft haar ook niet blind te vertrouwen.

**Je kunt samenwerken én controleren.**

---

## 7. Moet je iedere regel zelf kunnen schrijven?

Nee.

AI kan constructies voorstellen die jij nog niet zelf uit je hoofd zou kunnen schrijven.

Dat kan juist een manier zijn om te leren.

Maar als een regel belangrijk is voor de werking van je software, moet je een manier hebben om te onderzoeken wat die regel doet.

> **Je hoeft niet iedere regel zelf te kunnen schrijven. Maar je moet leren herkennen wanneer je begrip tekortschiet en weten hoe je verder kunt onderzoeken.**

---

## 8. Kleine uitdaging

Laat een AI deze code veranderen zodat alleen de getallen groter dan 15 worden opgeteld:

```javascript
const prijzen = [10, 20, 30, 5, 40];

let totaal = 0;

for (const prijs of prijzen) {
    totaal = totaal + prijs;
}

console.log("Totaal:", totaal);
```

Voordat je de AI-oplossing uitvoert:

- lees de wijziging;
- wijs aan welke regels veranderd zijn;
- voorspel de uitkomst;
- voer de code daarna pas uit;
- probeer vervolgens zelf een andere lijst met prijzen.

Als de code werkt, stel jezelf nog één vraag:

**Begrijp ik waarom zij werkt?**

---

## Tot slot

In deze module heb je niet geoefend om zoveel mogelijk code te schrijven.

Je hebt geoefend om een **model in je hoofd** te bouwen van wat code doet.

Dat maakt het gesprek met AI beter.

Want dan kun je niet alleen vragen:

> *Kun je dit voor mij maken?*

maar ook:

> *Waarom heb je dit zo gemaakt, en hoe kunnen we controleren dat onze uitleg klopt?*
