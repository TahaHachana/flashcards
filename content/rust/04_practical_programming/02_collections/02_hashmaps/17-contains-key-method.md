## Contains Key Method

How do you check if a key exists in a HashMap without retrieving the value?

---

Use `.contains_key(&key)` which returns a boolean:
```rust
if map.contains_key(&"key") {
    println!("Key exists");
}
```
More idiomatic with entry API:
```rust
map.entry("key").or_insert(default_value);
```

