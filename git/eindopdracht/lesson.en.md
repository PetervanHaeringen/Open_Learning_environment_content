# Final assignment — Complete Git workflow

You've gone through the theory, the visualizations, and the practical steps.
Now you'll bring it all together: a complete professional workflow on the practice repository.

---

## What you'll do

You'll go through the steps a tester carries out daily in a real team:

```
Create an issue
      ↓
Create a branch
      ↓
Write a test file + commit
      ↓
Push to GitHub
      ↓
Open a pull request
      ↓
Receive and process review
      ↓
Merge (by teacher or peer)
      ↓
Close the issue
```

---

## The assignment

### Step 1 — Create an issue

Create an issue in the `git-garden-playground` repository.

The scenario: you've discovered that the instructions in the `handleidingen/` folder are missing for the topic you learned.

Write an issue with:
- a clear title
- a description of what's missing
- label: `documentation`
- milestone: `Git Garden v1.0` (if it exists, otherwise leave this blank)

Note down the issue number — you'll need it later.

---

### Step 2 — Create a branch

```bash
git switch main
git pull
git switch -c docs/handleiding-[your-name]
```

Use a descriptive branch name that starts with `docs/`.

---

### Step 3 — Write a file

Create a file in the `handleidingen/` folder:

**`handleidingen/[your-name]-samenvatting.md`**

In it, write a short summary of what you learned in this Git learning path.
At minimum:
- 3 things you understand now that you didn't understand before
- 1 command you find the most useful
- 1 situation from your own work where you'd want to use Git

---

### Step 4 — Commit

```bash
git add handleidingen/[your-name]-samenvatting.md
git commit -m "Add Git summary for [your name] (Closes #[issue-number])"
```

---

### Step 5 — Push

```bash
git push origin docs/handleiding-[your-name]
```

---

### Step 6 — Open a pull request

Go to GitHub and open a pull request.

**Requirements for the PR description:**
- What did you add?
- Why is this useful for others?
- Reference to the issue: `Closes #[number]`
- One point the reviewer should specifically check

---

### Step 7 — Process the review

Your teacher or a fellow student will review your PR.
If there's feedback:
1. Adjust the file on your local branch
2. Commit the change with a clear message
3. Push the change — the PR is automatically updated

---

### Step 8 — Merge

After approval, the PR gets merged by the teacher or by you (if permissions allow it).

Then check:
```bash
git switch main
git pull
ls handleidingen/
```

Your file is now in `main`. It's part of the official repository.

---

## Assessment criteria

| Component | Good |
|-----------|------|
| Issue | Clear title, description, correct label |
| Branch name | Descriptive, starts with `docs/` |
| Commit message | Descriptive, references the issue number |
| File | Meets the requirements, own text |
| PR description | Complete, includes Closes #number |
| Processing feedback | New commit with a clear message |

---

## Done?

If everything has been merged, you've demonstrated that you can:
- independently carry out a complete Git workflow
- communicate professionally in issues and pull requests
- know how to process feedback without disrupting the workflow

That's not a trick with four commands — that's working like a professional.
