## Initializing with Specific Branch Name

What are three ways to initialize a Git repository with "main" as the default branch instead of "master"?

---

1. Set globally first: `git config --global init.defaultBranch main`, then `git init`
2. Specify during init: `git init -b main` or `git init --initial-branch=main`
3. Rename after init: `git init`, then `git branch -m master main`

Method 1 is recommended as it applies to all future repositories.

