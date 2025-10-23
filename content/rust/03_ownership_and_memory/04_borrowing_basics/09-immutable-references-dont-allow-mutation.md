## Immutable References Don't Allow Mutation

Can you modify data through an immutable reference?

---

No. Immutable references are read-only.

```rust
let s = String::from("hello");
let r = &s;
r.push_str(" world");  // ❌ Error
```

