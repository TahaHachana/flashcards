## What .gitignore Does

What three specific behaviours does `.gitignore` suppress for matched files?

---

For any file or path matched by a `.gitignore` pattern, Git will:

1. **Not list it** as untracked in `git status`.
2. **Not stage it** when you run `git add .` or `git add -A`.
3. **Not commit it** in any future commit.

`.gitignore` does **not** affect files that are already tracked (already committed). Those continue to be tracked regardless of any ignore rules added later.

