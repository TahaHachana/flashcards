## The Dot Star Combination

What does `.*` mean, and what does `:s/End.*/End/` do?

---

`.*` means "any number of any characters" (dot = any char, star = zero-or-more). `:s/End.*/End/` deletes everything after `End` on the line by replacing the rest of the line with nothing.

