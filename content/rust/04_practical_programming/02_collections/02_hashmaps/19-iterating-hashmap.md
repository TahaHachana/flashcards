## Iterating HashMap

Show three ways to iterate over a HashMap: key-value pairs, keys only, and values only.

---

```rust
// Key-value pairs
for (key, value) in &map {
    println!("{}: {}", key, value);
}

// Keys only
for key in map.keys() {
    println!("{}", key);
}

// Values only
for value in map.values() {
    println!("{}", value);
}
```

