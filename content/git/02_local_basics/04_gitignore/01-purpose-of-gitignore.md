## Purpose of .gitignore

What is the purpose of .gitignore and what types of files should be ignored?

---

.gitignore tells Git which files to ignore—they won't be staged, committed, or shown as untracked.

Files to ignore:

- Generated files (build artifacts, compiled code)
- Temporary files (cache, logs)
- Local files (IDE settings, OS files)
- Sensitive data (passwords, API keys, .env files)

KEY: .gitignore only affects untracked files. Already-tracked files remain tracked even if added to .gitignore.

