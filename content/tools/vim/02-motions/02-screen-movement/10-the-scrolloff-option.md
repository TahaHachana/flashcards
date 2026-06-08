## The scrolloff Option

Why might `z ENTER` place the current line a few lines below the top instead of exactly at the top?

---

Because `scrolloff` is set to a nonzero value (often 5), keeping that many context lines above/below the cursor. Set `:set scrolloff=0` to disable it.

