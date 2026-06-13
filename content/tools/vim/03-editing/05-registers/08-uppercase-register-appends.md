## Uppercase Register Appends

What happens when you yank or delete into an uppercase register name like `"Z`?

---

It appends to the matching lowercase register (`z`) instead of overwriting it, letting you accumulate several pieces of text into one register.

