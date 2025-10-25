## Previous Sibling with Fallback

What does `Alt-p` do, and what is its special fallback behavior?

---

Moves to the previous sibling node. Special fallback: if there's no previous sibling, it moves up the syntax tree and selects the previous element. For example, from `arg1` in `func(arg1, arg2, arg3)`, it moves to `func` since `arg1` has no previous sibling.

