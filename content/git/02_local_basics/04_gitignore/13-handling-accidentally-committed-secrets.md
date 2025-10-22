## Handling Accidentally Committed Secrets

What should you do if you accidentally commit sensitive data like API keys?

---

1. Add to .gitignore immediately:
   ```bash
   echo ".env" >> .gitignore
   git add .gitignore
   git commit -m "Add .env to gitignore"
   ```

2. If NOT pushed, remove and amend:
   ```bash
   git rm --cached .env
   git commit --amend --no-edit
   ```

3. If ALREADY pushed:
   - Change ALL secrets immediately (consider them compromised)
   - Rewrite history with git filter-branch or BFG Repo-Cleaner (advanced)
   - Consider repository compromised

PREVENTION: Add sensitive files to .gitignore BEFORE first commit.

