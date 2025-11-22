## Filter Map Combination

What does `.filter_map()` do? When is it more efficient than separate `.filter()` and `.map()`?

---

`.filter_map()` combines filtering and transformation in one operation, returning `Option<T>`.

**Signature:**
```rust
fn filter_map<B, F>(self, f: F) -> FilterMap<Self, F>
where
    F: FnMut(Self::Item) -> Option<B>
```

**How it works:**
- Closure returns `Some(value)` → value kept and extracted
- Closure returns `None` → element discarded

**Parsing with error handling:**
```rust
let numbers: Vec<i32> = vec!["1", "two", "3", "four", "5"]
    .iter()
    .filter_map(|s| s.parse().ok())
    .collect();
// [1, 3, 5] - unparseable strings filtered out
```

**Efficiency comparison:**
```rust
// Less efficient - evaluates twice
data.iter()
    .filter(|s| s.parse::<i32>().is_ok())
    .map(|s| s.parse::<i32>().unwrap())
    .collect()

// More efficient - evaluates once
data.iter()
    .filter_map(|s| s.parse::<i32>().ok())
    .collect()
```

**Pattern matching:**
```rust
enum Status { Active(u32), Inactive }

let active_ids: Vec<u32> = statuses.into_iter()
    .filter_map(|status| match status {
        Status::Active(id) => Some(id),
        Status::Inactive => None,
    })
    .collect();
```

**Use when:**
1. Processing Option/Result sequences
2. Filtering requires computation
3. Pattern matching with extraction

More efficient than separate operations because it evaluates each element only once.

