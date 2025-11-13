## Post-Clone Best Practices

What should you do immediately after cloning a repository?

---

1. Verify clone successful:
   ```bash
   git log
   git remote -v
   git status
   ```

2. Configure user info (if needed):
   ```bash
   git config user.name "Your Name"
   git config user.email "your@email.com"
   ```

3. Read README and documentation

4. Install dependencies:
   ```bash
   npm install  # or pip, bundle, etc.
   ```

5. Run tests to verify setup:
   ```bash
   npm test
   ```

Proper setup prevents issues later.

