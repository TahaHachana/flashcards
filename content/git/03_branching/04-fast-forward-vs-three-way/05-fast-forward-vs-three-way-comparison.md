## Fast-Forward vs Three-Way Comparison

What are the key differences between fast-forward and three-way merges?

---

Fast-Forward:
- Target unchanged since branch
- No merge commit
- Linear history
- Instant (pointer move)
- No conflicts possible

Three-Way:
- Both branches have new commits
- Merge commit created (two parents)
- Non-linear history (shows divergence)
- Creates new commit
- Conflicts possible

Detection: Git messages differ—"Fast-forward" vs "Merge made by..."

