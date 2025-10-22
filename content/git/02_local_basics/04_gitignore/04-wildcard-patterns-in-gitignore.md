## Wildcard Patterns in .gitignore

What do these wildcard patterns mean in .gitignore: `*`, `?`, `**`, `[abc]`?

---

- `*`: Matches zero or more characters except `/` (e.g., `*.txt` matches all .txt files)
- `?`: Matches exactly one character (e.g., `file?.txt` matches file1.txt, fileA.txt)
- `**`: Matches zero or more directories (e.g., `**/*.log` matches .log files anywhere)
- `[abc]`: Character class, matches a, b, or c (e.g., `file[123].txt`)
- `[!abc]`: Negated class, matches anything except a, b, c

