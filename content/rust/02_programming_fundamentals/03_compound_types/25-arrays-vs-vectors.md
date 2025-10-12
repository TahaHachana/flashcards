## Arrays vs Vectors

What is the difference between arrays and vectors?

---

Arrays are fixed-size and stack-allocated. Vectors (Vec<T>) are dynamic-size and heap-allocated. Use arrays when size is known and fixed, vectors when size needs to change.

```rust
let arr = [1, 2, 3];  // Fixed
let mut vec = vec![1, 2, 3];
vec.push(4);  // Can grow
```

