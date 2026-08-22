# Module 5 — Working locally

You've seen Git, felt it, and drawn it.
Now you're going to do it. In the terminal, on a real repository.

---

## Preparation: installation and configuration

**Install Git**
- Windows: [git-scm.com/download/win](https://git-scm.com/download/win)
- Mac: open Terminal, type `git --version` (installs automatically or gives instructions)
- Linux: `sudo apt install git`

**Set your name and email** (this goes into every commit you make):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

Check your settings:

```bash
git config --list
```

---

## The practice repository

For this learning path we use a separate practice repository:

**`git-garden-playground`**

Your teacher will give you the exact URL.
It starts with `https://github.com/...`

This repository is specifically for practicing — you can't break anything.

---

## Step 1: Cloning

Cloning means downloading a repository to your own computer.

```bash
git clone https://github.com/...url.../git-garden-playground
```

After cloning:

```bash
cd git-garden-playground
ls
```

You'll see the repo's files. And there's a hidden `.git` folder — the time machine.

---

## Step 2: Checking status

`git status` is your compass. Use it often.

```bash
git status
```

You'll see which branch you're on and whether any files have changed.

---

## Step 3: Making a change

Open the folder in your editor (or use the terminal).
Create a new file in the `deelnemers/` folder:

```bash
mkdir -p deelnemers
echo "Naam: [your name]" > deelnemers/[your-name].txt
```

Then check the status:

```bash
git status
```

Git reports the new file as "untracked" — it exists, but Git isn't tracking it yet.

---

## Step 4: Staging

Staging means saying: "I want to include this file in the next commit."

```bash
git add deelnemers/[your-name].txt
```

Or add everything at once:

```bash
git add .
```

Check the status again. The file is now in the "staging area" — ready for commit.

![Workflow: working directory → staging area → repository](images/werkstroom.png)

---

## Step 5: Committing

Now you create the snapshot.

```bash
git commit -m "Add [your name] to participants list"
```

A good commit message:
- starts with a verb: "Add", "Fix", "Update", "Remove"
- describes *what* changed, not *how*
- is short (max ~72 characters)

---

## Step 6: Viewing history

```bash
git log
```

You'll see all commits: hash, author, date, message.

For a compact overview:

```bash
git log --oneline
```

For a visual overview with branches:

```bash
git log --oneline --graph --all
```

---

## Step 7: Viewing differences

Want to see what changed before you commit?

```bash
git diff
```

After staging, but before commit:

```bash
git diff --staged
```

---

## Summary: the daily workflow

```
[make a change]
      ↓
git add .
      ↓
git commit -m "..."
      ↓
git push   (covered in module 6)
```

Repeat this pattern dozens of times a day.
It becomes second nature.
