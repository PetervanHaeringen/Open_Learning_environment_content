# Module 10 — Black-box test techniques

So far you've mainly learned *that* you test. This module is about *how* you smartly choose *what* you test. Because you can't possibly test everything — there are usually infinitely many possible inputs. The art is finding the bugs with a small, cleverly chosen set of test cases.

---

## 1. Black-box: testing without looking at the code

With **black-box testing**, you treat the program as a black box: you know what goes in and what should come out, but you don't look at the code inside. You test whether the behavior matches what was promised — the specification.

The opposite is **white-box testing**, where you *do* look at the internal code to determine what you test. Both have their place. Black-box is powerful because your test cases keep working even if the code inside gets completely rewritten — as long as the promised behavior stays the same.

In this module we cover four commonly used black-box techniques:
- Equivalence classes
- Boundary value analysis
- Decision tables
- State transitions

---

## 2. Equivalence classes: groups that get treated the same way

Imagine: a website only lets people aged 18 or older create an account. Age can range from 0 to roughly 120. Do you now have to test all 121 ages? No.

The idea behind **equivalence classes** is that the program treats large groups of input in exactly the same way. For the age check, there are really only two groups:
- **too young**: 0 through 17 (gets rejected)
- **old enough**: 18 through 120 (gets accepted)

Within each group, it doesn't matter which value you pick — if 25 works, 40 probably works too. So you test one value per group. For example, age 10 (too young) and age 30 (old enough). Two test cases instead of 121.

A **valid class** contains values that should be accepted, an **invalid class** contains values that should be rejected. Important: don't forget the invalid classes. A program that handles good input nicely but crashes on bad input is still broken.

---

## 3. Boundary value analysis: bugs live at the edges

Programmers don't make most of their mistakes in the middle of a group, but at the **boundaries** between groups. Is it `>= 18` or `> 18`? That one-year difference is exactly where things often go wrong.

**Boundary value analysis** therefore focuses on the edges of an equivalence class. At the age boundary of 18, the interesting values are:
- **17** — just too young (last value of the rejected group)
- **18** — just old enough (first value of the accepted group)

By testing exactly these two, you catch the classic "just does / just doesn't" error. A programmer who accidentally wrote `> 18` instead of `>= 18` would wrongly reject an 18-year-old — and your test at age 18 catches that.

Some testers also include the value one step further out (16, 17, 18 or 17, 18, 19) to be even more certain. The more boundary values you include, the more thorough — but also the more work. It's a trade-off.

Note: boundary value analysis only works with **ordered** input, where "greater than" and "less than" have meaning — numbers, dates, amounts. With unordered input (such as a choice between red, green, or blue), there is no boundary.

---

## 4. Decision tables: when multiple conditions come together

Sometimes a program's behavior depends on a combination of conditions. A webshop, for example, gives a discount according to these rules:
- Member of the customer club? **and**
- Order above 50 euros?

With two conditions, each of which can be true or false, there are four combinations. A **decision table** lays these out neatly:

| Member? | Above 50 euros? | Discount |
|------|----------------|---------|
| yes  | yes            | 10%     |
| yes  | no             | 5%      |
| no   | yes            | none    |
| no   | no             | none    |

Each column (or row, in this layout) is a separate rule that you test. The power of a decision table is that you systematically go through *all* combinations — including the one you might otherwise forget. Moreover, building it forces you to sharpen whether the rules are actually complete and without contradiction.

With two conditions there are four combinations, with three already eight, with four sixteen — it keeps doubling. With many conditions this becomes unworkable, and you choose the most important combinations based on risk.

---

## 5. State transitions: behavior that depends on history

Some systems behave differently depending on where they currently are — their **state**. Think of a simple traffic light: red → green → yellow → red. Or an online order: *draft → placed → shipped → delivered*.

With **state transition testing**, you test whether the system moves cleanly from one state to another when something happens (an *event*), and — just as importantly — whether it does *not* transition on forbidden actions.

Example: an order that has already been shipped should no longer be cancellable. That's an **invalid transition**. A good tester actually tries out those forbidden steps, because that's often where the most dangerous bugs live: a system that still lets you cancel a shipped package can lead to real problems.

So you test two things:
- the **valid transitions**: do they all happen correctly?
- the **invalid transitions**: are they all properly rejected?

---

## 6. Which technique, when?

No single technique is "the best" — they complement each other:
- **Equivalence classes** when there are groups of input treated the same way.
- **Boundary value analysis** as soon as ordered boundaries are involved (ages, amounts, dates).
- **Decision tables** when behavior depends on combinations of conditions.
- **State transitions** when behavior depends on where the system currently is.

In practice you combine them. For the age check, you use equivalence classes and boundary values together. An experienced tester senses which technique fits which problem — and you develop that sense through practice.

---

> **On your way to a certification?**
> These techniques form the core of internationally recognized entry-level test certifications, such as ISTQB Foundation. TestGarden prepares you for the concepts; you take the official exam through a recognized body (in the Netherlands and Belgium, the BNTQB). Discuss with your coach and at home whether and when that step is right for you.
