# Python — Functions

Een functie is een herbruikbaar stukje code met een naam. In Python definieer je een functie met het sleutelwoord `def`, gevolgd door de naam, haakjes en een dubbele punt — en de inhoud staat weer ingesprongen, net als bij `if`.

```python
def begroet():
    print("Hallo!")

begroet()   # roept de functie aan
```

Met **parameters** geef je waarden mee bij het aanroepen:

```python
def begroet_persoon(naam):
    print(f"Hallo, {naam}!")

begroet_persoon("Anna")
begroet_persoon("Bart")
```

Je kunt een parameter een **standaardwaarde** geven, die gebruikt wordt als er niets wordt meegegeven:

```python
def begroet_persoon(naam="gast"):
    print(f"Hallo, {naam}!")

begroet_persoon()          # Hallo, gast!
begroet_persoon("Cynthia") # Hallo, Cynthia!
```

Er is een belangrijk verschil tussen `print` en `return` in een functie: `print()` toont direct iets in de terminal, terwijl `return` een waarde teruggeeft die je daarna zelf verder kunt gebruiken — opslaan in een variabele, doorrekenen, of ergens anders in je programma inzetten.

```python
def optellen(a, b):
    return a + b

resultaat = optellen(4, 6)
print(f"De som is: {resultaat}")
```

> **Tip:** Gebruik `return` als je de uitkomst van een functie nog verder wilt gebruiken in je code. Gebruik `print()` alleen als het echt de bedoeling is om direct iets in de terminal te tonen. Een functie zonder `return` geeft in Python automatisch `None` terug.

## Praktijkopdracht

Deze module hoort bij **Opdracht — Functions**: schrijf een functie `bereken_totaal(prijs, aantal)` die met `return` het totaalbedrag teruggeeft, en print het resultaat daarna apart met `print()`.
