## When to Use Fast-Forward

When should you use or allow fast-forward merges?

---

Use fast-forward when:
- Working solo on simple features
- Want clean, linear history
- Changes are sequential and independent
- Quick bug fixes or documentation updates
- Main branch hasn't changed since branching

Example workflow:
```bash
git switch -c feature/typo-fix
git commit -m "Fix typo"
git switch main
git merge feature/typo-fix  # Fast-forward
```

Result: Clean linear history without merge commit clutter.

