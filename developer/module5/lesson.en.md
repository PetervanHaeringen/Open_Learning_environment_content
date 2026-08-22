# Module 5 — Programming without a computer

You don't understand code by reading it. You understand it by *doing* it.
In this module you'll act out algorithms — with cards, roles, and your own body.

---

## Materials

- Cards or post-its (at least 20)
- Markers
- Participants: 3 to 8 people
- Optional: tape on the floor for "memory spots"

---

## Game roles

| Role | Task |
|-----|------|
| **Processor** | Executes the instructions — one by one |
| **Memory** | Holds cards with values (variables) |
| **Input** | Provides new values when the program asks for them |
| **Output** | Writes down what the program "prints" |
| **Program** | Reads the instructions aloud, one at a time |

---

## Game 1 — Variables and addition

**The program:**
```
1. Store the value 5 as "x"
2. Store the value 3 as "y"
3. Calculate x + y
4. Store the result as "sum"
5. Print "sum"
```

**Gameplay:**
- Memory writes "x = 5" on a card and holds it
- Memory writes "y = 3" on a card and holds it
- Processor asks Memory: "What is x?" → Memory shows the card
- Processor asks: "What is y?" → Memory shows the card
- Processor calculates 5 + 3 = 8
- Memory writes "sum = 8" on a new card
- Output writes "8" on the board

**Debrief:** What happens if you change "x = 5" to "x = 10" in step 1? Who adjusts what?

---

## Game 2 — Condition (if/else)

**The program:**
```
1. Ask the user for a number → store as "number"
2. If number is greater than 10:
       print "big"
   Otherwise:
       print "small"
```

**Gameplay:**
- Input picks a number (e.g. 7) and writes it on a card
- Memory stores it as "number = 7"
- Processor asks: "Is 7 greater than 10?" → No
- Processor goes to the "Otherwise" branch
- Output writes "small"

Play it three times with different numbers. What changes in the Processor's behavior?

---

## Game 3 — Loop (repetition)

**The program:**
```
1. Store the value 1 as "counter"
2. While counter is less than or equal to 5:
       print counter
       increase counter by 1
3. Done
```

**Gameplay:**
- Memory starts with "counter = 1"
- Processor checks: is 1 ≤ 5? Yes → output writes "1", counter becomes 2
- Processor checks: is 2 ≤ 5? Yes → output writes "2", counter becomes 3
- ... (continue until counter = 6)
- Processor checks: is 6 ≤ 5? No → stop

**Debrief:** What would happen if we'd forgotten step 3 — "increase counter by 1"? Try it out.

*(This is an **infinite loop** — the program never stops. This is a common mistake.)*

---

## Game 4 — Sorting (acting out an algorithm)

This is a classic: **Bubble Sort**.

**Setup:**
- Write 5 random numbers on cards: e.g. 4, 1, 7, 2, 9
- Lay them out in a row on the table

**The algorithm:**
```
Repeat until nothing changes anymore:
    For each pair next to each other:
        If the left number is greater than the right one:
            Swap them
```

**Gameplay:**
- Round 1: compare 4 and 1 → 4 > 1, swap → [1, 4, 7, 2, 9]
- Compare 4 and 7 → 4 < 7, don't swap
- Compare 7 and 2 → 7 > 2, swap → [1, 4, 2, 7, 9]
- Compare 7 and 9 → 7 < 9, don't swap
- Round 2: start over from the beginning...
- Keep going until a full round produces no more swaps

**Debrief:**
- How many rounds did you need?
- What's the "worst case" — which order requires the most steps?
- Can you think of a faster approach?

---

## Connecting to real code

After these games, you'll recognize the concepts when you encounter them in code:

| What you did in the game | In code |
|--------------------------|---------|
| Holding a card with a value | `x = 5` (variable) |
| "If this, then that" | `if / else` |
| Repeating until a condition no longer holds | `while` loop |
| Going through a row | `for` loop |
| Forgetting a step so it doesn't stop | infinite loop (bug) |

In the next module, you'll write all of this yourself — but in a real language.
