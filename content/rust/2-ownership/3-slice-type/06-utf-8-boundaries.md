## UTF-8 Boundaries

Why must string slices align to UTF-8 boundaries?

---

Rust strings are UTF-8 encoded.
Slicing in the middle of a multibyte character causes a runtime panic to prevent invalid strings.

