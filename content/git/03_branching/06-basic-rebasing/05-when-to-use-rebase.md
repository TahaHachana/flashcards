## When to Use Rebase

What are four good use cases for rebasing?

---

✅ Good uses:
1. Clean up local commits before pushing
2. Keep feature branch updated with main: `git rebase main`
3. Maintain linear project history (easier to follow)
4. Before creating pull request (present clean commits)

Example:
```bash
# Before pushing feature
git switch feature
git rebase main           # Update with main
git push origin feature   # Push clean history
```

All these involve local or personal branches, not shared public branches.

