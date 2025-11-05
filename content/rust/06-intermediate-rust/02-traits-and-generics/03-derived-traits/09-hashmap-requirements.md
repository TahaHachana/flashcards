## HashMap Key Requirements

What traits must a type derive to be used as a `HashMap` key?

---

A type needs **`Hash` + `Eq`** (which requires `PartialEq`):

```rust
#[derive(PartialEq, Eq, Hash)]
struct UserId(u64);

fn main() {
    use std::collections::HashMap;
    let mut map: HashMap<UserId, String> = HashMap::new();
    map.insert(UserId(1), "Alice".to_string());
}
```

Often you'll also add `Debug` and `Clone` for convenience:
```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
```

