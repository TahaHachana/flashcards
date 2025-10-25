## Max and Min Methods

What do `.max()` and `.min()` return?

---

Return `Option<T>` with maximum/minimum value:
```rust
let max = vec![1, 5, 3, 9, 2].into_iter().max();
// Some(9)

let min = vec![1, 5, 3, 9, 2].into_iter().min();
// Some(1)

let empty: Vec<i32> = vec![];
let max = empty.iter().max();
// None
```

