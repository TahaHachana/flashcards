## The Three g Meanings

In `:g/pattern/s/old/new/g`, what do the leading `:g` and the trailing `g` each control?

---

The leading `:g` chooses which lines to act on (lines matching `pattern`). The trailing `g` flag makes the substitution apply to every match on each chosen line, not just the first.

