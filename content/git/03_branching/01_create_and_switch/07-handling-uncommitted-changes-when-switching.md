## Handling Uncommitted Changes When Switching

What are three ways to handle uncommitted changes when Git prevents branch switching?

---

1. Commit changes:
   ```bash
   git add .
   git commit -m "Work in progress"
   git switch other-branch
   ```

2. Stash changes (temporary storage):
   ```bash
   git stash
   git switch other-branch
   git stash pop  # Later retrieve
   ```

3. Discard changes (careful!):
   ```bash
   git restore file.txt
   git switch other-branch
   ```

Choose based on whether you want to keep the changes.

