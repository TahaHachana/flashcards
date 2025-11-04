## Preventing Fast-Forward with --no-ff

What does `git merge --no-ff` do and why would you use it?

---

`git merge --no-ff feature` forces creation of a merge commit even when fast-forward is possible.

Result:
```
main:    A --- B --------- M
              \           /
feature:       C --- D ---
```

Reasons to use --no-ff:
- Preserve feature branch history
- Group related commits together
- Easier rollback (revert entire feature)
- Better visualization (branch structure visible)
- Team policy compliance

Makes it clear that work was done on a separate branch.

