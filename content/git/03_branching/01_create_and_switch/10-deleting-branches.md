## Deleting Branches

What's the difference between `git branch -d` and `git branch -D`?

---

- `git branch -d branch-name`: Safe delete—only deletes if branch is fully merged. Git protects you from losing work.

- `git branch -D branch-name`: Force delete—deletes even if unmerged. Use carefully as you may lose unique commits.

Cannot delete current branch:
```bash
git branch -d main  # Error
```
Switch to another branch first.

After merging a feature branch, use `-d` to clean up.

