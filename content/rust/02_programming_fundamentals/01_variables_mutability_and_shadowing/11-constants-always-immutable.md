## Constants Always Immutable

Can you use `mut` with constants?

---

No. Constants are always immutable. You cannot declare a mutable constant.

```rust
const mut MAX: u32 = 100;  // ❌ Error: invalid syntax
```

