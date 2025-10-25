## Pre-allocating String Capacity

How does pre-allocating capacity improve String performance? Show an example.

---

Pre-allocating prevents multiple reallocations:
```rust
// May reallocate multiple times
let mut s = String::new();
for _ in 0..1000 {
    s.push('a');
}

// No reallocations
let mut s = String::with_capacity(1000);
for _ in 0..1000 {
    s.push('a');
}
```
The second version is faster because memory is allocated once upfront.

