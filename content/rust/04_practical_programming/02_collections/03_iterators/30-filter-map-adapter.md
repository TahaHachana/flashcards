## Filter Map Adapter

What does `.filter_map()` do and what should the closure return?

---

Combines filter and map - closure returns `Option<T>`:
- `Some(value)`: Keep and map to value
- `None`: Filter out

```rust
let strings = vec!["1", "two", "3"];
let numbers: Vec<i32> = strings.iter()
    .filter_map(|s| s.parse().ok())
    .collect();
// [1, 3] - "two" filtered out
```

