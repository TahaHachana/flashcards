## Rev Adapter

What does `.rev()` do?

---

Reverses the iterator direction:
```rust
let vec = vec![1, 2, 3];
let reversed: Vec<i32> = vec.iter()
    .rev()
    .cloned()
    .collect();
// [3, 2, 1]

// Useful for efficiency:
vec.iter().rev().find(|&&x| x == 5)
// Searches from end, faster if item is near end
```

