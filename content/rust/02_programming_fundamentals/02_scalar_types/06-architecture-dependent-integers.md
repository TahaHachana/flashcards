## Architecture-Dependent Integers

What are isize and usize, and when should you use them?

---

Architecture-dependent integers: i32/u32 on 32-bit systems, i64/u64 on 64-bit systems. Use usize for array/vector indices, collection sizes, and memory operations.

```rust
let vec = vec![1, 2, 3];
let length: usize = vec.len();
```

