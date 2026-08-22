# Module 1 — Origin & philosophy

Git is today the most widely used version control system in the world.
But it didn't always exist. And it didn't come about by accident — there was a serious problem behind it.

---

## 1. The problem: building software as a team

Imagine you're working with ten people on the same project.
Everyone has the same files. Everyone makes changes.

How do you then know:
- who changed what?
- when an error crept in?
- how to go back to yesterday?

Without version control, the answer is: you don't know.
You send files by email, overwrite each other's work, lose code.

That is exactly what used to happen in software teams.

---

## 2. Centralized version control: the previous generation

Before Git there were systems like SVN and CVS.
They worked in a **centralized** way: one central server held all the history.

That had drawbacks:
- the server goes down → everyone is stuck
- you can't work without a network connection
- one error on the server = everything gone

![Centralized vs distributed version control](/instructions/content-images/git/module1/centralized_vs_distributed.svg)

---

## 3. Linus Torvalds and the conflict of 2005

Linus Torvalds is the creator of the Linux kernel — the heart of many operating systems.
Thousands of developers contributed to it.

They used a commercial system: **BitKeeper**.
Free for open-source projects — until the license was withdrawn in 2005.

Linus had a choice: switch to an existing system, or build something himself.
None of the existing tools did what he needed.

In **two weeks** he wrote the foundation of Git.

> "I'm an egotistical bastard, and I name all my projects after myself.
> First Linux, now Git."
> — Linus Torvalds

---

## 4. The philosophy of Git

Git is built on three core ideas:

**Distributed**
Everyone has the full history on their own computer.
You can work without internet. The server is not sacred.

**Secure**
Every commit gets a unique code (hash) based on its content.
Changing something in the history is immediately noticeable.

**Fast**
Git works locally. Almost everything happens on your own machine.
No waiting time, no dependence on a server.

---

## 5. Git is not GitHub

This is a common confusion.

**Git** is the version control system — a program you install locally.
**GitHub** is a website where you can store and share Git projects.

Git was invented by Linus Torvalds.
GitHub is a company, founded in 2008, bought by Microsoft in 2018.

You can use Git without GitHub.
But GitHub without Git makes no sense.

---

## 6. Why is this relevant to you as a tester?

As a tester you work with code, test scripts, bug reports and documentation.
All those files change over time.

Git gives you:
- a complete history of every file
- insight into who changed what and when
- the ability to go back when something goes wrong
- collaboration without chaos

You don't need to program to find Git useful.
