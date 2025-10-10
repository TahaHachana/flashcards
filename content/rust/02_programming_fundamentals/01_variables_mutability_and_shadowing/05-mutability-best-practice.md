## Mutability Best Practice

When should you use mutable variables in Rust?

---

Use immutability by default. Only add `mut` when you genuinely need to modify the value. This makes code safer and clearer about intent.

```rust
let count = calculate_total();  // Won't change
let mut sum = 0;                // Will accumulate
```

