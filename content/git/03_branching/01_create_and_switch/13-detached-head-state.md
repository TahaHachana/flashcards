## Detached HEAD State

What is detached HEAD state and how do you handle it?

---

Detached HEAD occurs when HEAD points directly to a commit instead of a branch.

Happens when: `git checkout a1b2c3d` (checking out specific commit)

Problem: Commits made in detached HEAD aren't on any branch and can be lost.

Solutions:
1. Create branch from detached HEAD: `git switch -c new-branch-name`
2. Return to a branch: `git switch main`

Detached HEAD is useful for examining old commits but risky for new work.

