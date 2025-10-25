## Collecting Iterator to Vec

Show how to collect an iterator into a Vec, including type annotation.

---

```rust
let vec: Vec<i32> = (1..=5).collect();
// or with turbofish
let vec = (1..=5).collect::<Vec<i32>>();
// or let Rust infer
let vec = (1..=5).collect::<Vec<_>>();
```

