## Slice to Vec Conversion

How do you convert a slice `&[i32]` into an owned `Vec<i32>`?

---

```rust
let slice = &[1, 2, 3, 4];
let vec = slice.to_vec();  // Creates owned copy
// or
let vec2: Vec<i32> = slice.into();  // Also works
```
Both clone the data into a new heap-allocated vector.

