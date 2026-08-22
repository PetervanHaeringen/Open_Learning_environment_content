# Module 1 — Eén opdracht, meerdere AI's

AI kan code schrijven.

Maar wat betekent dat eigenlijk?

In deze eerste module gaan we daar nog geen antwoord op geven. We gaan eerst **kijken**.

> **Waarom JavaScript?**  
> In deze leerlijn gebruiken we JavaScript voor kleine experimenten omdat TestGarden deze code rechtstreeks in het lesscherm kan uitvoeren. De manier van denken die je oefent geldt net zo goed voor Python, Java, PHP, C#, C++ en andere talen.

---

## 1. Wat heb je nodig?

Gebruik twee verschillende AI-systemen waar je toegang toe hebt.

Dat mogen bijvoorbeeld ChatGPT, Claude, Gemini, Copilot, Kimi of andere AI-systemen zijn.

Het merk of model is voor deze opdracht niet belangrijk.

> Het doel is niet om te bepalen welke AI "de beste" is. We onderzoeken wat er gebeurt wanneer twee systemen dezelfde opdracht krijgen.

---

## 2. Geef exact dezelfde opdracht

Open bij beide AI-systemen een nieuw gesprek.

Geef beide systemen **precies dezelfde tekst**:

> Schrijf een eenvoudig JavaScript-programma.  
> Gebruik de drie getallen 12, 7 en 20.  
> Toon met `console.log()` het grootste getal en het gemiddelde van de drie getallen.  
> Houd de code eenvoudig en voeg geen HTML toe.

Voeg niets aan de opdracht toe.

Als een AI eerst een vraag stelt, noteer dat dan ook als waarneming.

Bewaar het eerste antwoord van beide systemen.

---

## 3. Nog niet uitvoeren

Je hebt nu twee antwoorden gekregen.

**Voer de programma's nog niet uit.**

Lees eerst beide antwoorden alsof twee collega's ieder een oplossing voorstellen.

Onderzoek bijvoorbeeld:

- Hoe worden de drie getallen opgeslagen?
- Hoe wordt het grootste getal bepaald?
- Hoe wordt het gemiddelde berekend?
- Worden functies gebruikt?
- Heeft de AI iets toegevoegd waar niet om gevraagd werd?
- Heeft de AI aannames gemaakt?
- Is er code die je niet begrijpt?

Je hoeft nog niet te bepalen welke oplossing beter is.

**Eerst waarnemen.**

---

## 4. Voorspel

Schrijf voor beide oplossingen op wat je verwacht dat er in de console verschijnt.

Denk je dat beide programma's hetzelfde resultaat geven?

Een voorspelling hoeft niet juist te zijn. Juist het verschil tussen verwachting en werkelijkheid kan interessant zijn.

---

## 5. Test in TestGarden

Hieronder staat een kleine voorbeeldoplossing. Je kunt de JavaScript-code rechtstreeks aanpassen. TestGarden voert hem uit en toont de console-uitvoer.

```javascript
const getallen = [12, 7, 20];

const grootste = Math.max(...getallen);
const gemiddelde = (getallen[0] + getallen[1] + getallen[2]) / getallen.length;

console.log("Grootste:", grootste);
console.log("Gemiddelde:", gemiddelde);
```

Vervang de voorbeeldcode eerst door de oplossing van **AI A** en bekijk de uitvoer.

Gebruik daarna **Reset** of vervang de code door de oplossing van **AI B**.

Controleer:

1. Geeft de code het verwachte grootste getal?
2. Klopt het gemiddelde?
3. Komt de uitvoer overeen met jouw voorspelling?
4. Werken beide oplossingen op dezelfde manier?

Probeer daarna zelf iets: verander één van de drie getallen en **voorspel vóór de wijziging wat de nieuwe uitvoer zal zijn**.

---

## 6. Probeer de oplossing te verrassen

Een programma kan voor één voorbeeld goed werken en toch een zwakke oplossing zijn.

Probeer daarom andere waarden, bijvoorbeeld:

- drie gelijke getallen;
- een negatief getal;
- kommagetallen;
- een veel groter getal.

Kijk opnieuw naar de twee AI-oplossingen.

Blijven ze doen wat jij verwacht?

---

## 7. Welke oplossing zou jij accepteren?

Stel dat deze oplossingen afkomstig zijn van twee collega's.

Welke zou jij in een echt softwareproject accepteren?

Je mag ook besluiten dat je **geen van beide** zou accepteren.

"Deze werkt" is niet voldoende als argument.

Kijk bijvoorbeeld naar:

- begrijpelijkheid;
- eenvoud;
- leesbaarheid;
- onderhoudbaarheid;
- gedrag bij andere getallen.

---

## 8. Kijk terug naar de oorspronkelijke opdracht

Beide AI-systemen kregen exact dezelfde woorden.

Kijk nu naar de keten:

**opdracht → interpretatie door AI → code → werkelijk gedrag**

Wat heb je ontdekt?

---

## 9. Jouw eerste samenwerkingsregel

Formuleer één regel die jij jezelf voortaan wilt meegeven wanneer je AI gebruikt bij softwareontwikkeling.

Bewaar die regel. We komen er in module 2 op terug.

---

## Tot slot

Je hoefde in deze module niet te leren welke AI het beste is.

Je hoefde ook geen perfecte prompt te schrijven.

Je hebt iets anders geoefend:

**kijken voordat je oordeelt.**
