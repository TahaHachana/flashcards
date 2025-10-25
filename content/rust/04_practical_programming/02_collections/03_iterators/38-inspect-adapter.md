## Inspect Adapter

What does `.inspect()` do and when is it useful?

---

Calls a closure on each item for debugging/logging without consuming items:
```rust
let result: Vec<i32> = vec![1, 2, 3]
    .into_iter()
    .inspect(|x| println!("Before: {}", x))
    .map(|x| x * 2)
    .inspect(|x| println!("After: {}", x))
    .collect();
```
Useful for debugging iterator chains.

