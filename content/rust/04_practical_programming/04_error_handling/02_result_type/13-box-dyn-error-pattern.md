## Box Dyn Error Pattern

Why use `Box<dyn Error>` as an error type and when is it appropriate?

---

`Box<dyn Error>` is a generic error type that can hold any error implementing the `Error` trait:

```rust
fn complex() -> Result<String, Box<dyn Error>> {
    let contents = std::fs::read_to_string("file.txt")?;  // io::Error
    let number: i32 = contents.trim().parse()?;            // ParseIntError
    Ok(format!("{}", number))
}
```

**When to use:**
- Applications where you don't need to handle specific error types
- When dealing with multiple error types
- For prototyping or simple programs

**Drawbacks:** You lose type information about the specific error.

