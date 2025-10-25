## Clearing a Vector

What's the difference between `.clear()` and `vec = Vec::new()` for clearing a vector?

---

`.clear()` removes all elements but keeps the allocated capacity:
```rust
vec.clear();  // len=0, capacity unchanged
```
`vec = Vec::new()` replaces with new empty vector:
```rust
vec = Vec::new();  // len=0, capacity=0, old memory freed
```

