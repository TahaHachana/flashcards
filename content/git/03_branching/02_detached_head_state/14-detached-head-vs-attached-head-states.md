## Detached HEAD vs Attached HEAD States

What is the key difference in behavior when committing in attached vs detached HEAD?

---

Attached HEAD (normal):
```bash
git commit -m "Fix"
```
- Branch moves forward to new commit
- Commit is saved on the branch
- Easy to find and reference

Detached HEAD:
```bash
git commit -m "Fix"
```
- No branch moves (none exists)
- Commit is created but "dangling"
- Will be lost when switching away
- Requires reflog to recover

Always be on a branch (attached HEAD) for actual development work.

