## Force Pushing After Rebase

Why is force push needed after rebasing, and what's the safer option?

---

After rebasing pushed commits, histories diverge (different hashes). Normal push fails.

Force push required:
```bash
git push --force origin feature
```

Safer option:
```bash
git push --force-with-lease origin feature
```

`--force-with-lease`:
- Checks if remote changed since last fetch
- Prevents overwriting others' work
- Safer than plain `--force`

⚠️ Only force push branches you own or after coordinating with team.

