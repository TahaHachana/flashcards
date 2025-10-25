## Modifying Existing Values

How do you modify an existing value in a HashMap if the key exists, without inserting a default?

---

```rust
if let Some(value) = map.get_mut(&key) {
    *value += 10;  // Modify in place
}
```
Or with entry API:
```rust
map.entry(key).and_modify(|v| *v += 10);
```

