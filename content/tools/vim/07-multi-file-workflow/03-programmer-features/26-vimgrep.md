## Vimgrep

What does `:vimgrep` do, and what is its basic syntax?

---

`:vimgrep` is a built-in grep that fills the Quickfix window with matches across files, useful for refactoring. Syntax: `:vimgrep[!] /pattern/[g][j] file(s)` — e.g. `:vimgrep /++vim++/ *.asciidoc`.

