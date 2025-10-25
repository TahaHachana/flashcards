## What is Merging

What is merging in Git and what's the basic workflow?

---

Merging combines changes from different branches into one branch. It's how parallel lines of development come back together.

Basic workflow:
1. Switch to target branch (branch you want to merge INTO): `git switch main`
2. Merge source branch: `git merge feature-branch`
3. Git combines changes and creates merge commit
4. Target branch now contains all changes

Remember: You merge FROM another branch INTO your current branch.

