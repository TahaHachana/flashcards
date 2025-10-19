## Commit References

What do these commit references mean: `HEAD`, `HEAD~1`, `HEAD~5`, `HEAD^`?

---

- `HEAD`: Current commit
- `HEAD~1` or `HEAD~`: Parent of HEAD (1 commit back)
- `HEAD~2`: Grandparent (2 commits back)
- `HEAD~5`: 5 commits back
- `HEAD^`: First parent (same as HEAD~1 for linear history)

Examples: `git show HEAD~3`, `git show main~5`, `git show a1b2c3d~2`

