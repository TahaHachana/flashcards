## Bare vs. Normal Repository

What is a bare repository, how is it created, and when would you use one?

---

A **bare repository** is a Git repository that contains only the `.git/` data and has no working directory. It is created with:

```bash
git init --bare project.git
```

By convention, bare repos are named with a `.git` suffix.

**Use case:** bare repositories are used as **shared central servers** (e.g., a team's origin remote). Developers push to and pull from them, but no one edits files directly inside the bare repo. Commands that require a working tree (`git add`, `git checkout`, `git commit`) cannot be run inside a bare repository.

