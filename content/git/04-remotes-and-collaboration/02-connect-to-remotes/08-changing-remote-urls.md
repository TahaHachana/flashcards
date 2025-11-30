## Changing Remote URLs

How do you change a remote's URL?

---

```bash
git remote set-url <name> <new-url>
```

Example (HTTPS to SSH):
```bash
git remote set-url origin git@github.com:user/project.git
```

Verify:
```bash
git remote -v
```

Common scenarios:
- Switch from HTTPS to SSH
- Repository moved to new URL
- Change from personal to organization account
- Update after repository rename

