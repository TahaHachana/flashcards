## Reinitializing an Existing Repository

What happens if you run `git init` in a directory that's already a Git repository?

---

It's SAFE. Git will:
- Recognize the existing `.git` folder
- Preserve all data and history
- Keep existing configuration
- Ensure repository structure is correct
- Output: "Reinitialized existing Git repository..."

This is sometimes used to repair corrupted repository structure, but rarely needed.

