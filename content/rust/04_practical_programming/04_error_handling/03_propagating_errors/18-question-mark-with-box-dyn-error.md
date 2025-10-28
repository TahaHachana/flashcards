## Question Mark With Box Dyn Error

Why does `Box<dyn Error>` work so well with `?` for handling multiple error types?

---

`Box<dyn Error>` can hold any error type that implements the `Error` trait:

```rust
fn process() -> Result<(), Box<dyn Error>> {
    let contents = std::fs::read_to_string("file")?;  // io::Error
    let number: i32 = contents.trim().parse()?;        // ParseIntError
    Ok(())
}
```

The `?` operator automatically converts different error types to `Box<dyn Error>` via `From` implementations. This is convenient for applications but loses specific error type information (you can't match on specific error types later).

