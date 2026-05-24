## Interactive Staging with git add -p

What is `git add -p`, what does it allow you to do, and what do the keys `y`, `n`, and `s` do at the hunk prompt?

---

`git add -p` (patch mode) presents each **hunk** (contiguous block of changes) in your modified files one at a time and asks whether to stage it.

```
y  → Yes, stage this hunk
n  → No, skip this hunk (do not stage it)
s  → Split the hunk into smaller pieces for finer control
e  → Manually edit the hunk before staging
q  → Quit; leave remaining hunks unstaged
```

**Purpose:** lets you commit only part of a file's changes — keeping unrelated modifications out of the current commit and crafting a cleaner, single-purpose history.

