# Module 8 — Git for testers

As a tester, you might use Git differently than a developer.
You work with test scripts, bug reports, findings, and documentation.
In this module you'll see how Git and GitHub directly support your work as a tester.

---

## 1. GitHub Issues: the heart of the workflow

An **issue** is a task, bug report, or question tracked in GitHub.

As a tester you create issues for:
- bugs you found
- test-related questions for the team
- requests for extra test data
- improvement suggestions for test scripts

**A good bug report as an issue contains:**

```markdown
## Description
Clicking the "Save" button on the form gives a 500 error.

## Steps to reproduce
1. Go to /formulier
2. Fill in all fields
3. Click "Save"

## Expected behavior
The form is saved and you get a confirmation.

## Actual behavior
Error message: Internal Server Error (500)

## Environment
- Browser: Chrome 124
- OS: Windows 11
- Test environment: staging
```

---

## 2. Labels: adding structure

Labels categorize issues.
Default labels in GitHub:

| Label | Use |
|-------|---------|
| `bug` | Something isn't working as expected |
| `enhancement` | Improvement suggestion |
| `question` | Question for the team |
| `documentation` | Documentation is missing or incorrect |
| `duplicate` | Already reported before |
| `won't fix` | Deliberate choice not to fix |

You can also create your own labels:
- `priority: high`
- `test: regression`
- `environment: staging`

---

## 3. Milestones: linking to a version or sprint

A **milestone** groups issues that belong to a version or sprint.

Example:
- Milestone `Sprint 4 — Release 2.1`
- Issues: 12 bugs, 3 test requests
- Progress: 7 of 15 closed

As a tester, a milestone gives you an overview: what needs to be ready before the release?

---

## 4. Managing test scripts in Git

Test scripts are just ordinary files (YAML, txt, Python, etc.).
Because they live in a Git repository, you get:

- **History**: who changed this test script, and when?
- **Rollback**: mistake in a test script? Go back to the previous version.
- **Collaboration**: a colleague can review test scripts through a pull request.
- **Traceability**: you can link a test script to an issue.

**Good folder structure for test scripts:**

```
testscripts/
  regressie/
    module1_login.yaml
    module2_formulieren.yaml
  smoke/
    dagelijkse_check.yaml
  exploratory/
    notities_sprint4.md
```

---

## 5. Linking a bug report to a commit

In a commit message you can refer to an issue:

```bash
git commit -m "Fix login validation (#42)"
```

GitHub recognizes `#42` and automatically links it to issue 42.
Use `Closes #42` to automatically close the issue when merged:

```bash
git commit -m "Fix: broken save button in form (Closes #58)"
```

---

## 6. The testing workflow in Git

A typical cycle for a tester:

```
1. Write or adjust a test script
       ↓
2. Create a branch: test/sprint4-regressie
       ↓
3. Commits: small changes with clear messages
       ↓
4. Pull request → reviewed by a colleague
       ↓
5. Found a bug? → Create an issue with reproduction steps
       ↓
6. Bug fixed by the developer → you test again on the PR branch
       ↓
7. PR merged → milestone updated
```

Git isn't extra administration.
It's the place where your work becomes visible and traceable.
