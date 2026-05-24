## Two-Dot vs Three-Dot git diff

What is the difference between `git diff main..feature` and `git diff main...feature`?

---

```
main..feature   (two dots)
  Standard diff: compares the tip of main directly with the
  tip of feature. Shows all differences between the two
  branch tips as they currently stand.

main...feature  (three dots)
  Symmetric diff: compares the tip of feature with the
  MERGE BASE (the common ancestor where the branches diverged).
  Shows only the changes introduced on feature since it
  branched off — exactly what a pull request diff shows.
```

Use `...` when reviewing a feature branch to see only its own changes, independent of what has happened on main since the branch was created.

