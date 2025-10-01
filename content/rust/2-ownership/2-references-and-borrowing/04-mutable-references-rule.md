## Mutable References Rule

What restriction applies to mutable references in Rust?

---

Only **one mutable reference (`&mut`)** is allowed at a time.
This prevents data races at compile time.

