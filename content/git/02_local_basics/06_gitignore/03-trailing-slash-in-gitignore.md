## Trailing Slash in .gitignore

What is the difference between the patterns `build` and `build/` in a `.gitignore` file?

---

```
build    → Matches BOTH a file named build AND a directory
           named build/ (and its contents).

build/   → Matches ONLY a directory named build/, not a file.
           The trailing slash restricts the match to directories.
```

Use the trailing slash when you specifically want to ignore a directory (e.g., `dist/`, `__pycache__/`, `node_modules/`) to avoid accidentally ignoring a file with the same name.

