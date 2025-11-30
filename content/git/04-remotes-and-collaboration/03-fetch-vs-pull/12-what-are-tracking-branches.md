## What are Tracking Branches

What is a tracking branch and how do you view them?

---

A tracking branch is a local branch with a direct relationship to a remote branch.

View tracking:
```bash
git branch -vv
# * main    a1b2c3d [origin/main] Latest commit
#   feature b2c3d4e [origin/feature: ahead 2]
```

Set tracking:
```bash
git push -u origin main        # During push
# or
git branch -u origin/main      # For existing branch
```

Tracking enables simple `git pull` and `git push` without specifying remote.

