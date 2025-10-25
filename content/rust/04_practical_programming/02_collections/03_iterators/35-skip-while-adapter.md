## Skip While Adapter

What does `.skip_while()` do?

---

Skips items while predicate is true, then yields rest:
```rust
let result: Vec<i32> = vec![1, 2, 3, 4, 5]
    .into_iter()
    .skip_while(|&x| x < 3)
    .collect();
// [3, 4, 5] - skipped [1, 2]
```
Stops skipping at first false, returns everything after.

