# Python — Loops (for, while)

Een `for`-loop in Python ziet er anders uit dan in de meeste andere talen — er is geen teller, geen `i++`, geen puntkomma's. In plaats daarvan loop je direct door een reeks waarden.

Voor een simpele telling gebruik je `range()`:

```python
for i in range(1, 6):
    print(f"Ronde {i}")
```

`range(1, 6)` genereert de getallen 1 tot en met 5 — let op: de eindwaarde (6) telt zelf niet mee. `range(5)` (met maar één getal) begint automatisch bij 0 en gaat tot en met 4.

Een `while`-loop gebruik je als je niet vooraf weet hoeveel herhalingen er nodig zijn — de loop blijft draaien zolang de voorwaarde `True` is.

```python
pogingen = 0

while pogingen < 3:
    print(f"Poging {pogingen + 1}")
    pogingen += 1
```

> **Let op:** Python kent geen `pogingen++`. Je schrijft `pogingen += 1` (of voluit `pogingen = pogingen + 1`). Vergeet je dit, dan blijft de voorwaarde altijd waar en krijg je een oneindige loop.

Het echte krachtsnummer van Python's `for`-loop is dat je er direct mee door een lijst kunt lopen, zonder index of teller:

```python
vakken = ["Python", "JavaScript", "PHP", "HTML"]

for vak in vakken:
    print(vak)
```

Dit is vergelijkbaar met `foreach` uit andere talen, maar in Python is dit gewoon hoe een `for`-loop standaard werkt.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Loops**: print met een `for`-loop en `range()` de tafel van 7 (1 t/m 10), en gebruik daarna een `for`-loop om een lijst van drie eigen favoriete talen te tonen.
