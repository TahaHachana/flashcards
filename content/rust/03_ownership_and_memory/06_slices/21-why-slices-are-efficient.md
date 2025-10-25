## Why Slices Are Efficient

Why is creating a slice efficient?

---

Just copies pointer and length, doesn't copy the data. Passing slices is cheap - only two values.

```rust
let large = vec![0; 1_000_000];
let slice = &large[..];  // Fast: just pointer + length
```

