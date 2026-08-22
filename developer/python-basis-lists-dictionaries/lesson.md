# Python — Lists & Dictionaries

Python kent twee vormen om meerdere waarden bij elkaar te houden: de **list** (genummerd) en de **dictionary** (met eigen sleutelnamen).

Een **list** werkt zoals een array in andere talen — elk element heeft een positie, beginnend bij `0`.

```python
vakken = ["Python", "JavaScript", "PHP", "HTML"]

print(vakken[0])       # Python
print(vakken[2])       # PHP
print(len(vakken))     # 4 — het aantal elementen
```

Je kunt eenvoudig iets aan een list toevoegen met `.append()`:

```python
vakken.append("CSS")
print(vakken)   # ['Python', 'JavaScript', 'PHP', 'HTML', 'CSS']
```

Een **dictionary** gebruikt zelfgekozen sleutels (keys) in plaats van getallen — vergelijkbaar met een object in JavaScript of een associatieve array in PHP.

```python
cursist = {
    "naam": "Anna",
    "leeftijd": 22,
    "track": "developer",
}

print(cursist["naam"])    # Anna
print(cursist["track"])   # developer
```

Door een dictionary te combineren met een `for`-loop doorloop je snel alle sleutel-waarde-paren met `.items()`:

```python
for sleutel, waarde in cursist.items():
    print(f"{sleutel}: {waarde}")
```

> **Tip:** Gebruik een list voor een simpele opsomming (zoals namen of taken). Gebruik een dictionary zodra elk stukje data een eigen betekenis heeft (zoals "naam", "leeftijd", "track" bij één cursist).

## Praktijkopdracht

Deze module hoort bij **Opdracht — Lists & Dictionaries**: maak een list met drie favoriete gerechten en print die met een `for`-loop, en maak daarna een dictionary voor jezelf (naam, leeftijd, hobby) en print elk sleutel-waarde-paar met `.items()`.
