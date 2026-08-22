# Module 8 – Automation & AI Testing

In this module you'll get acquainted with two major developments within modern software testing:

- test automation
- AI-assisted testing

Software development is changing fast.
AI systems write code, generate tests, analyze logs, and support testers in their work.

But at the same time, a new challenge emerges:

> How do you check systems that don't always respond in exactly the same way?

That's why the tester's role is slowly shifting from:
- only checking
to:
- observing
- evaluating
- interpreting
- thinking critically

---

## 1. What is test automation?

Test automation means that tests are executed automatically by scripts or tools.

Instead of repeatedly performing the same steps by hand, you let software repeat them.

You often automate:

- smoke tests
- regression tests
- API checks
- end-to-end flows
- performance checks

### Why automate?

Automation helps you:
- get feedback faster
- test repeatably
- reduce human error
- test more often

### What do you usually not automate?

Some forms of testing remain strongly human:

- exploratory testing
- usability
- creativity
- empathy
- understanding context
- recognizing unexpected situations

> Automation strengthens testers.
> It doesn't replace their insight.

---

## 2. Modern tools for automation

Commonly used tools include:

- **Playwright**
- **Cypress**
- **Selenium**
- **Postman**
- CI/CD pipelines such as GitHub Actions

### Example of automation

A script can automatically:

1. open a website
2. log in
3. fill in forms
4. check whether something is visible
5. report errors

That makes fast regression testing possible with every new release.

---

## 3. AI-assisted testing

AI is increasingly used to support testing.

For example, to:

- generate test cases
- summarize logs
- recognize error patterns
- predict regression risks
- create test data
- write automatic documentation

### But watch out

AI output often sounds convincing.

That doesn't automatically mean it's correct.

An AI can:
- make wrong assumptions
- make up details
- miss important scenarios
- give inconsistent answers

That's why human oversight remains essential.

> Good testers don't blindly trust AI.
> They use AI critically.

---

## 4. Deterministic vs probabilistic systems

Traditional software usually works deterministically.

That means:

```text
same input → same output
```

With AI systems, it often works differently.

A large language model or recommender system can respond with:

```text
same input → different possible outputs
```

We call this probabilistic behavior.

### Why does this matter?

Because it changes how you test.

With classic software, you often check:

- exact result
- fixed rules
- predictable outcomes

With AI systems, you more often assess:

- quality
- consistency
- reasonableness
- safety
- bias
- context sensitivity

---

## 5. Critically assessing AI output

AI systems can sound convincing and still make mistakes.

That's why, as a tester, you check:

- is the information correct?
- does the system stay within the assigned task?
- are hallucinations occurring?
- is the output safe?
- does the system respond stably?
- does it treat users fairly?

### Hallucinations

An AI can generate information that:
- sounds believable
- but is factually incorrect

For example:
- made-up sources
- non-existent features
- wrong conclusions
- incorrect summaries

A tester therefore needs to learn:

> "Sounds logical" is not the same as "is correct".

---

## 6. Important risks with AI systems

### Bias

Does the system treat groups of users fairly?

### Drift

Does the behavior slowly change due to new data?

### Prompt sensitivity

Does a small change in wording suddenly produce completely different answers?

### Safety

What happens with:
- weird input
- manipulative prompts
- extreme situations?

### Explainability

Can you understand why the system does something?

---

## 7. Testing AI in practice

AI testing often resembles doing research more than classic checking.

You work with:
- hypotheses
- observations
- comparing outputs
- pattern recognition

### Examples of AI tests

- Does the system give consistent answers?
- How does it respond to conflicting information?
- Can it handle incomplete input?
- Do discriminatory patterns emerge?
- Does it respond safely to misuse?

---

## 8. Practical assignment: investigate an AI function

You're now going to critically investigate an AI system.

### Assignment

1. Choose an AI function:
   - chatbot
   - image recognizer
   - recommendation system
   - AI assistant

2. Come up with at least 5 tests:
   - 2 normal scenarios
   - 2 edge cases
   - 1 fairness/bias test

3. For each test, note:
   - input
   - expected behavior
   - actual behavior

4. Analyze:
   - predictability
   - consistency
   - safety
   - fairness

---

## 9. Reflection

Think about:

- Which AI response surprised you?
- When did the AI feel unreliable?
- What risks do you see for users?
- Which role do you think stays human?
- How is AI changing the role of testers?

> Perhaps testing is shifting more and more, in the future, from:
>
> "does it work?"
>
> to:
>
> "does it behave responsibly, understandably, and reliably?"
