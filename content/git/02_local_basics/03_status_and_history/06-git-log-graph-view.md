## git log Graph View

How do you visualize branch structure with git log?

---

`git log --graph --oneline --all`

Shows ASCII graph of branch structure:
```
* a1b2c3d (HEAD -> main) Add feature
| * b2c3d4e (feature-branch) New feature
|/
* c3d4e5f Initial commit
```

Use `--graph --oneline --decorate --all` for more detail, or create an alias for a beautiful colored version.

