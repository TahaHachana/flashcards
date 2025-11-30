## Adding a Remote

How do you add a new remote to your repository?

---

Syntax:
```bash
git remote add <name> <url>
```

Example (adding origin):
```bash
git remote add origin https://github.com/user/project.git
```

Example (adding upstream for forks):
```bash
git remote add upstream https://github.com/original/project.git
```

Verify:
```bash
git remote -v
```

Choose meaningful names: origin, upstream, github, gitlab, etc.

