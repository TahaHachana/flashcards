## Listing Branches

What do these commands show: `git branch`, `git branch -a`, `git branch -v`?

---

- `git branch`: List all local branches (`*` indicates current branch)
- `git branch -a` or `--all`: List all branches (local and remote)
- `git branch -v`: Verbose output showing last commit on each branch
- `git branch -r`: List only remote branches

Example output:
```
* main           a1b2c3d Fix bug
  feature-login  b2c3d4e Add form
```

