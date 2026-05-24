## Custom Log Format

Write a `git log` command that outputs one line per commit in this format: `<short hash> <author name> <relative date> — <subject>`, and list the format placeholders used.

---

```bash
git log --format="%h %an %cr — %s"
```

Sample output:
```
521edbe Jane Doe 3 days ago — Convert to HTML
c149e12 Jane Doe 4 days ago — Initial contents of my_website
```

Placeholders:
```
%h   → Abbreviated (short) commit hash
%an  → Author name
%cr  → Committer date, relative ("3 days ago", "2 weeks ago")
%s   → Subject — the first line of the commit message
```

Other useful placeholders: `%H` (full hash), `%ae` (author email), `%ad` (author date), `%D` (ref decorations).

