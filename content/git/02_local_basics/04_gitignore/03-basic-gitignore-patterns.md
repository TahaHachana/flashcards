## Basic .gitignore Patterns

What do these basic .gitignore patterns do: `*.log`, `node_modules/`, `temp/*`?

---

- `*.log`: Ignore all files ending with .log extension
- `node_modules/`: Ignore the node_modules directory and all its contents
- `temp/*`: Ignore all files inside the temp directory (but not the directory itself)

Add trailing slash to directory patterns for clarity: `build/` (directory) vs `build` (ambiguous).

