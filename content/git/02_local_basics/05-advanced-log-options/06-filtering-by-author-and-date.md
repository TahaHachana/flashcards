## Filtering by Author and Date

Write a `git log` command to show the last 5 commits by the author "Jane" made in the last two weeks, one line per commit.

---

```bash
git log --oneline \
        --author="Jane" \
        --since="2 weeks ago" \
        -n 5
```

Key flags:
```
--author="Jane"       → Substring match against author name
                        or email address.

--since="2 weeks ago" → Only show commits after this point.
                        Also accepts ISO dates: "2024-01-01"
                        and natural language: "yesterday".

-n 5                  → Limit output to 5 most recent matches.
```

