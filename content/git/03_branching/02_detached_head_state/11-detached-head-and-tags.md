## Detached HEAD and Tags

What happens when you checkout a tag, and how do you work with it?

---

Checking out a tag puts you in detached HEAD:
```bash
git checkout v1.0.0  # Detached HEAD
```

To make changes based on a tag, create a branch:
```bash
# Method 1: Checkout then create branch
git checkout v1.0.0
git switch -c hotfix-v1.0.1

# Method 2: Create branch directly from tag
git switch -c hotfix-v1.0.1 v1.0.0
```

Tags are immutable references, so you must branch to make changes.

