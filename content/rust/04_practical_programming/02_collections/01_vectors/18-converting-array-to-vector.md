## Converting Array to Vector

Show two ways to convert an array `[1, 2, 3]` into a `Vec<i32>`.

---

```rust
// Method 1: Using .into()
let v1: Vec<i32> = [1, 2, 3].into();

// Method 2: Using vec! macro
let v2 = vec![1, 2, 3];
```

