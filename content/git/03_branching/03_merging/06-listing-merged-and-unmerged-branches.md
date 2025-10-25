## Listing Merged and Unmerged Branches

How do you list which branches have been merged and which haven't?

---

Merged branches (safe to delete):
```bash
git branch --merged
```
Shows branches whose changes are in current branch.

Unmerged branches (have unique commits):
```bash
git branch --no-merged
```
Shows branches with commits not yet in current branch.

Use this before cleanup to avoid deleting branches with unmerged work.

