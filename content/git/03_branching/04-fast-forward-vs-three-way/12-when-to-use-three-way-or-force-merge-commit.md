## When to Use Three-Way or Force Merge Commit

When should you use three-way merges or force merge commits with --no-ff?

---

Use three-way (or force --no-ff) when:
- Collaborating with team (branches diverge naturally)
- Want to preserve feature context
- Need ability to revert entire features
- Following team conventions
- Complex features with multiple commits

Example:
```bash
git switch main
git merge --no-ff feature/payment  # Force merge commit
```

Result: Feature clearly identified in history, easy to understand grouping of related commits.

