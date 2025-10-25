## Flat Map Adapter

What does `.flat_map()` do? Give an example.

---

Maps each item to an iterator, then flattens all results:
```rust
let nested = vec![vec![1, 2], vec![3, 4]];

let flat: Vec<i32> = nested.iter()
    .flat_map(|inner| inner.iter())
    .cloned()
    .collect();
// [1, 2, 3, 4]
```
Useful for nested structures.

