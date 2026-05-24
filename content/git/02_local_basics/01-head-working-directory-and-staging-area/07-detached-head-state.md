## Detached HEAD State

What is detached HEAD state, what triggers it, and what is the risk of making commits in it?

---

**Detached HEAD** occurs when HEAD points directly to a commit hash instead of to a branch reference:

```
Normal:    HEAD → refs/heads/main → commit abc
Detached:  HEAD → commit abc  (no branch in between)
```

**Triggers:**
- `git checkout <commit-hash>`
- `git checkout <tag>`
- `git checkout origin/main` (a remote-tracking branch)

**Risk:** Any commits made in detached HEAD state are not reachable from any branch. If you switch away without saving them to a branch, Git's garbage collector will eventually delete them.

**Recovery:**
```bash
git switch -c my-recovery-branch   # create a branch at current position
```

