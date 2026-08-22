# Python — Installatie & Eerste Programma

Tot nu toe kon je in dit leerpad meteen typen en zien wat er gebeurt — in de browser, zonder iets te installeren. Python werkt anders: het draait niet in de browser, maar op je eigen computer. Dat betekent dat je nu voor het eerst zelf een omgeving gaat inrichten. Dat is even wennen, maar het is ook precies hoe echte software-ontwikkeling werkt.

Er zijn drie losse dingen nodig, en het is belangrijk om ze niet door elkaar te halen:

1. **Python zelf** — de taal en het programma dat jouw code kan uitvoeren
2. **VS Code** — de editor waarin je je code typt (net een heel uitgebreid tekstverwerkingsprogramma)
3. **De Python-extensie in VS Code** — een uitbreiding die VS Code laat samenwerken met Python (kleurtjes, foutmeldingen tonen, de groene "Run"-knop)

VS Code zelf installeert geen Python en heeft geen ingebouwde package manager voor Python — dat komt allemaal uit stap 1.

## Stap 1 — Python installeren

Download Python van [python.org](https://www.python.org/downloads/). Op Windows: vink tijdens het installeren **"Add python.exe to PATH"** aan — dit is de meest gemaakte fout, en zonder dit vinkje kan je terminal Python straks niet vinden.

Controleer na installatie of het gelukt is. Open een terminal en typ:

```bash
python --version
```

Zie je een versienummer (zoals `Python 3.12.1`)? Dan werkt het. Zie je een foutmelding dat `python` niet herkend wordt? Dan is de installatie niet goed gegaan, of het PATH-vinkje is gemist — installeer opnieuw en let daar specifiek op.

Controleer meteen ook `pip`, de package manager die standaard met Python meekomt:

```bash
pip --version
```

## Stap 2 — VS Code installeren

Download VS Code van [code.visualstudio.com](https://code.visualstudio.com/). Installeer met de standaardinstellingen.

## Stap 3 — De Python-extensie

Open VS Code, ga naar het Extensions-icoon in de zijbalk, zoek op "Python" (de officiële extensie van Microsoft) en klik op **Install**. Deze extensie zorgt voor syntax-kleuring, foutmeldingen terwijl je typt, en een "Run"-knop rechtsboven in je bestand.

## Je eerste programma

Maak een map aan voor je oefeningen, open die map in VS Code (**File → Open Folder**), en maak een nieuw bestand aan met de naam `hallo.py`. Typ:

```python
print("Hallo, wereld!")
```

Klik rechtsboven op de groene ▶-knop (of gebruik de terminal in VS Code met `python hallo.py`). Zie je `Hallo, wereld!` verschijnen in het terminalvenster onderin? Dan staat je hele omgeving.

> **Tip:** Kom je een foutmelding tegen die je niet meteen snapt? Lees hem rustig van onder naar boven — de laatste regel vertelt meestal wát er misging, de regels erboven laten zien wáár. In module 8 van dit hoofdstuk gaan we hier dieper op in.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Installatie**: zorg dat `python --version` en `pip --version` allebei een versienummer teruggeven, installeer VS Code met de Python-extensie, en laat `print("Hallo, wereld!")` succesvol draaien vanuit een `.py`-bestand.
