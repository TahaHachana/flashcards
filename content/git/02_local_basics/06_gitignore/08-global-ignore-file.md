## Global Ignore File

How do you configure a global ignore file, and what kinds of patterns should go there versus in the repository's `.gitignore`?

---

**Setup:**
```bash
git config --global core.excludesFile ~/.config/git/ignore
```

Then add patterns to `~/.config/git/ignore`. It uses the same syntax as `.gitignore` but is **never committed** — it is personal to your machine.

```
Global ignore file (personal, not shared):
  .DS_Store, Desktop.ini, Thumbs.db   ← OS artifacts
  .vscode/, .idea/                    ← editor directories
  *.swp, *~                           ← editor temp files

Repository .gitignore (committed, shared with team):
  build/, dist/, *.egg-info/          ← build artifacts
  __pycache__/, *.pyc                 ← language artifacts
  node_modules/                       ← dependency directories
  .env                                ← secret config files
```

