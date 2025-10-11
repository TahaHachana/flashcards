## Integer Division

How does integer division work in Rust?

---

Integer division truncates toward zero, discarding the fractional part.

```rust
let a = 10 / 3;     // 3 (not 3.333...)
let b = -10 / 3;    // -3 (not -3.333...)
let c = 10.0 / 3.0; // 3.333... (float division)
```

