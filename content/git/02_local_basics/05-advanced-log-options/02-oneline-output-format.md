## --oneline Output Format

What exactly does `--oneline` display per commit, and how does it differ from the default `git log` output?

---

`--oneline` shows each commit on a single line:

```
521edbe (HEAD -> main, origin/main) Convert to HTML
c149e12 Initial contents of my_website
```

```
Default git log shows per commit:
  - Full 40-character SHA-1 hash
  - Author name and email on a separate line
  - Date on a separate line
  - Blank line + full commit message (indented)

--oneline shows per commit:
  - 7-character abbreviated hash (still unique for references)
  - Ref decorations (if --decorate is also active)
  - First line of commit message (subject) only
```

The 7-character short hash is sufficient to reference any commit in most repositories.

