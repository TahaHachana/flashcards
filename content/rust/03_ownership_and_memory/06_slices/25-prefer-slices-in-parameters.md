## Prefer Slices in Parameters

Why prefer slice parameters over owned or full collection references?

---

More flexible and efficient. Works with arrays, vectors, and subranges. Just borrows, no allocation or deallocation.

```rust
// Less flexible
fn process(v: &Vec<i32>) { }

// More flexible
fn process(s: &[i32]) { }
```

