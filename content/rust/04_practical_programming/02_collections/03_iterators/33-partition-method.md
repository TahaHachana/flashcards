## Partition Method

What does `.partition()` do?

---

Splits into two collections based on predicate:
```rust
let vec = vec![1, 2, 3, 4, 5, 6];

let (evens, odds): (Vec<i32>, Vec<i32>) = vec
    .into_iter()
    .partition(|&x| x % 2 == 0);

// evens = [2, 4, 6]
// odds = [1, 3, 5]
```
Must specify both tuple types.

