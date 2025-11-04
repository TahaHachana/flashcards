## Key Branch Deletion Principles

What are the essential principles for branch deletion?

---

1. Deleting branch removes pointer, not commits (if merged)
2. `-d` is safe delete (merged only), `-D` forces deletion
3. Cannot delete current branch (switch first)
4. Local and remote deletion are separate operations
5. `git push origin --delete branch` removes remote branch
6. Prune stale references with `git fetch --prune`
7. Recovery possible via reflog (within ~30 days)
8. Delete promptly after merging for clean repo
9. Protected branches can't be deleted
10. Team coordination essential for shared branches

Regular cleanup keeps repositories professional and manageable!

