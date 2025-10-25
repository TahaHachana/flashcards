## Empty HashMap Type Inference

What's wrong with this code and how do you fix it?
```rust
let mut map = HashMap::new();
// later...
map.insert("key", 10);
```

---

Nothing is wrong if insertion happens in the same scope! Rust can infer types from usage. But if the HashMap is created far from first use, specify types explicitly:
```rust
let mut map: HashMap<&str, i32> = HashMap::new();
```

