## Paste Option Caveat

Why set `:set paste` before pasting code into an auto-indented buffer?

---

Without it, auto-indent treats pasted text as typed input and progressively skews it rightward. `:set paste` disables Vim's automatic features so text comes in intact; reset with `:set nopaste`.

