## Arrays vs Tuples Element Types

What is the key difference between arrays and tuples regarding element types?

---

Arrays must have all elements of the same type. Tuples can have elements of different types.

```rust
let arr = [1, 2, 3];  // All i32
let tup = (1, 2.5, "hi");  // Different types
```

