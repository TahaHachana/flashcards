## Array Slices

Can slices work with arrays in Rust?

---

Yes. Slices apply to arrays and collections, not just strings.

```rust
let a = [1, 2, 3, 4, 5];
let slice = &a[1..3]; // &[2, 3]
```

