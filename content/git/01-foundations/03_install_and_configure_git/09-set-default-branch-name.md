## Set Default Branch Name

What command sets the default branch name for all new Git repositories to `main`?

---

```bash
git config --global init.defaultBranch main
```

Historically Git used `master` as the default. The current convention (and default on GitHub and GitLab) is `main`. This config ensures consistency when you run `git init`.

