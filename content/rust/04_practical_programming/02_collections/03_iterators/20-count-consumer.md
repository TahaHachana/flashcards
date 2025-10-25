## Count Consumer

What does `.count()` do and give an example with filtering.

---

Consumes iterator and returns the number of items:
```rust
let count = vec![1, 2, 3, 4, 5]
    .iter()
    .filter(|&&x| x > 2)
    .count();
// count = 3 (elements 3, 4, 5)
```
Useful after filtering to count matching items.

