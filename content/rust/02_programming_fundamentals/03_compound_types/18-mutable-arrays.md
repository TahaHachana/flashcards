## Mutable Arrays

How do you modify array elements?

---

Make the array mutable, then assign to specific indices. Length cannot change.

```rust
let mut arr = [1, 2, 3, 4, 5];
arr[0] = 10;
arr[4] = 50;
println!("{:?}", arr);  // [10, 2, 3, 4, 50]
```

