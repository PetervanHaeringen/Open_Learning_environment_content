# Python — Operators

Met rekenkundige operators reken je met getallen. De meeste ken je al van rekenles, maar Python heeft er twee extra die het overzichtelijk maken:

```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333333333333335  -> "gewone" deling, geeft altijd een float
print(a // b)   # 3                   -> gehele deling, rondt af naar beneden
print(a % b)    # 1                   -> modulo, de rest na deling
print(a ** b)   # 1000                -> machtsverheffen (a tot de macht b)
```

Het verschil tussen `/` en `//` is iets waar je in Python specifiek op moet letten: `/` geeft altijd een kommagetal terug, ook als de uitkomst netjes rond is. `//` (dubbele deling) rondt juist af naar het dichtstbijzijnde gehele getal naar beneden.

Voor vergelijkingen gebruik je operators die `True` of `False` teruggeven:

```python
print(5 == 5)    # True  -- gelijk aan
print(5 != 3)    # True  -- niet gelijk aan
print(5 > 3)     # True  -- groter dan
print(5 < 3)     # False -- kleiner dan
```

> **Verschil met JavaScript en PHP:** in Python bestaat er geen apart `===`. Python vergelijkt met `==` altijd zowel waarde als type in één keer, dus je hoeft daar niet over na te denken zoals bij JavaScript of PHP. Eén ding minder om te onthouden.

Ook logische combinaties schrijf je in Python met gewone woorden in plaats van symbolen:

```python
ingelogd = True
rol = "docent"

if ingelogd and rol == "docent":
    print("Welkom, docent.")
```

`and`, `or` en `not` doen precies wat je zou verwachten — en zijn voor veel mensen makkelijker te lezen dan `&&`, `||` en `!`.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Operators**: bereken met twee variabelen zowel `/` als `//`, en laat met `print()` zien wat het verschil in resultaat is. Vergelijk daarna twee waarden met `==` en `!=`.
