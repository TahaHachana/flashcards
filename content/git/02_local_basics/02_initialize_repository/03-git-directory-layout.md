## .git Directory Layout

Name the five most important items inside `.git/` and state the role of each.

---

```
HEAD          → Symbolic ref pointing to the current branch.
                Contains text like: ref: refs/heads/main

config        → Repository-local configuration (remote URLs,
                user info overrides, merge settings).

objects/      → Content-addressable object database.
                Stores every blob (file version), tree
                (directory snapshot), and commit as an
                immutable object keyed by its SHA-1 hash.

refs/heads/   → One file per local branch, each containing
                the SHA-1 hash of that branch's tip commit.

hooks/        → Shell scripts called at Git lifecycle events
                (pre-commit, post-merge, etc.). All samples
                end in .sample and are disabled by default.
```

