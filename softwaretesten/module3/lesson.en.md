# Module 3 – Test Plan & Risk Analysis

In this module you'll learn the basics of a lightweight test plan.

Not thick documents, but a practical summary of:

**what are we going to test, why, how, and when is it good enough?**

---

## 1. What is a test plan?

A test plan is a short document that gives direction to testing.

It describes:

- what needs to be tested
- which risks matter
- which approach is chosen

In modern projects, and certainly in TestGarden, we keep test plans as simple as possible.

Often one page is already enough.

### A test plan usually contains

- Scope — what do we test, and what don't we?
- Main risks
- Approach — smoke tests, test cases, exploratory testing
- Test environment
- Entry & Exit criteria
- Roles — who does what?

---

## 2. What is risk-based testing?

Risks help you decide which parts are most important to test.

A risk arises when a **possible bug** is combined with **impact**.

We use a simple formula:

> **Risk = probability × impact**

The higher the risk, the more attention a part needs in your test plan.

### Webshop example

- "View product" page → low impact
- "Checkout" page → high impact

That's why the checkout process gets more, and deeper, testing.

---

## 3. Example of a 1-page test plan

Use this as a base when you write your own test plan.

```text
Title: Test plan for [component/app]
Date:
Author:

1. Scope:
   - What do we test?
   - What don't we test?

2. Main risks:
   - R1: [risk + reason]
   - R2: [risk + reason]

3. Approach:
   - Smoke tests
   - Test cases
   - Exploratory testing

4. Test environment:
   - URL, data, accounts

5. Entry criteria:
   - Build works
   - Test data available

6. Exit criteria:
   - No open P1/P0 bugs
   - Smoke test passed

7. Roles:
   - Tester(s)
   - Coach / Product owner
```

---

## 4. Practical assignment: Make your own mini test plan

You're now going to write your first test plan for a small part of the demo app.

### Assignment

1. Choose one part of the demo app, for example registration.
2. Identify 3 risks using probability × impact.
3. Describe what you're going to test (*scope*).
4. Choose your approach:
   - smoke testing
   - test cases
   - exploratory testing
5. Fill in the full 1-page test plan template.

> **Tip:**
> Keep it short, clear, and practical.
> A test plan isn't a report — it's your compass.

---

## 5. Reflection

Think about your test plan:

- Which risks were the most important?
- What did you leave *out* of scope, and why?
- Would you want to add more or less detail?

Try to figure out:

- which choices were deliberate
- which parts got extra attention
- and how your approach would change with a larger application
