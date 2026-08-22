# Module 7 — Conflicts & quality

Collaboration doesn't always go smoothly.
Sometimes you try to merge something and Git says: "I can't do this on my own."
That's not an error — it's a question directed at you.

---

## 1. What is a merge conflict?

A merge conflict happens when two branches have **changed the same line in different ways**.

Git can't decide on its own which version is the right one.
It marks the conflicting lines and waits for you.

Example: on `main`, the first line of `README.md` is:
```
Versie: 1.0
```

On your branch, you changed it to:
```
Versie: 2.0
```

And on the other branch it says:
```
Versie: 1.5
```

Who's right? Git doesn't know. You do.

---

## 2. What does a conflict look like?

Git opens the file and inserts markers:

```
<<<<<<< HEAD
Versie: 2.0
=======
Versie: 1.5
>>>>>>> other-branch
```

- Everything between `<<<<<<< HEAD` and `=======` is your version
- Everything between `=======` and `>>>>>>>` is the other branch's version
- You choose what stays

---

## 3. Resolving a conflict: step by step

```bash
# You try to merge
git merge other-branch

# Git reports: CONFLICT (content) in README.md
# Open the file in your editor
```

**In the editor:**
1. Find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
2. Decide which version is correct — or combine them
3. Remove all the markers
4. Save the file

**Back in the terminal:**
```bash
git add README.md
git commit -m "Resolved conflict: version number set to 2.0"
```

The conflict is resolved. The merge commit has been created.

---

## 4. Preventing conflicts

The best way to avoid conflicts: **small, frequent commits and merges**.

The longer you wait to merge, the greater the chance someone else has changed the same lines.

Good habits:
- Keep branches short-lived — work in days, not weeks
- Pull regularly: `git pull origin main` on your branch to stay up to date
- Discuss who is working on which part

---

## 5. Code review: quality before the merge

A **code review** means looking at someone else's work before it gets merged.

As a reviewer, pay attention to:
- Is the change understandable?
- Does it have any unexpected consequences?
- Are the commit messages clear?
- Are there any typos or inconsistencies?

As a tester, you're excellent at reviewing — you already think in edge cases and risks.

**Good review etiquette:**
- Ask questions instead of making demands: "Have you thought about...?" instead of "This is wrong."
- Point out what's good too
- Leave your ego out of the review — it's about the product

![Pull request review on GitHub](images/code_review.png)

---

## 6. Tags and releases

A **tag** is a name you give to a specific commit.
Useful for version numbers: `v1.0`, `v2.3.1`.

```bash
# Create a lightweight tag
git tag v1.0

# Create an annotated tag (with a description)
git tag -a v1.0 -m "First stable version"

# Push the tag to GitHub
git push origin v1.0
```

On GitHub you can create a **release** from a tag.
A release contains:
- the code at that point in time
- release notes (what's new, what's fixed)
- optionally, attachments (installation files)

For a tester, a release is the starting point of a test round.
