## Setting awk's Field Separator

How do you make awk split on punctuation as well as spaces, e.g. so "car", "car," and "car." count as one word?

---

Set the field separator to a regex in a BEGIN rule: `BEGIN { FS = "[,. ]+" }`.

