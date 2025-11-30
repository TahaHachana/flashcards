## Pull with Rebase

How do you pull with rebase instead of merge, and why would you?

---

Pull with rebase:
```bash
git pull --rebase
```

Equivalent to:
```bash
git fetch
git rebase origin/main
```

Configure as default:
```bash
git config --global pull.rebase true
```

Advantage: Linear history (no merge commits)

Choose based on team preference for history style.

