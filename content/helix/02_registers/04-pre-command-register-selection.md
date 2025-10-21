## Pre-Command Register Selection

What happens when you type `"hc` in Helix?

---

It stores the current selection in register `h`, then changes it (deletes the selection and enters insert mode). Pre-selecting a register preserves the text before a destructive operation.

