## Hidden Buffers

What is a hidden buffer, and what enables hiding instead of forcing a save?

---

A hidden buffer is loaded in memory but not displayed in any window. Setting the `hidden` option lets you `:edit` another file while keeping the current modified buffer in memory (flagged `h` in `:ls`) instead of being forced to write it first.

