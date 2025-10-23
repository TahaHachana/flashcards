## Common Mistake Multiple Mutable Borrows

What happens if you try to create two mutable references at once?

---

Compile error. Only one &mut allowed at a time.

```rust
let r1 = &mut s;
let r2 = &mut s;  // ❌ Error
```

