## Why Mutable and Immutable Cannot Coexist

Why can't mutable and immutable references exist simultaneously?

---

Immutable references expect data won't change. Mutable references can change data, violating immutable references' expectations.

```rust
let r1 = &s;      // Expects s unchanged
let r2 = &mut s;  // ❌ Could change s
```

