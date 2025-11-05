## Copy Requires Clone

What is the relationship between `Copy` and `Clone` when deriving?

---

**`Copy` requires `Clone`**. You must always derive both together.

```rust
// ❌ WRONG
#[derive(Copy)]
struct Point { x: i32, y: i32 }
// Error: Copy requires Clone

// ✅ CORRECT
#[derive(Copy, Clone)]
struct Point { x: i32, y: i32 }
```

This is because `Copy` types must support explicit cloning via `Clone`, even though they're copied implicitly.

