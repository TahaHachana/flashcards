## Force Fast-Forward Only

What does `git merge --ff-only` do and when is it useful?

---

`git merge --ff-only feature` will:
- Succeed only if fast-forward is possible
- Fail if three-way merge would be required

Example:
```bash
git merge --ff-only feature
# fatal: Not possible to fast-forward, aborting.
```

Use cases:
- Enforcing linear history policy
- Ensuring target branch unchanged before merge
- Preventing accidental merge commits

Useful when you want to maintain strictly linear history and catch diverged branches.

