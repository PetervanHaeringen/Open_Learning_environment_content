# Module 3 — Languages and abstraction

When you write Python, you're not really talking to the computer.
You're talking to Python. Python talks to C. C talks to assembly. Assembly talks to the processor.

Every layer hides the complexity of the layer beneath it. That's called **abstraction** — and it's one of the most powerful ideas in computer science.

---

## 1. The computer only speaks zeros and ones

At the deepest level, a computer understands only one thing: current or no current. On or off. 1 or 0.

Every piece of code you'll ever write eventually gets converted into a long sequence of 1s and 0s — **machine language**.

A simple addition in machine language looks like this:
```
10110000 01100001
00000101 00000001
10100010 01100001
```

This is literally what the processor executes. Humans can't write or read this without making mistakes. That's why the next layer was invented.

---

## 2. Assembly — names for instructions

In the 1950s, programmers thought: why don't we give the most commonly used instructions names?

Instead of `10110000 01100001` you write:
```asm
MOV AL, 1
ADD AL, 1
MOV memory, AL
```

`MOV` means "move a value". `ADD` means "add".
These are the exact same instructions as the zeros and ones — but readable for humans.

An **assembler** converts assembly code into machine language.

Assembly was a huge step forward. But it stayed close to the hardware — you still had to know exactly how much memory you had, which registers were available, how the processor was built.

---

## 3. High-level languages — writing for humans

In the 1950s and 60s a new idea emerged: what if you write code that looks more like human language?

**FORTRAN** (1957) — for scientific calculations:
```fortran
X = A + B * C
```

**COBOL** (1959) — for business applications:
```cobol
ADD SALARY TO TOTAL-WAGES
```

**C** (1972) — compact, powerful, close to the hardware but readable:
```c
int sum = a + b;
```

**Python** (1991) — so readable it's almost English:
```python
sum = a + b
```

Each generation of languages became more readable. And each step hid more complexity.

![Layers of abstraction in programming languages](/instructions/content-images/developer/module3/lagen_abstractie.svg)

---

## 4. Compilers and interpreters — the translators

How does readable code reach the processor?

Through a **compiler** or an **interpreter**.

**Compiler** — translates the entire code into machine language in one go, before the program runs.
Advantage: the program is fast.
Disadvantage: you have to recompile with every change.
Examples: C, C++, Rust.

**Interpreter** — translates the code line by line while the program is running.
Advantage: you see the result of a change immediately.
Disadvantage: slightly slower.
Examples: Python, JavaScript, Ruby.

Most languages you'll encounter as a developer are interpreted — both Python and JavaScript are. That's convenient for learning: you write a line, you see what happens.

---

## 5. Why is abstraction so powerful?

Imagine having to write the full machine-language code for displaying text on a screen every single time you build a website. You'd never get further than "Hello world."

Abstraction makes it possible to **build on what others have already built**.

Python is written in C.
C is written in assembly.
Assembly is written in machine language.
Machine language is executed by transistors.
Transistors are designed by electrical engineers.

You don't need to know any of that to write a program that does something useful. You use the layers that others have built.

That's also the philosophy behind open source: sharing code so the next person can build further.

---

## 6. The price of abstraction

But abstraction also has a price.

The higher the layer of abstraction, the less control you have over exactly what happens.
A C programmer can determine exactly how much memory a program uses.
A Python programmer delegates that to Python.

For most applications, that doesn't matter at all. But for systems where every millisecond counts — operating systems, game engines, embedded hardware — you choose a lower layer.

As a developer, you learn to choose which layer fits your problem.
