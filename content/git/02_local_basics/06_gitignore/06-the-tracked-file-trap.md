## The Tracked-File Trap

You accidentally committed `secrets.env` three commits ago and now add it to `.gitignore`. Is it still tracked? What must you do?

---

**Yes, it is still tracked.** `.gitignore` only prevents untracked files from becoming tracked. Files already in the repository's history continue to be tracked regardless.

**Fix:**
```bash
# 1. Remove from the index (staging area) only — keep file on disk
git rm --cached secrets.env

# 2. Add the rule to .gitignore (if not already done)
echo "secrets.env" >> .gitignore

# 3. Commit both changes
git add .gitignore
git commit -m "Stop tracking secrets.env"
```

**Warning:** the file still exists in all previous commits. To remove it from history entirely, use `git filter-repo` or BFG Repo Cleaner — especially critical for credentials or API keys.

