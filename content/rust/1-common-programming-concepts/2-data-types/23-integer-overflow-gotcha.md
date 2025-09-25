## Integer Overflow Gotcha

How does Rust handle integer overflow, and how can you manage it?

---

* Debug mode: panics at runtime.
* Release mode: wraps with two’s complement.

Helper methods for explicit handling:

* `wrapping_*`, `checked_*`, `overflowing_*`, `saturating_*`

Example:

```rust
let x: u8 = 255;
let y = x.wrapping_add(1); // 0
```

