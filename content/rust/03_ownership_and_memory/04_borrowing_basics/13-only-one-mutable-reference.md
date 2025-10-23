## Only One Mutable Reference

How many mutable references can you have to the same data at once?

---

Only one. This prevents data races by ensuring only one part of code can modify data at a time.

```rust
let r1 = &mut s;
let r2 = &mut s;  // ❌ Error
```

