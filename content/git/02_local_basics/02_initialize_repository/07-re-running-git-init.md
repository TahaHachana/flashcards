## Re-running git init

What happens if you run `git init` inside a directory that is already a Git repository?

---

It is **safe and non-destructive**. Git re-initialises the repository without touching any commits, branches, tags, or configuration. It prints:

```
Reinitialized existing Git repository in /path/to/project/.git/
```

This is occasionally useful after manually changing `.git/` settings, upgrading Git, or restoring a corrupted config file.

