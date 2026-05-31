## Backspace Limit In vi-Compatible Mode

In strict vi-compatible mode, how far back can you backspace while inserting?

---

Only up to the point where you entered insert mode — you cannot backspace beyond it. With vi compatibility disabled (nocompatible, the common Linux default) you can backspace past that point.

