## Key Takeaways About Detached HEAD

What are the essential principles to remember about detached HEAD state?

---

1. Detached HEAD is NOT an error—it's a normal Git state
2. HEAD should point to a branch (attached) for normal development
3. Detached HEAD is for temporary inspection and experimentation
4. Commits in detached HEAD must be saved to a branch or they'll be lost
5. Use `git switch -c branch-name` to save work immediately
6. Use `git reflog` to recover lost commits (within ~30 days)
7. When in doubt, create a branch before committing

Remember: HEAD → branch → commit (normal); HEAD → commit (detached, risky for new work)

