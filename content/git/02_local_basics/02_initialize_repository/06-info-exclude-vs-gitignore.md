## info/exclude vs .gitignore

What is `.git/info/exclude`, and how does it differ from `.gitignore`?

---

`.git/info/exclude` uses the same pattern syntax as `.gitignore` and tells Git to ignore matching files. The key difference is **scope**:

```
.gitignore         → Committed to the repository and shared with
                     all contributors. Rules apply to everyone.

.git/info/exclude  → Local to your machine only. Never committed,
                     never shared. Used for personal editor files,
                     OS artifacts, or tool output that only you
                     need to exclude (e.g., .DS_Store, *.swp).
```

