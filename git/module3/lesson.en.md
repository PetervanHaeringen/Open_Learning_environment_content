# Module 3 — Version control, visualized

Before you type a command, you need to be able to *see* it.
In this module we build the mental model: what does Git look like when you draw it?

---

## 1. The timeline: commits in a row

The simplest Git situation is a straight line of commits.
Each commit is a snapshot. Each commit points back to its predecessor.

```
○ — ○ — ○ — ○ — ○
A   B   C   D   E
```

- **A** is the first commit (the origin)
- **E** is the latest commit (the current state)
- The arrows point to the past

Read the timeline from left to right: that's how the history grew.

![Git timeline — commits in a row](images/tijdlijn_lineair.png)

---

## 2. A branch: a side path

Imagine: you want to try something without touching the main line.
You create a **branch** — a side path that starts at an existing commit.

```
○ — ○ — ○ — ○ — ○       (main)
              |
              ○ — ○       (experiment)
```

- `main` simply continues
- `experiment` starts at commit D and grows independently
- Both exist at the same time, without affecting each other

In Git, a branch is nothing more than a name pointing to a commit.
That's it. No copy of the files, no duplicate folder — just a label.

![Branch as a side path off the timeline](images/branch_zijtak.png)

---

## 3. Merging: joining two branches

Once the experiment is finished, you want to fold it back into `main`.
That's called a **merge**.

```
○ — ○ — ○ — ○ — ○ — ○   (main, after merge)
              |       |
              ○ — ○ ——   (experiment, merged)
```

Git looks at the common ancestor (commit D) and the two endpoints.
It combines the changes and creates a new **merge commit** (the last ○ on main).

If the same lines were changed on both branches → conflict.
If not → automatic merge.

![Merge of two branches](images/merge_visueel.png)

---

## 4. HEAD: you are here

`HEAD` is a sticker showing where you currently are in the graph.

```
○ — ○ — ○ — ○ — ○
                 ↑
                HEAD (main)
```

When you switch to another branch (`git switch experiment`), the sticker moves with you:

```
○ — ○ — ○ — ○ — ○       (main)
              |
              ○ — ○
                   ↑
                  HEAD (experiment)
```

Everything you commit now goes to whichever branch HEAD is on.

---

## 5. Back in time

Suppose commit C contained a bug you now want to investigate.
You can temporarily move HEAD to C (`git checkout C`).

```
○ — ○ — ○ — ○ — ○
         ↑
        HEAD (detached)
```

Your files will then look exactly as they did at that moment.
Git calls this a "detached HEAD" — you're not on a branch, but directly on a commit.

Useful for looking around. Dangerous to commit without creating a new branch first.

---

## 6. Exercise: draw it yourself

Grab a pen and paper.

1. Draw a straight line with five circles (commits A through E).
2. Draw a branch that starts at C, with two extra commits.
3. Draw a merge back into the main line after E.
4. Place the HEAD sticker in the right spot.

This drawing is exactly what Git keeps track of internally.
In the next module you'll act this out again using cards.
