## Handling Rebase Conflicts

How do you resolve conflicts during a rebase?

---

Rebase applies commits one at a time. When conflict occurs:

1. Fix conflicts in files (remove markers)
2. Stage resolved files: `git add file.txt`
3. Continue rebase: `git rebase --continue`
4. Repeat for each conflicting commit

Commands:
```bash
git rebase --continue  # After resolving conflict
git rebase --skip      # Skip problematic commit
git rebase --abort     # Cancel entire rebase
```

Each commit may have conflicts—more tedious than merge (resolves once).

