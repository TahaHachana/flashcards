## Comparing Commits and Branches

How do you compare two commits or branches with git diff?

---

Two commits: `git diff a1b2c3d b2c3d4e`
Commit and its parent: `git diff a1b2c3d~1 a1b2c3d`
Current branch vs another: `git diff main feature-branch`
Specific file between branches: `git diff main feature -- path/to/file.txt`

Two dots (`..`): differences between endpoints
Three dots (`...`): changes since branches diverged

