## Staged File Scenario

You stage `app.py` with `git add app.py`, then edit `app.py` again without staging. How many distinct versions of `app.py` now exist across the three areas, and what does each contain?

---

**Three distinct versions** exist simultaneously:

```
Working directory → app.py with BOTH sets of edits
                    (the post-stage modifications)

Staging area      → app.py as it was when you ran git add
                    (first set of edits only; will go into next commit)

HEAD (repository) → app.py as it was in the last commit
                    (original, unmodified version)
```

Running `git diff` shows working-dir vs index (second edit).
Running `git diff --staged` shows index vs HEAD (first edit).
Running `git commit` records only the staged (first edit) version.

