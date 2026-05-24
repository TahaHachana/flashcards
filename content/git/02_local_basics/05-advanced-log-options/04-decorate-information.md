## --decorate Information

What does the decoration `(HEAD -> main, origin/main, tag: v1.0)` tell you about a commit?

---

```
HEAD -> main   → The current branch is main, and this commit
                 is its tip. HEAD is currently checked out here.

origin/main    → The remote-tracking branch origin/main also
                 points to this commit, meaning the local branch
                 is in sync with the remote.

tag: v1.0      → A tag named v1.0 was applied to this commit
                 (e.g., a release marker).
```

Without `--decorate` you would see only the hash, with no indication of which branches or tags land at each commit.

