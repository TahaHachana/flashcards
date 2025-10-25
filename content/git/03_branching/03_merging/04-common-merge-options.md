## Common Merge Options

What do these merge options do: `--no-commit`, `--squash`, `-m "message"`?

---

- `git merge --no-commit feature`: Merge but don't auto-commit (stage changes for review first)
- `git merge --squash feature`: Combine all feature commits into one commit (flattens history)
- `git merge feature -m "message"`: Merge with custom commit message

Examples:
```bash
git merge --no-commit feature  # Review before committing
git merge --squash feature     # Single commit
git commit -m "Add feature"
```

