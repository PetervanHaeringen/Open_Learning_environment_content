# Module 2 — Test Levels & Smoke Testing

In this module you'll discover how software testing happens in different layers, and what the role is of the well-known **smoke test**.

We'll go from overview to practice, so you understand how your test work fits into the bigger picture.

---

## 1. What are test levels?

Software isn't tested all at once. Each part is checked at a different level.

We call these levels **test levels**.

- **Unit Testing** — small pieces of code, tested by developers
- **Integration tests** — does everything work together as intended?
- **System tests** — does the whole application work as a whole?
- **Acceptance tests** — does it work for the user and the client?

### Example

In a webshop:

- unit test → does the discount calculation work?
- integration test → do the shopping cart and inventory work together?
- system test → does the ordering process work end-to-end?
- acceptance test → does the customer find the flow logical and usable?

---

## 2. Test types: functional & non-functional

Besides test levels, you also have **test types**.

This describes *what* you're testing.

- **Functional testing** — does the function do what it's supposed to do?
- **Non-functional testing** — speed, security, ease of use, stability

In TestGarden we mainly focus on functional testing, such as smoke tests and exploratory testing.

---

## 3. What is a Smoke Test?

A smoke test is a **short, quick check** to see whether the system is "roughly healthy" after a new release, update, or deploy.

It's the digital equivalent of:

> "is the smoke alarm going off?"

If something fundamental is broken, you want to know right away.

### Why smoke tests?

- They're fast and give immediate clarity
- They prevent wasting time on broken builds
- They give a GO / NO-GO for further testing

### Example of a smoke test

- Does the application load?
- Can the user log in?
- Does the main flow work?
- Are there no 404 or 500 errors?

---

## 4. Example Smoke Test Checklist

- [ ] Is the website reachable?
- [ ] Can a test user log in?
- [ ] Does the main functionality work?
- [ ] Do the main links and buttons work?
- [ ] Are there no major errors visible?
- [ ] Does it also work on mobile or a different browser?

You close out a smoke test with:

**GO / NO-GO**

---

## 5. Practical assignment

1. Choose a demo web app
2. Create a smoke checklist
3. Run the checklist
4. Note Pass / Fail
5. Write a conclusion

> A smoke test is not a complete test.
> It's a quick health scan.

---

## 6. Reflection

Think about:

- Which check was the most important?
- Which problem was the biggest risk?
- How would you improve your checklist?
