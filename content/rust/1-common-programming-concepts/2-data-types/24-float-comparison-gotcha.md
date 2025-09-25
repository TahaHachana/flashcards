## Float Comparison Gotcha

Why is comparing floats with `==` unreliable in Rust?

---

Floats use IEEE-754 and can’t represent some values exactly.
Direct equality may fail. Use an epsilon check:

```rust
let a = 0.1 + 0.2;
let b = 0.3;
assert!((a - b).abs() < f64::EPSILON);
```

