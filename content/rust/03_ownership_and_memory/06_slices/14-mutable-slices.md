## Mutable Slices

How do you create and use mutable slices?

---

Use &mut with range syntax. Original data must be mutable. Only one mutable slice at a time.

```rust
let mut arr = [1, 2, 3];
let slice = &mut arr[1..3];
slice[0] = 10;  // Modify through slice
```

