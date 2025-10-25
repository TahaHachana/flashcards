## Filter Adapter Purpose

What does `.filter()` do and what should the closure return?

---

`.filter()` keeps only items matching a condition. Closure must return `bool`:
```rust
let evens: Vec<i32> = vec.iter()
    .filter(|&&x| x % 2 == 0)  // Keep if true
    .cloned()
    .collect();
```
Returns `true` to keep item, `false` to discard.

