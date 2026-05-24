## Global Config File Location

Where is the global Git configuration file stored, and what does a typical one look like?

---

Located at `~/.gitconfig` (or `~/.config/git/config`). A typical file after basic setup:

```ini
[user]
    name = Jane Doe
    email = jane@example.com
[core]
    editor = code --wait
    autocrlf = input
[init]
    defaultBranch = main
```

