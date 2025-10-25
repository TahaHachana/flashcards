## Why Multiple Immutable Are Safe

Why can you have unlimited immutable references?

---

Reading data from multiple places simultaneously is safe. All references are read-only, so no one can modify data and no conflicts are possible.

```rust
let r1 = &s;
let r2 = &s;
let r3 = &s;  // ✅ All safe
```

