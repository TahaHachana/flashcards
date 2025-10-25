## Escape Space in Argument

How do you escape a space in an unquoted command argument on Unix?

---

Use a backslash: `:open a\ b.txt` is equivalent to `:open 'a b.txt'`. The backslash escapes the space character to prevent argument splitting.

