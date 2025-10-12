## Array Slices

How do you create a slice of an array?

---

Use a reference with a range. Slices have type &[T] and provide a view into the array.

```rust
let arr = [1, 2, 3, 4, 5];
let slice = &arr[1..4];  // [2, 3, 4]
```

