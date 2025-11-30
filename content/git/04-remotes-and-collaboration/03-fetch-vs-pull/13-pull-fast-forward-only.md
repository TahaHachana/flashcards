## Pull Fast-Forward Only

What does `git pull --ff-only` do and when would you use it?

---

```bash
git pull --ff-only
```

Only pulls if fast-forward is possible. Fails if branches diverged (prevents automatic merge commits).

Configure as default:
```bash
git config --global pull.ff only
```

Use when:
- Want to maintain linear history
- Want to be notified if branches diverged
- Prefer explicit merge/rebase decisions

Forces you to handle divergence manually.

