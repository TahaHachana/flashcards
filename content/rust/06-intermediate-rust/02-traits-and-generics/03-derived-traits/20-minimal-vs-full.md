## Minimal vs Full Derives

Compare minimal and full derive patterns. When would you use each?

---

**Minimal** (internal types, simple debugging):
```rust
#[derive(Debug)]
struct Internal {
    complex_field: HashMap<String, Vec<i32>>,
}
```

**Full** (public APIs, data containers):
```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash, PartialOrd, Ord)]
struct PublicData {
    id: u64,
    name: String,
}
```

**Use minimal**: Private types, complex internals, or when Clone/comparison doesn't make sense

**Use full**: Public types, simple data, collections keys, when you need all operations

