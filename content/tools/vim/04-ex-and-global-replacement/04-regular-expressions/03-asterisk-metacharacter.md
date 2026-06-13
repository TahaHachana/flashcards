## The Asterisk Metacharacter

What does `*` match?

---

Zero or more of the single character (or single-character pattern) immediately before it. `slo*w` matches `slw`, `slow`, `sloow`, etc. Because it allows zero, matching one-or-more requires writing the character twice (e.g. two spaces then `*`).

