# Module 8 — Building something real

You know the building blocks. Now you're going to build something.

In this module you choose one of four projects and finish it. Not perfect — but working. And working is the only measure that counts.

---

## Choose your project

Choose the project that appeals to you the most.

---

### Project A — Quiz

A quiz that asks questions and keeps track of how many you got right.

**What it does:**
- Asks 3 or more questions
- Accepts an answer from the user
- Tells you whether it was right or wrong
- Gives the total score at the end

**Starting point:**
```javascript
let score = 0;

function askQuestion(question, correctAnswer) {
    let answer = prompt(question);
    if (answer.toLowerCase() === correctAnswer.toLowerCase()) {
        alert("Correct!");
        score++;
    } else {
        alert("Too bad. The correct answer was: " + correctAnswer);
    }
}

askQuestion("What is the capital of the Netherlands?", "Amsterdam");
askQuestion("What is 7 times 8?", "56");
askQuestion("Who wrote the first algorithm for a machine?", "Ada Lovelace");

alert("Your score: " + score + " out of 3");
```

**Extend it:**
- Add more questions
- Give feedback per question
- Randomize the questions with `Math.random()`

---

### Project B — Calculator

A calculator that computes with two numbers and an operation.

**What it does:**
- Asks for two numbers
- Asks which operation (+, -, *, /)
- Gives the result

**Starting point:**
```javascript
function calculate(a, b, operation) {
    if (operation === "+") return a + b;
    if (operation === "-") return a - b;
    if (operation === "*") return a * b;
    if (operation === "/") {
        if (b === 0) return "Cannot divide by zero";
        return a / b;
    }
    return "Unknown operation";
}

let number1 = Number(prompt("First number:"));
let number2 = Number(prompt("Second number:"));
let operation = prompt("Operation (+, -, *, /):");

let result = calculate(number1, number2, operation);
alert(number1 + " " + operation + " " + number2 + " = " + result);
```

**Extend it:**
- Let the user do multiple calculations in a row
- Add square root (`Math.sqrt()`)
- Keep a history of all calculations

---

### Project C — Text processor

A program that does something with text you enter.

**What it does:**
- Counts the number of words in a text
- Counts how many times a specific word appears
- Converts the text to uppercase or lowercase

**Starting point:**
```javascript
let text = prompt("Enter a text:");

let words = text.split(" ");
alert("Number of words: " + words.length);

let searchWord = prompt("Which word do you want to search for?");
let count = 0;
for (let i = 0; i < words.length; i++) {
    if (words[i].toLowerCase() === searchWord.toLowerCase()) {
        count++;
    }
}
alert("'" + searchWord + "' appears " + count + " times");
```

**Extend it:**
- Replace one word with another word
- Reverse the order of the words
- Count the number of sentences (hint: look for periods)

---

### Project D — Guess the number

A game where the computer picks a number and you have to guess it.

**What it does:**
- The computer picks a random number between 1 and 100
- The player guesses
- The program says "too high", "too low", or "correct"
- It counts how many attempts the player needed

**Starting point:**
```javascript
let secret = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
let guessed = false;

while (!guessed) {
    let guess = Number(prompt("Guess a number between 1 and 100:"));
    attempts++;

    if (guess < secret) {
        alert("Too low! Try higher.");
    } else if (guess > secret) {
        alert("Too high! Try lower.");
    } else {
        alert("Correct! You needed " + attempts + " attempts.");
        guessed = true;
    }
}
```

**Extend it:**
- Add a maximum number of attempts
- Give a rating based on the number of attempts
- Let the player play again without reloading the page

---

## How to approach this

**Step 1 — Choose and understand the starting point**
Read the code line by line. Can you explain what each line does?

**Step 2 — Get it working as-is**
Copy the starting point into the browser console and run it. Does it work?

**Step 3 — Adjust one thing**
Change one small value or add one line. Run it again.

**Step 4 — Extend it step by step**
Add one extension at a time. Test after each addition.

**Step 5 — Break it deliberately**
Change something so it fails. Read the error message. Fix it.

---

## What makes a good program?

- It does what it's supposed to do
- It gives clear feedback to the user
- It doesn't crash on unexpected input
- You can explain to others how it works

Perfectionism is the enemy of finished. Make it work — then you can improve it.
