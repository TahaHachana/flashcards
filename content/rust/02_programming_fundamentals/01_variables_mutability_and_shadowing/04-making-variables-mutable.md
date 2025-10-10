## Making Variables Mutable

How do you make a variable mutable in Rust?

---

Use the `mut` keyword when declaring the variable:

```rust
let mut x = 5;
x = 6;  // ✅ OK: x is mutable
```

