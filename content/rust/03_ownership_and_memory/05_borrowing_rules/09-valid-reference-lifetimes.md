## Valid Reference Lifetimes

When is a reference's lifetime valid?

---

When it doesn't outlive the data it references. The reference's lifetime must be within the data's lifetime.

```rust
let x = 5;
let r = &x;  // ✅ OK: r's lifetime within x's
println!("{}", r);
```

