## Post-Install Setup Checklist

What are the four essential configuration steps to run immediately after installing Git?

---

```bash
# 1. Set your name
git config --global user.name "Your Name"

# 2. Set your email
git config --global user.email "you@example.com"

# 3. Set your preferred editor
git config --global core.editor "code --wait"

# 4. Set the default branch name
git config --global init.defaultBranch main
```

Verify everything with: `git config --list`

