## Creating and Using .gitignore

How do you create a .gitignore file and what are the basic steps to use it?

---

1. Create file in repository root: `touch .gitignore`
2. Add patterns (one per line):
   ```
   *.log
   node_modules/
   .env
   ```
3. Save and commit:
   ```bash
   git add .gitignore
   git commit -m "Add .gitignore file"
   ```

The .gitignore file is committed and shared with collaborators.

