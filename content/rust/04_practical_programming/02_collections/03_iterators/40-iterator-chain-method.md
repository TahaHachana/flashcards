## Iterator Chain Method

What does `.chain()` do?

---

Connects two iterators into one sequential iterator:
```rust
let vec1 = vec![1, 2, 3];
let vec2 = vec![4, 5, 6];

let combined: Vec<i32> = vec1.iter()
    .chain(vec2.iter())
    .cloned()
    .collect();
// [1, 2, 3, 4, 5, 6]
```
First iterator exhausted, then second.

