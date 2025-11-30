## Remote Troubleshooting

How do you fix common remote issues?

---

"Remote already exists":
```bash
git remote set-url origin <new-url>  # Update URL
# or
git remote remove origin && git remote add origin <url>
```

"No such remote":
```bash
git remote add <name> <url>  # Add it first
```

"Remote URL changed":
```bash
git remote set-url origin <new-url>
```

Always verify with `git remote -v` after changes.

