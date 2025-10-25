## Cloning to Preserve Ownership

How can you insert a String into a HashMap while keeping ownership of the original?

---

Use `.clone()` to create a copy before inserting:
```rust
let key = String::from("favorite");
let value = String::from("blue");

map.insert(key.clone(), value.clone());

println!("{} {}", key, value); // OK, originals still owned
```
Trade-off: Uses more memory by creating copies.

