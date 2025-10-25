## Collect Type Flexibility

Show three different ways to specify the type when using `.collect()`.

---

```rust
// 1. Variable type annotation
let vec: Vec<i32> = iter.collect();

// 2. Turbofish syntax
let vec = iter.collect::<Vec<i32>>();

// 3. Type inference with underscore
let vec: Vec<_> = iter.collect();
```

