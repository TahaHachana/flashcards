## Mutable Slices

Can slices be mutable in Rust?

---

Yes. Use `&mut [start..end]` for mutable slices.
Slices, like references, follow borrowing rules: many immutable slices or one mutable slice at a time.

