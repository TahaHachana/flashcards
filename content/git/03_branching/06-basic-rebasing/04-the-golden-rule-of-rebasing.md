## The Golden Rule of Rebasing

What is the golden rule of rebasing and why does it matter?

---

**Never rebase commits that have been pushed to a shared/public repository**

Once commits are public, don't rewrite them because:
- Rewriting breaks others' work
- Creates divergent histories
- Forces collaborators to fix their branches
- Destroys trust in shared history

Safe: Rebase local, unpushed commits
Dangerous: Rebase pushed commits on shared branches

Use merge instead for public/shared branches.

