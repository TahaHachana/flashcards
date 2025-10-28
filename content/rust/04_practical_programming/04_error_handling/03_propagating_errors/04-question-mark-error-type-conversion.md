## Question Mark Error Type Conversion

How does the `?` operator handle different error types?

---

The `?` operator automatically converts error types using the `From` trait via `.into()`:

```rust
fn flexible() -> Result<(), Box<dyn Error>> {
    std::fs::read_to_string("file")?;  // io::Error
    "123".parse::<i32>()?;              // ParseIntError
    Ok(())
    // Both automatically convert to Box<dyn Error>
}
```

This is why implementing `From<OtherError> for YourError` enables automatic conversion when using `?`.

