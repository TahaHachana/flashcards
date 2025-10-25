## Slices vs Owned Collections Performance

Why are slices more efficient than owned collections for read-only functions?

---

Slices just borrow - no allocation, copying, or deallocation. Owned collections require taking ownership and eventual freeing.

```rust
fn read(data: &[i32]) { }  // Just borrows
fn own(data: Vec<i32>) { }  // Must allocate/free
```

