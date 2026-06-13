## Bufdo Command

What does `:bufdo cmd` do, and how does it differ from `:windo`?

---

`:bufdo cmd` runs `cmd` on every buffer in the session (not just visible ones), stopping at the first error. `:windo` only operates on visible windows in the current tab.

