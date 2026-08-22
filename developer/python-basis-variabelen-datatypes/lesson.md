# Python — Variabelen & Datatypes

In Python maak je een variabele aan door gewoon een naam te typen, een `=`, en een waarde. Geen `let`, geen `$`, geen puntkomma nodig.

```python
naam = "Softpool"
leeftijd = 5
prijs = 19.95
actief = True

print(naam)
```

Python kent dezelfde basis-datatypes als de meeste talen:

- **str** — tekst, tussen `"..."` of `'...'`
- **int** — een heel getal, zoals `5`
- **float** — een kommagetal, zoals `19.95`
- **bool** — `True` of `False` (let op de hoofdletter — dat is anders dan JavaScript!)

Je kunt met `type()` altijd opvragen wat het datatype van een waarde is:

```python
print(type(leeftijd))   # <class 'int'>
print(type(naam))       # <class 'str'>
```

Om tekst en variabelen te combineren gebruik je in Python meestal een **f-string** — een string met een `f` ervoor, waarin je de variabele tussen accolades zet:

```python
naam = "Anna"
print(f"Welkom, {naam}!")
```

Dit is vergelijkbaar met interpolatie in andere talen, maar dan zonder speciale aanhalingstekens-regels: een f-string werkt altijd, met enkele én dubbele aanhalingstekens.

> **Tip:** Python is hoofdlettergevoelig. `naam` en `Naam` zijn twee verschillende variabelen — een veelgemaakte fout bij het overtypen van voorbeelden.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Variabelen & Datatypes**: leg drie variabelen vast (een str, een int en een bool), print met `type()` wat elk datatype is, en print daarna met een f-string een zin waarin je de str-variabele verwerkt.
