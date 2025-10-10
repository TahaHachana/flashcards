## Type Inference

Does Rust require explicit type annotations for all variables?

---

No. Rust can usually infer types, but annotations are required when the compiler can't determine the type.

```rust
let x = 5;              // Inferred as i32
let y: f64 = 5.0;       // Explicitly f64
let z: u32 = "42".parse().unwrap();  // Must annotate
```

