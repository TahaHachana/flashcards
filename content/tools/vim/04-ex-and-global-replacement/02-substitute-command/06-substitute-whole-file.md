## Substitute Across The Whole File

Give two equivalent commands that change every occurrence of `old` to `new` in the entire file.

---

`:1,$s/old/new/g` and `:%s/old/new/g` — `%` is shorthand for `1,$` (first line through last line).

