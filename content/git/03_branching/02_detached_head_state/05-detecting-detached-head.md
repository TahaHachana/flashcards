## Detecting Detached HEAD

What are three ways to detect if you're in detached HEAD state?

---

1. `git status`:
   - Detached: "HEAD detached at a1b2c3d"
   - Normal: "On branch main"

2. `git branch`:
   - Detached: `* (HEAD detached at a1b2c3d)`
   - Normal: `* main`

3. `cat .git/HEAD`:
   - Detached: Shows commit hash
   - Normal: `ref: refs/heads/main`

Most GUI tools also show visual warnings about detached HEAD.

