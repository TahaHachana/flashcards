## Floating-Point Types

What floating-point types does Rust have, and which is the default?

---

Rust has:

* `f32` (32-bit, single precision)
* `f64` (64-bit, double precision, default)

Both are signed and follow IEEE-754.

Example:

```rust
let x = 2.0;      // f64 by default
let y: f32 = 3.0; // f32
```

