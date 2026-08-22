# Python — Conditionals (if/elif/else)

Met `if`, `elif` en `else` laat je je code beslissingen nemen. De logica is hetzelfde als in elke andere taal — het grote verschil zit in de vorm.

```python
leeftijd = 16

if leeftijd >= 18:
    print("Je bent meerderjarig.")
elif leeftijd >= 12:
    print("Je bent een tiener.")
else:
    print("Je bent nog een kind.")
```

Twee dingen vallen meteen op als je van JavaScript of PHP komt:

1. **Geen haakjes verplicht** om de voorwaarde — `leeftijd >= 18:` is genoeg
2. **Geen accolades** `{ }` om aan te geven wat bij het if-blok hoort — in plaats daarvan gebruikt Python **inspringing** (indentatie)

Dat tweede punt is geen stijlkeuze — het is de syntax zelf. Alles dat bij elkaar hoort binnen een `if`, staat even ver ingesprongen (meestal 4 spaties). Zodra de inspringing stopt, is het blok voorbij. Verkeerd inspringen geeft een `IndentationError` — de eerste foutmelding die de meeste Python-beginners tegenkomen, en volkomen normaal.

```python
if leeftijd >= 18:
    print("Meerderjarig")
    print("Deze regel hoort ook bij het if-blok")
print("Deze regel hoort er NIET bij, want die springt niet in")
```

Voorwaarden combineer je, net als in de vorige module, met `and`, `or` en `not`:

```python
ingelogd = True
rol = "docent"

if ingelogd and rol == "docent":
    print("Welkom, docent.")
```

> **Tip:** Laat VS Code voor je inspringen — druk op Tab, niet op losse spaties, en de editor houdt het automatisch consistent. Mengen van tabs en spaties is een klassieke bron van `IndentationError`.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Conditionals**: schrijf een if/elif/else die op basis van een cijfer (variabele `score`) "voldoende", "twijfelachtig" of "onvoldoende" print, en laat bewust één regel verkeerd inspringen om de foutmelding een keer met eigen ogen te zien.
