## Context Sensitive Replacement Syntax

What is the syntax for a context-sensitive replacement using `:g` and `:s`?

---

`:g/pattern/s/old/new/g` — operate only on lines matching `pattern`, and on those lines substitute `old` with `new` (the trailing `g` replaces all matches per line).

