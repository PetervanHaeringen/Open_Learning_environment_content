# Module 4 — The Git Game

You only truly understand Git once you've *felt* it.
In this game, the group itself becomes a version control system.
No terminal. No commands. But a real experience of what happens inside Git.

---

## Materials

- Post-its or cards (at least 30)
- Markers (at least 2 colors)
- A table or wall as a "timeline"
- 1 roll of tape or masking tape for the lines
- Participants: 3 to 8 people

---

## Roles

| Role | Task |
|-----|------|
| **Maintainer** | Manages the `main` branch. Approves merges. |
| **Developer A** | Works on their own branch. |
| **Developer B** | Works on another branch (at the same time as A). |
| **Reviewer** | Reviews branches before they get merged. |

In small groups, one person can take on multiple roles.

---

## The "project"

The project is a fictional text file: `README.txt`
The starting version has three lines:

```
Projectnaam: Git Garden
Versie: 1.0
Beschrijving: Een oefenproject.
```

Write this starting version on a post-it. This is **commit A** — the origin.
Stick it on the far left of the timeline.

---

## Round 1 — Straight timeline

**Goal:** experience how commits follow one another.

1. Developer A writes a small change on a new post-it.
   Example: `Versie: 1.1`
   Write at the top: `Commit B — Developer A — "version updated"`
2. Stick commit B to the right of A, connected with an arrow.
3. Developer A makes another change → commit C.
4. Developer B does the same → commit D, E.

After five commits you have a timeline. Discuss:
- Who changed what?
- Can you go back to commit B?

---

## Round 2 — Branching

**Goal:** experience that two people can work on the same project at the same time.

1. Use tape to draw two lines starting from commit C — one going up, one going straight on.
2. Developer A keeps working on the top line: commit D (their version of the file).
3. Developer B works on the bottom line: commit D' (their version — different changes).
4. Both write their post-its and stick them on their own line.

Now you have two branches. Discuss:
- What's on the A line? What's on the B line?
- Are they both valid? Yes. Git keeps track of both.

---

## Round 3 — Merging

**Goal:** experience what a merge is — and when it can go wrong.

**Scenario A: no conflict**
Developer A changed the description.
Developer B changed the version.
→ No conflict. The Reviewer combines both changes on a new post-it: **merge commit M**.
Stick M to the right of the two lines, with two arrows pointing to it.

**Scenario B: conflict**
Developer A writes: `Versie: 2.0`
Developer B also writes: `Versie: 1.5`
→ Conflict! Same line, two different values.
The Reviewer stops. Discuss: who is right? What do you choose?
Write the decision on the merge commit.

This is exactly what Git does: merge automatically when it can, and stop when it can't.

---

## Round 4 — Back in time

**Goal:** understand that Git never forgets anything.

1. Look at the timeline.
2. The Maintainer asks: "What did the file look like at commit B?"
3. Everyone looks at the post-it for commit B — and can give the answer.

Git does exactly this: every commit contains the full state of the project.
You can always go back.

---

## Debrief

Discuss with the group:

1. What was the hardest moment in the game?
2. When did the conflict arise — and how did you resolve it?
3. What could have been a better commit message?
4. How does this relate to your daily work with files?

---

## Connecting to the real terminal

After this game you know the concepts from the inside out:

| What you did in the game | Git command |
|--------------------------|--------------|
| Writing a post-it (recording a change) | `git commit -m "..."` |
| Drawing a new line (creating a branch) | `git branch name` |
| Switching to another line | `git switch name` |
| Combining two lines | `git merge name` |
| Looking back at an earlier post-it | `git log` / `git checkout` |

In the next module you'll do exactly this — but in the terminal.
