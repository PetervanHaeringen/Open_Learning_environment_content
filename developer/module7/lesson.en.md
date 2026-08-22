# Module 7 — Making and reading errors

Every program you write will go wrong at some point.
That's not a big deal — it's inevitable. The question isn't *whether* you make mistakes, but how quickly you find and fix them.

Good developers aren't people who don't make mistakes. They're people who read errors fast.

---

## 1. Three kinds of errors

**Syntax error (SyntaxError)**
The code is grammatically incorrect — the language doesn't understand it.

```javascript
console.log("Hello"   // missing closing parenthesis
```
```
Uncaught SyntaxError: Unexpected end of input
```

The interpreter can't even start running the code. Look for missing parentheses, quotation marks, or curly braces.

---

**Runtime error**
The code is grammatically correct, but goes wrong during execution.

```javascript
let number = null;
console.log(number.toString());
```
```
Uncaught TypeError: Cannot read properties of null
```

The code looks valid but tries to do something that's not possible — in this case, calling a method on `null`.

---

**Logic error**
The code runs without any error message, but doesn't do what you meant.

```javascript
function average(a, b) {
    return a + b / 2;   // bug: only divides b by 2
}

console.log(average(4, 6));  // gives 7, not 5
```

This is the trickiest kind of error — the computer doesn't complain. You have to discover for yourself what's wrong.

---

## 2. Reading error messages

An error message isn't an attack. It's information.

```
Uncaught TypeError: names.push is not a function
    at <anonymous>:3:7
```

Read it in three steps:

1. **Error type** — `TypeError`: something has the wrong type
2. **Description** — `names.push is not a function`: the variable `names` doesn't have a `push` method
3. **Location** — `at <anonymous>:3:7`: line 3, character 7

Always start with the first error message. Sometimes one error triggers a cascade of other messages.

---

## 3. Debugging as a thought process

Debugging is scientific thinking: form a hypothesis, test it, draw a conclusion.

**Step 1 — Reproduce the problem**
Can you reliably make the problem occur? If you don't know when it goes wrong, you can't fix it.

**Step 2 — Isolate the problem**
Shrink the code down until you have the smallest version that still fails. Less code is easier to understand.

**Step 3 — Form a hypothesis**
"I think it goes wrong because variable x is empty at this point."

**Step 4 — Test the hypothesis**
Add `console.log` to see what the values are:

```javascript
function calculateDiscount(price, percentage) {
    console.log("price:", price);           // check input
    console.log("percentage:", percentage);  // check input
    let discount = price * percentage / 100;
    console.log("discount:", discount);        // check calculation
    return price - discount;
}
```

**Step 5 — Adjust and test again**
Was your hypothesis correct? If not, form a new one.

---

## 4. Common mistakes and how to fix them

| Error | Cause | Fix |
|------|---------|-----------|
| `is not defined` | Variable doesn't exist or the name is misspelled | Check the name and whether `let` was used |
| `is not a function` | Calling something that isn't a function | Check the type of the variable |
| `Cannot read properties of null` | Calling a method on null/undefined | Check whether the variable has a value |
| `SyntaxError` | Missing parenthesis, quotation mark, or curly brace | Count the parentheses — are they closed? |
| Infinite loop | Stop condition never becomes false | Check whether the variable in the condition changes |

---

## 5. Fixing broken programs

Below are three pieces of broken code. Find the bug and fix it.

**Broken program 1:**
```javascript
function greet(name) {
    console.log("Hello, " + name)
}

greet("Ali"
```

**Broken program 2:**
```javascript
let score = "95";

if (score >= 90) {
    console.log("Passed");
}
```
*(Hint: `score` is a string, not a number. What does `>=` do with a string?)*

**Broken program 3:**
```javascript
function multiply(a, b) {
    return a + b;
}

console.log(multiply(3, 4));  // expected 12, gives 7
```

---

## 6. The mindset of a debugger

The best developers don't get grumpy about errors — they get curious.

An error means: *the computer is telling you something about your own code that you didn't know yet.*

That's valuable. Every bug you fix makes you better at avoiding that same mistake next time.

> "Debugging is like being the detective in a crime story where you're also the murderer."
