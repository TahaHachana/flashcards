## Collect Into HashMap

How do you collect an iterator of tuples into a HashMap?

---

```rust
let pairs = vec![("a", 1), ("b", 2), ("c", 3)];

let map: HashMap<_, _> = pairs.into_iter().collect();
```

The iterator must yield `(K, V)` tuples. Rust infers or you specify the HashMap type.

