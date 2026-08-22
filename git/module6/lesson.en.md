# Module 6 — Branches & collaborating

You know the basic workflow. Now you add collaboration.
Collaborating in Git revolves around branches and pull requests — the two tools that let teams work on the same project at the same time without chaos.

---

## 1. Creating a branch

Always create a branch for a new task.
Never work directly on `main`.

```bash
git branch my-branch
git switch my-branch
```

Or in one step:

```bash
git switch -c my-branch
```

Check which branch you're on:

```bash
git branch
```

The branch with `*` in front of it is the current branch.

Good branch names are descriptive and short:
- `add-readme`
- `fix-intro-typo`
- `update-version-number`

---

## 2. Committing changes on the branch

Work just like in module 5:

```bash
# make a change to a file
git add .
git commit -m "Description of the change"
```

Your commits now live on your branch — not on `main`.
`main` remains unchanged.

---

## 3. Pushing to GitHub

Now you send your branch to GitHub:

```bash
git push origin my-branch
```

The first time, Git asks you to confirm your GitHub account.
After pushing, the branch is on GitHub — visible to others.

---

## 4. Opening a pull request

A **pull request (PR)** is a proposal: "I'd like to merge my branch into main."

On GitHub:
1. Go to the `git-garden-playground` repository
2. You'll see a yellow bar: "my-branch — Compare & pull request"
3. Click on it
4. Write a description:
   - What did you change?
   - Why?
   - Is there anything the reviewer should know?
5. Click **"Create pull request"**

![Creating a pull request on GitHub](images/pull_request_aanmaken.png)

A pull request is a conversation, not a form.
The better the description, the smoother the review.

---

## 5. The collaboration workflow

```
main (stable)
 |
 ├── branch A (Developer A works here)
 |        → commits → push → PR → review → merge
 |
 ├── branch B (Developer B works here)
 |        → commits → push → PR → review → merge
 |
main (updated after merges)
```

Everyone works on their own branch.
`main` only gets updated through approved pull requests.
That way, `main` stays stable at all times.

---

## 6. Getting other people's changes

If someone else's branch has been merged, you'll want those changes too.

```bash
git switch main
git pull
```

`git pull` fetches the newest version of `main` from GitHub.

Want to know what's on GitHub without changing your local files?

```bash
git fetch
git status
```

`git fetch` retrieves the information. `git pull` retrieves the information *and* updates your files.

---

## 7. Practical assignment

1. Clone the `git-garden-playground` repository (if you haven't already).
2. Create a branch with your name: `contribution-[your-name]`
3. Create a file in the `bijdragen/` folder: `[your-name].md`
4. Write in it:
   - What you expect to learn from Git
   - One question you still have
5. Commit the file with a clear message.
6. Push the branch to GitHub.
7. Open a pull request with a short description.

After the assignment: your teacher or a fellow student will review the PR.
