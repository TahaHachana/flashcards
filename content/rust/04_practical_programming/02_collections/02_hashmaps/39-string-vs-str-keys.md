## String vs Str Keys

When should you use `HashMap<String, V>` vs `HashMap<&str, V>`?

---

**HashMap<String, V>**: Keys are owned, HashMap controls lifetime
```rust
map.insert(String::from("key"), value);
```

**HashMap<&str, V>**: Keys are borrowed, must outlive HashMap
```rust
map.insert("key", value);  // "key" is &'static str
```

Use String for dynamic keys, &str for static/literal keys.

