# Module 4 – Test Techniques

In this module you'll learn how to design good test cases.

Not "just clicking around randomly", but structured, smart, and creative testing.

These techniques help you find bugs you'd otherwise never see.

---

## 1. Why test techniques?

Test techniques help you test **more deliberately, more completely, and more intelligently**.

They make sure you don't just test the "happy paths", but also:
- error scenarios
- weird input
- boundary values

A good tester uses techniques to:
- find more bugs
- test more efficiently
- show that thought went into the test cases
- create repeatable and clear test cases

---

## 2. Equivalence Partitioning (EP)

With Equivalence Partitioning (EP), you divide all possible input into groups ("partitions") that you expect to produce the same behavior.

### Example

An age field accepts ages between **18 and 65**.

Then the partitions are:

- Too young (0–17)
- Valid (18–65)
- Too old (66+)

> Instead of testing 48 possible valid ages, you just test 1.
> Less work, the same coverage.

---

## 3. Boundary Value Analysis (BVA)

Bugs often sit at the edges of input values.

Boundary testing therefore focuses on:
- minimums
- maximums
- values just over the boundary

### Example

Age 18–65 is valid.

Then you test:

- 17 (just too low)
- 18 (lowest valid)
- 65 (highest valid)
- 66 (just too high)

This technique finds many bugs that directly affect users.

---

## 4. Decision Tables

Use this when multiple rules or conditions apply at the same time.

You put everything in a table and create a test case for each combination.

### Example: logging in

| Username | Password | Expectation |
|---|---|---|
| Correct | Correct | Login OK |
| Correct | Wrong | Error message |
| Wrong | Correct | Error message |
| Wrong | Wrong | Error message |

---

## 5. State Transition Testing

Some systems change status.

For example:
- a user logs in or out
- an order changes status
- a workflow moves to the next step

Here you test:
- valid transitions
- invalid transitions
- what happens when steps get skipped

### Example: order status

#### Valid transitions
- Placed → Paid
- Paid → Shipped

#### Invalid transitions
- Shipped → Placed
- Shipped → Paid

---

## 6. Practical assignment: write 8 test cases

You're now going to create test cases yourself, for a login screen or input field of your choice.

Use at least two techniques.

### Assignment

1. Choose a component:
   - login
   - password reset
   - age field
   - or something else

2. Write 8 test cases with:
   - steps
   - expected result
   - technique used

3. Have a classmate run your test cases.

4. Improve your test cases based on the feedback.

> A good test case is:
> - short
> - clear
> - reproducible

---

## 7. Reflection

Think about your test cases:

- Which technique felt the most logical?
- What took the most time?
- Which technique did you find surprisingly effective?
