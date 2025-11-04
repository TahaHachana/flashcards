## How Rebase Works

What are the 5 steps Git performs during a rebase?

---

When rebasing, Git:
1. Finds common ancestor between branches
2. Saves your commits temporarily
3. Resets your branch to target branch
4. Reapplies commits one by one on top of target
5. Creates new commit hashes (history rewritten)

Important: Original commits are replaced with new commits that have different hashes. This is why rebasing rewrites history.

