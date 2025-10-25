## Append vs Extend

What's the difference between `.append()` and `.extend()` for adding multiple elements?

---

`.extend()` takes an iterator and adds elements:
```rust
vec.extend([1, 2, 3]);  // Can use arrays, iterators
```
`.append()` takes another vector and moves all its elements:
```rust
vec1.append(&mut vec2);  // vec2 becomes empty
```

