# Module 6 — Building blocks of a program

You've felt algorithms with your hands. Now you're going to write them down.
Open the browser console (F12 → Console) and type along as you read.

---

## 1. Variables — giving values a name

A variable is a name that holds a value.

```javascript
let name = "Ali";
let age = 23;
let active = true;
```

- `let` creates a new variable
- `name`, `age`, `active` are the names
- The values to the right of `=` get stored

Type this in the console and press Enter after each line.
Then type `name` and press Enter — the console shows "Ali".

**Three kinds of values:**
- Text (string): `"Ali"` — always between quotation marks
- Number: `23` — no quotation marks
- True/false (boolean): `true` or `false`

---

## 2. Conditions — making decisions

```javascript
let temperature = 22;

if (temperature > 25) {
    console.log("Warm — bring water");
} else {
    console.log("Cool — a jacket comes in handy");
}
```

Type this in the console. Then change `22` to `30` and run it again.

The structure is always:
```javascript
if (condition) {
    // do this if the condition is true
} else {
    // do this if the condition is not true
}
```

**Comparison operators:**
| Operator | Meaning |
|----------|-----------|
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |
| `===` | exactly equal to |
| `!==` | not equal to |

---

## 3. Loops — repeating

**For-loop** — when you know how many times you want to repeat something:

```javascript
for (let i = 1; i <= 5; i++) {
    console.log("Step " + i);
}
```

This prints "Step 1" through "Step 5".

The three parts between the parentheses:
1. `let i = 1` — start at 1
2. `i <= 5` — keep going as long as i is less than or equal to 5
3. `i++` — increase i by 1 after each step

**While-loop** — when you don't know how many times:

```javascript
let counter = 1;

while (counter <= 5) {
    console.log("Counter is now: " + counter);
    counter++;
}
```

Same result, different way of writing it. Use `while` when the stopping condition depends on something that changes during the program.

---

## 4. Functions — reusable blocks

A function is a block of code with a name. You write it once and use it many times.

```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("Ali");
greet("Fatima");
greet("Jonas");
```

The function `greet` expects a **parameter** — `name`.
Each time you call the function, you pass in a different value.

**Functions that return a value:**

```javascript
function square(number) {
    return number * number;
}

let result = square(4);
console.log(result);
```

`return` sends a value back. You can store it or use it directly.

---

## 5. Putting it all together — a mini program

```javascript
function grade(score) {
    if (score >= 90) {
        return "Excellent";
    } else if (score >= 70) {
        return "Good";
    } else if (score >= 55) {
        return "Passing";
    } else {
        return "Failing";
    }
}

let scores = [88, 42, 95, 67, 55];

for (let i = 0; i < scores.length; i++) {
    let judgment = grade(scores[i]);
    console.log("Score " + scores[i] + ": " + judgment);
}
```

Type this into the console. See what happens.
Then change one score and run it again.

This is a real program: it has input, processing, and output.

---

## 6. Exercises

Try these assignments in the browser console:

**Assignment 1:** Write a function `isEven` that returns `true` if a number is even, and `false` if it's odd. Test it with the numbers 4, 7, 12, and 9.

**Assignment 2:** Write a loop that prints the 3 times table (3, 6, 9, ... up to and including 30).

**Assignment 3:** Create a list of five names. Loop through the list and print each name with "Welcome, [name]!".

*Tip: Use `let names = ["name1", "name2", ...]` for a list (array).*
