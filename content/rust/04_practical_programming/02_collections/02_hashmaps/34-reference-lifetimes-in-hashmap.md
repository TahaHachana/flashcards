## Reference Lifetimes in HashMap

What's the lifetime constraint when storing references in a HashMap?

---

References must live at least as long as the HashMap:
```rust
let value = String::from("data");
let mut map = HashMap::new();
map.insert("key", &value);  // Stores reference

// value must outlive map
// drop(value); // Would cause error
println!("{:?}", map.get("key")); // Still need value
```

