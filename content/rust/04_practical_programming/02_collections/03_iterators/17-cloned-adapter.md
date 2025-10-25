## Cloned Adapter

What does `.cloned()` do and when is it commonly used?

---

Converts `&T` to `T` by cloning (requires `Clone` trait):
```rust
let vec = vec![1, 2, 3];
let owned: Vec<i32> = vec.iter()  // &i32
    .cloned()                      // i32
    .collect();
```
Common after `.filter()` to go from references to owned values.

