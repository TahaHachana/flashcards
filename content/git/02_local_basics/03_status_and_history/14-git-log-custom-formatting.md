## git log Custom Formatting

How do you customize git log output format and what are common format placeholders?

---

`git log --pretty=format:"%h - %an, %ar : %s"`

Common placeholders:
- `%H` = Full commit hash
- `%h` = Abbreviated hash
- `%an` = Author name
- `%ae` = Author email
- `%ar` = Author date, relative ("2 hours ago")
- `%s` = Commit subject (message)
- `%b` = Commit body

Create aliases for frequently used formats.

