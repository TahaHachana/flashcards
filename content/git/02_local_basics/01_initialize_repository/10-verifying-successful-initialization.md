## Verifying Successful Initialization

What are four ways to verify that `git init` was successful?

---

1. Check for `.git` folder: `ls -la` (should see .git directory)
2. Check Git status: `git status` (should show branch info, not error)
3. Check current branch: `git branch` (shows branch, may be empty)
4. Verify config: `git config --list --local` (shows repo-specific settings)

If any command shows "fatal: not a git repository", initialization failed.

