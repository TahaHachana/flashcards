## Slices

What is a slice in Rust and how is it used?

---

A slice is a dynamically sized view into a contiguous sequence.
It doesn’t own the data.

Example:

```rust
let arr = [1, 2, 3, 4];
let slice: &[i32] = &arr[1..3]; // [2, 3]
```

