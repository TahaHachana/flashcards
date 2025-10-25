## Enumerate Adapter

What does `.enumerate()` do and what type does it return?

---

Adds an index to each item, returning `(usize, T)` tuples:
```rust
for (index, value) in vec.iter().enumerate() {
    println!("Index {}: {}", index, value);
}
// Output: Index 0: ..., Index 1: ..., etc.
```
Index starts at 0.

