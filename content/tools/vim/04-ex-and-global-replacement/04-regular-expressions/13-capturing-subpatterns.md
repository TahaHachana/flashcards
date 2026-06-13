## Capturing Subpatterns

What do `\(` and `\)` do, and how many subpatterns can be saved per line?

---

They save the enclosed subpattern into a numbered hold buffer. Up to nine subpatterns can be saved on a single line, replayed later with `\1` through `\9`.

