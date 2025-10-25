## Common Merge Scenarios

What are three common merge scenarios and their workflows?

---

1. Simple feature integration:
   ```bash
   git switch main
   git merge feature/login
   git branch -d feature/login
   ```

2. Keeping feature updated with main:
   ```bash
   git switch feature/payment
   git merge main  # Bring main changes into feature
   ```

3. Merge with review:
   ```bash
   git merge --no-commit feature/experimental
   git diff --staged  # Review
   git commit  # or git merge --abort
   ```

Each scenario addresses different workflow needs.

