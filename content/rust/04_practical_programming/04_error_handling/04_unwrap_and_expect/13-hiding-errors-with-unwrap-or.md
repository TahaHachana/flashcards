## Hiding Errors With Unwrap Or

What's the danger of silently providing defaults instead of handling errors?

---

**Bad - hides failures silently:**
```rust
fn load_data() -> Vec<Item> {
    load_from_file("data.json").unwrap_or(Vec::new())
    // Silently returns empty vec on any error - hard to debug!
}
```

**Better - log the error:**
```rust
fn load_data() -> Vec<Item> {
    match load_from_file("data.json") {
        Ok(items) => items,
        Err(e) => {
            eprintln!("Warning: Failed to load data: {}", e);
            Vec::new()
        }
    }
}
```

**Best - propagate the error:**
```rust
fn load_data() -> Result<Vec<Item>, Error> {
    load_from_file("data.json")
}
```

Silent failures make debugging impossible. Either log errors or propagate them.

