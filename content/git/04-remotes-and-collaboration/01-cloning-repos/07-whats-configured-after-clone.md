## What's Configured After Clone

What is automatically configured after cloning a repository?

---

Automatically set up:
1. Remote named 'origin': `git remote -v`
2. Default branch checked out
3. Remote tracking branches: `git branch -r`
4. Local branches track remote: `git branch -vv`

Verify:
```bash
git remote -v        # Shows origin
git branch -a        # Shows all branches
git status           # Shows current branch
```

Ready to work immediately after clone.

