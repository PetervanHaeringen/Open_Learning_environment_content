# Module 1 — The human as programmer

Before we write a single line of code, let's pause on something people have been doing for thousands of years: telling other people and machines what to do.

Programming is a special form of that. But it didn't start with a computer.

---

<iframe width="560" height="315" 
src="https://www.youtube.com/embed/cDA3_5982h8?rel=0&modestbranding=1" 
frameborder="0" allowfullscreen></iframe>

## 1. The peanut butter experiment

Imagine: a child writes an instruction for their father.

> "Put peanut butter on the bread."

The father takes the jar of peanut butter. And places it on the bread. Without opening it. Without a knife. Exactly what it says.

The child becomes desperate. But the father didn't do anything wrong — he followed exactly what was written.

This experiment shows the core of programming: **the gap between what you mean and what you say**.

A human automatically fills in what's missing. A computer doesn't. A computer does exactly what you tell it — no more, no less, nothing in between.

![The gap between intention and instruction](/instructions/content-images/developer/module1/kloof_bedoeling_instructie.svg)

---

## 2. Instructions are everywhere

Long before computers, humans were already writing programs. We just called them something else.

**A recipe** is a program for a cook.
Ingredients are the input. The steps are the instructions. The dish is the output.

**A piece of sheet music** is a program for a musician.
The notes are instructions: which sound, how long, how loud, when.

**A law** is a program for a society.
If situation X occurs, then action Y follows.

**A chess strategy** is a program for a player.
If the opponent does this, then do that.

Each of these systems has something in common: they describe **what needs to happen, step by step, unambiguously**.

That's the core of an algorithm.

---

## 3. What makes an instruction precise?

Look at these two versions of the same recipe:

**Version A — vague:**
> "Put some flour in a bowl, add some water and mix it until it's good."

**Version B — precise:**
> "Put 200 grams of flour in a bowl. Add 120 ml of water. Mix for 3 minutes until the dough feels smooth and no longer sticks to the bowl."

Version A works for an experienced baker — they fill in the rest themselves.
Version B also works for someone who has never baked before.

A computer is always a beginner. You can never assume it "knows what you mean."

---

## 4. The other side: multiple paths to the same goal

But there's also the opposite problem.

Imagine: you ask someone to go from Amsterdam to Utrecht.
You're thinking of the A2 highway. They take the train. A third person cycles.

All three arrive. The instruction was correct. The execution differed.

This is something humans do but computers don't do on their own: **finding alternative paths to the same goal**.

As a developer, you learn to design this deliberately. Your program has to work, but there are always multiple ways to write it. Each with its own pros and cons.

---

## 5. What is an algorithm?

An algorithm is a sequence of steps that:
- has a beginning
- ends (always, not "maybe")
- has a clear next step for every situation
- gives the same result for the same input

That sounds formal. But you use algorithms every day.

How do you make tea?
1. Fill the kettle with water.
2. Turn on the kettle.
3. Wait until the water boils.
4. Pour the water over the tea bag.
5. Wait 3 minutes.
6. Remove the tea bag.
7. Done.

That's an algorithm. Step by step. Unambiguous. Repeatable.

---

## 6. Why is this the foundation of programming?

Every programming language — Python, JavaScript, Java, C — is ultimately a way to write down algorithms that a computer can execute.

The language is the spelling. The algorithm is the thought.

You can become an excellent developer without knowing every language. But you can't become a good developer without being able to think well in steps, in cases, in input and output.

That thinking starts here. Not at a terminal or a screen — but with the question: **how do I explain this so clearly that no misunderstanding is possible?**
