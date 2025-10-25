## Vec::with_capacity Purpose

When and why should you use `Vec::with_capacity(n)` instead of `Vec::new()`?

---

Use it when you know approximately how many elements you'll add. It pre-allocates enough space, avoiding multiple reallocations and improving performance. Example: `let mut v = Vec::with_capacity(1000);` for 1000 elements.

