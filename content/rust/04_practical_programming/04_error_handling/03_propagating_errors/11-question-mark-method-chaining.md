## Question Mark Method Chaining

How do you combine `?` with method chaining?

---

You can use `?` at any point in a method chain:

```rust
fn get_first_word(path: &str) -> Result<String, io::Error> {
    Ok(std::fs::read_to_string(path)?
        .split_whitespace()
        .next()
        .ok_or_else(|| io::Error::new(
            io::ErrorKind::InvalidData, 
            "Empty file"
        ))?
        .to_string())
}
```

The `?` unwraps intermediate Results, allowing you to continue chaining methods on the success value.

