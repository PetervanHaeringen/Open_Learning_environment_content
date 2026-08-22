# Python — Input & Foutmeldingen lezen

Met `input()` kun je je programma laten reageren op wat iemand typt — dit maakt een programma voor het eerst echt interactief, in de terminal in plaats van een browserformulier.

```python
naam = input("Hoe heet je? ")
print(f"Hallo, {naam}!")
```

Er is één belangrijke valkuil: `input()` geeft **altijd een string terug**, ook als iemand een getal typt. Wil je met die invoer rekenen, dan moet je hem eerst omzetten:

```python
leeftijd_tekst = input("Hoe oud ben je? ")
leeftijd = int(leeftijd_tekst)   # zet de tekst om naar een geheel getal

volgend_jaar = leeftijd + 1
print(f"Volgend jaar ben je {volgend_jaar}.")
```

Vergeet je die omzetting, dan krijg je een foutmelding zodra je met `+` probeert te rekenen op een string. En dat brengt ons bij het tweede onderwerp van deze module: **foutmeldingen leren lezen**.

## Een traceback lezen

Python-foutmeldingen heten **tracebacks**, en ze zien er in het begin overweldigend uit — veel tekst, met bestandsnamen en regelnummers. De truc is: lees van **onder naar boven**.

```
Traceback (most recent call last):
  File "leeftijd.py", line 4, in <module>
    volgend_jaar = leeftijd + 1
TypeError: can only concatenate str (not "int") to str
```

- **De laatste regel** vertelt je wát er misging: `TypeError: can only concatenate str (not "int") to str` — Python probeerde tekst en een getal bij elkaar op te tellen, en dat kan niet.
- **De regel erboven** vertelt je waar het misging: regel 4, bij `volgend_jaar = leeftijd + 1`.
- De oplossing: `leeftijd` was nog een string, en had eerst met `int()` omgezet moeten worden.

Een traceback is geen teken dat je iets fout hebt gedaan als persoon — het is Python die precies vertelt waar te kijken. Dat is een groot verschil met bijvoorbeeld een JavaScript-console, waar de melding vaak korter en minder specifiek is over de exacte plek.

> **Tip:** Zie je een foutmelding die je niet meteen snapt? Kopieer de laatste regel (het type fout + de beschrijving) en zoek daarop. Bijna elke Python-foutmelding is al duizenden keren door iemand anders tegengekomen.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Input & Foutmeldingen**: schrijf een programma dat met `input()` iemands leeftijd vraagt, dit omzet met `int()`, en berekent hoe oud iemand over 10 jaar is. Verwijder daarna bewust de `int()`-omzetting, bekijk de traceback die daardoor ontstaat, en herstel de fout.
