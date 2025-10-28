## Question Mark With Incompatible Types

What do you do when the error type from `?` doesn't match your function's return type?

---

You have three options:

1. **Change function's error type** to match:
```rust
fn fixed1() -> Result<String, io::Error> {
    let contents = std::fs::read_to_string("file")?;
    Ok(contents)
}
```

2. **Convert the error explicitly** with `map_err()`:
```rust
fn fixed2() -> Result<String, String> {
    let contents = std::fs::read_to_string("file")
        .map_err(|e| e.to_string())?;
    Ok(contents)
}
```

3. **Use a generic error type**:
```rust
fn fixed3() -> Result<String, Box<dyn Error>> {
    let contents = std::fs::read_to_string("file")?;
    Ok(contents)
}
```

