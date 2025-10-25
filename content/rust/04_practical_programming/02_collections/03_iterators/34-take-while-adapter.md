## Take While Adapter

What does `.take_while()` do and how is it different from `.take()`?

---

`.take_while()`: Takes items while predicate is true, stops at first false:
```rust
let result: Vec<i32> = vec![1, 2, 3, 4, 5]
    .into_iter()
    .take_while(|&x| x < 4)
    .collect();
// [1, 2, 3] - stops at 4
```

`.take(n)`: Takes exactly n items regardless of values.

