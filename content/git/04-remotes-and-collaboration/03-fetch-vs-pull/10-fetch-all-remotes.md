## Fetch All Remotes

How do you fetch from all configured remotes at once?

---

```bash
git fetch --all
```

Fetches from all remotes:
```bash
git remote -v
# origin    https://github.com/user/project.git
# upstream  https://github.com/original/project.git

git fetch --all
# Fetches from both origin and upstream
```

Useful when working with forks or multiple backup locations.

