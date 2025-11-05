## Copy Requires Clone

What is the relationship between the `Copy` and `Clone` traits?

---

`Copy` requires `Clone`. You cannot implement `Copy` without also implementing `Clone`.

```rust
// ❌ WRONG
#[derive(Copy)]
struct Point { x: i32, y: i32 }
// Error: Copy requires Clone

// ✅ CORRECT
#[derive(Copy, Clone)]
struct Point { x: i32, y: i32 }
```

This is because `Copy` is a marker trait that indicates a type can be copied by simply copying bits, but it must also support explicit cloning via `Clone`.

