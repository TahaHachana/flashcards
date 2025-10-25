## Sum Consumer

How do you sum all elements in a vector using iterators?

---

```rust
let sum: i32 = vec![1, 2, 3, 4, 5]
    .iter()
    .sum();
// sum = 15

// Or with fold:
let sum = vec.iter().fold(0, |acc, x| acc + x);
```
Type annotation often needed for `.sum()`.

