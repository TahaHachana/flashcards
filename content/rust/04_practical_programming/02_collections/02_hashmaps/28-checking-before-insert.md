## Checking Before Insert

Show two ways to insert a value only if the key doesn't already exist.

---

**Method 1**: Using `.contains_key()`
```rust
if !map.contains_key(&key) {
    map.insert(key, value);
}
```

**Method 2**: Using `.entry()` (more idiomatic)
```rust
map.entry(key).or_insert(value);
```

