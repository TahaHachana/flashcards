## What Ownership Prevents

What bugs do the ownership rules prevent?

---

Use-after-free (can't use data after owner is gone), double-free (only one owner to free data), memory leaks (data freed when owner goes out of scope), and data races (only one owner can mutate).

