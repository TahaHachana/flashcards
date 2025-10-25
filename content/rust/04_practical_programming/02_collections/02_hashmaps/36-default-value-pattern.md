## Default Value Pattern

What's the idiomatic way to get a value from a HashMap or a default if the key doesn't exist?

---

**Reading**: Use `.get().unwrap_or(&default)`
```rust
let value = map.get(&key).unwrap_or(&0);
```

**Reading and inserting**: Use `.entry().or_insert()`
```rust
let value = map.entry(key).or_insert(0);
```

