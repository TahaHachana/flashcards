## Preventing Merge Conflicts

What are five best practices to prevent merge conflicts?

---

1. Pull frequently: `git pull origin main` (stay updated)
2. Keep feature branches short-lived (create → work → merge quickly)
3. Communicate with team (coordinate who works on what)
4. Break features into smaller pieces (smaller changes = fewer conflicts)
5. Merge main into feature regularly:
   ```bash
   git switch feature-branch
   git merge main
   ```

Prevention is better than resolution. Communication and frequent integration reduce conflicts.

