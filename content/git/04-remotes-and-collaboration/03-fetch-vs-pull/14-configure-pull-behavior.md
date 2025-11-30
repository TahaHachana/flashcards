## Configure Pull Behavior

What are the three ways to configure default pull behavior?

---

1. Merge (default):
   ```bash
   git config pull.rebase false
   ```

2. Rebase:
   ```bash
   git config pull.rebase true
   ```

3. Fast-forward only:
   ```bash
   git config pull.ff only
   ```

Choose based on team workflow:
- Merge: Preserves history (default)
- Rebase: Linear history
- FF-only: Strict linear, manual handling

Can also use flags per-pull: `--rebase`, `--ff-only`

