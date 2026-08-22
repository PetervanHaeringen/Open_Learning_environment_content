# Module 4 — Comparing languages

There are hundreds of programming languages. You don't need to know them all.
But you do need to understand why there are so many — and how to choose.

---

## 1. The same problem, three languages

Let's start with a simple algorithm: determine whether a number is even or odd.

**Pseudocode** — not a real language, just writing down the idea:
```
if number is divisible by 2:
    print "even"
else:
    print "odd"
```

**Python:**
```python
number = 7
if number % 2 == 0:
    print("even")
else:
    print("odd")
```

**JavaScript:**
```javascript
let number = 7;
if (number % 2 === 0) {
    console.log("even");
} else {
    console.log("odd");
}
```

The idea is identical. The spelling differs.

Notice: Python uses indentation (whitespace) to mark blocks. JavaScript uses curly braces `{}`. Both work — they're just different choices made by the language designers.

---

## 2. The big names and what they're used for

| Language | Strong at | Typically used for |
|------|----------|-----------------------|
| Python | readability, data, AI | scripts, data analysis, backend, education |
| JavaScript | browser, interactivity | websites, frontend, also backend (Node.js) |
| Java | stability, large systems | business software, Android |
| C / C++ | speed, hardware control | operating systems, game engines, embedded |
| SQL | querying databases | any application with a database |
| HTML/CSS | structure and style | web pages (not a programming language, but still code) |
| PHP | web servers | WordPress, many existing websites |
| Swift / Kotlin | mobile | iOS (Swift), Android (Kotlin) |

There's no "best" language. Every language is a tool. You choose based on the problem.

---

## 3. How do you read unfamiliar code?

Throughout your career you'll constantly run into code you've never seen before.
That's normal. The skill isn't knowing everything — it's being able to read the main flow.

**Strategy:**
1. Find the structure: where do blocks begin? Where do they end?
2. Find the intent: what is this code trying to do?
3. Find the input and output: what goes in, what comes out?
4. Find familiar patterns: if/else, loops, functions — these look similar in every language

**Example — unfamiliar language (Ruby):**
```ruby
number = 7
if number % 2 == 0
  puts "even"
else
  puts "odd"
end
```

You might not know Ruby. But you recognize `if`, `else`, `% 2`, and the idea of output.
You understand what this does without ever having learned Ruby.

---

## 4. JavaScript in the browser — try it yourself

JavaScript has a special advantage: every computer with a browser already has a JavaScript environment built in.

**Here's how to open it:**
1. Open Chrome, Firefox, or Edge
2. Press F12 (or right-click → "Inspect")
3. Click the "Console" tab
4. Type JavaScript here and press Enter

Try:
```javascript
console.log("Hello world");
```

And then:
```javascript
let x = 5;
let y = 3;
console.log(x + y);
```

The browser executes it immediately. No installation, no configuration.

---

## 5. Python — the language that reads like English

Python was designed with one clear goal: **readability**.

Its creator, Guido van Rossum, wrote a language in 1991 where whitespace has meaning, where you don't need semicolons, and where code reads almost like prose.

```python
names = ["Ali", "Fatima", "Jonas"]

for name in names:
    print("Hello, " + name)
```

This does exactly what it says: for each name in the list, print a greeting.

Python is popular in education, data analysis, AI, and scripting. It's the language you choose when you want to build something quickly and readability matters.

---

## 6. Which language should you learn first?

The honest answer: it matters less than you think.

If you learn JavaScript, you'll understand Python faster afterward. If you learn Python, you'll understand JavaScript faster afterward. The core concepts — variables, conditions, loops, functions — are present in every language.

Choose based on:
- **What you want to build** — a website? JavaScript. Analyze data? Python. An app? Swift or Kotlin.
- **What your environment uses** — if your colleagues write Python, start with Python.
- **What motivates you** — you learn faster with a language that excites you.

In this course we use JavaScript for browser exercises (no installation needed) and Python for backend concepts.
