## Why Vim Needs No Built-In Transforms

Why can Vim sort, dedupe, reflow, and reshape text without having any of these features built in?

---

Because the filter operator pipes lines to any external Unix command and swaps in its output. The editor doesn't need to know the tools — it just delegates to them.

