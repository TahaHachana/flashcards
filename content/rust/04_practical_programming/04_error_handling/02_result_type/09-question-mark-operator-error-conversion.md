## Question Mark Operator Error Conversion

How does the `?` operator handle different error types?

---

The `?` operator automatically converts error types using the `From` trait:

```rust
fn complex() -> Result<String, Box<dyn Error>> {
    let contents = std::fs::read_to_string("file.txt")?;  // io::Error
    let number: i32 = contents.trim().parse()?;            // ParseIntError
    Ok(format!("{}", number))
}
```

Both errors are automatically converted to `Box<dyn Error>` through `From` implementations, allowing different error types to work together.

