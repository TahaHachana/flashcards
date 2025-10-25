## Chaining Adapters

Show how to chain multiple iterator adapters and explain why it's efficient.

---

```rust
let result: Vec<i32> = vec.iter()
    .filter(|&&x| x > 5)
    .map(|x| x * 2)
    .take(3)
    .collect();
```
Efficient due to **zero-cost abstractions** - compiler optimizes the chain to be as fast as hand-written loops. No intermediate collections created.

