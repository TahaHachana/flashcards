## Slices Borrow Data

Do slices take ownership of data?

---

No. Slices borrow data without taking ownership. Original data remains valid after creating a slice.

```rust
let vec = vec![1, 2, 3];
let slice = &vec[1..3];  // Borrow
// vec still valid
```

