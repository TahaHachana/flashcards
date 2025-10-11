## Numeric Type Inference

How does Rust infer numeric types from context?

---

Rust infers types from usage. Integers default to i32, floats to f64.

```rust
let x = 5;      // i32
let y = 5.0;    // f64
let z = 42u8;   // Explicitly u8
```

