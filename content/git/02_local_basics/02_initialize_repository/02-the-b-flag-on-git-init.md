## The -b Flag on git init

What does `git init -b main` do, and why is it preferred over a plain `git init`?

---

The `-b <name>` flag sets the **name of the initial branch** when creating a new repository. `git init -b main` creates the repo with `main` as the default branch instead of Git's built-in default (`master`).

It is preferred because:
- Modern platforms (GitHub, GitLab) use `main` as the default, avoiding a mismatch that would require a rename.
- It keeps local and remote repositories consistent from the start.

The global equivalent (so you never need `-b` again):
```bash
git config --global init.defaultBranch main
```

