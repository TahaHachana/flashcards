## Matching An Empty Line

What pattern matches an empty line, and how would you delete all empty lines?

---

`^$` (beginning of line immediately followed by end of line, nothing between). Delete them all with `:g/^$/d`.

