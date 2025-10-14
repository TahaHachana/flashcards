## The commit -a Flag

What does `git commit -a` or `git commit -am "message"` do, and what are its limitations?

---

It stages all modified tracked files and commits them in one step, skipping the explicit `git add` step.

LIMITATION: It ONLY works for files Git already tracks. It does NOT add new (untracked) files. New files still require explicit `git add`.

Example: `git commit -am "Quick fix for styling"`

