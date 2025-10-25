## Mutable Blocks Immutable

Can you create an immutable reference while a mutable reference exists?

---

No. Immutable reference expects data won't change, but mutable reference can change it.

```rust
let r1 = &mut s;
let r2 = &s;  // ❌ Error
r1.push_str("!");
```

