## Feature Branch Workflow

What are the steps in a typical feature branch workflow?

---

1. Start on main: `git switch main`
2. Create feature branch: `git switch -c feature/user-profile`
3. Work and commit: `git add . && git commit -m "Add profile"`
4. More commits as needed
5. Switch back: `git switch main`
6. Merge feature: `git merge feature/user-profile`
7. Delete branch: `git branch -d feature/user-profile`

This keeps main stable while developing features in isolation.

