## Why Mutable References Are Exclusive

Why can you only have one mutable reference at a time?

---

Prevents data races and memory corruption. If multiple mutable references existed, operations like reallocation could invalidate other references, causing crashes.

```rust
let r1 = &mut vec;
let r2 = &mut vec;  // ❌ Error
// r1.push() could invalidate r2
```

