## Global .gitignore

What is a global .gitignore file and how do you set it up?

---

A global ignore file applies to ALL your repositories for personal patterns (OS files, IDE settings, personal notes).

Setup:
```bash
# Create global ignore file
touch ~/.gitignore_global

# Configure Git to use it
git config --global core.excludesfile ~/.gitignore_global

# Add personal patterns
echo ".DS_Store" >> ~/.gitignore_global
echo ".vscode/" >> ~/.gitignore_global
```

Use for patterns that apply everywhere but aren't project-specific.

