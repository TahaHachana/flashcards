## Tree Sitter Dependent Textobjects

Which textobjects require tree-sitter grammar and query files to work?

---

`f` (function), `t` (type/class), `a` (argument), `c` (comment), `T` (test), and `g` (change/git hunk) all require an active tree-sitter grammar and special query file for the current document's language.

