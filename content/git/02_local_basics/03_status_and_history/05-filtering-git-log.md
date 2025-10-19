## Filtering git log

How can you filter `git log` by author, date, and commit message?

---

By author: `git log --author="Jane"`
By date: `git log --since="2 weeks ago"` or `git log --until="2025-12-31"`
By message: `git log --grep="authentication"` (add `-i` for case insensitive)
By file: `git log -- path/to/file.txt`

Combine filters: `git log --author="Jane" --since="1 week ago" --grep="bug"`

