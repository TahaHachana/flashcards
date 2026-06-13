## Bunload Vs Bdelete

What is the difference between `:bunload` and `:bdelete`?

---

`:bunload` removes the buffer from memory but keeps it in the buffer list (so it can be reloaded). `:bdelete` unloads it AND removes it from the buffer list entirely. Add `!` to force either on a modified buffer.

