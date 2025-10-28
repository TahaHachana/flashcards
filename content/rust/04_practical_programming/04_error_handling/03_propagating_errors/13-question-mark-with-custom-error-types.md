## Question Mark With Custom Error Types

How do you enable `?` to automatically convert to your custom error type?

---

Implement the `From` trait for automatic conversion:

```rust
#[derive(Debug)]
enum MyError {
    Io(io::Error),
    Parse(String),
}

impl From<io::Error> for MyError {
    fn from(err: io::Error) -> Self {
        MyError::Io(err)
    }
}

fn my_function() -> Result<(), MyError> {
    std::fs::read_to_string("file")?;  // Auto-converts!
    Ok(())
}
```

The `?` operator calls `From::from()` automatically, converting `io::Error` to `MyError`.

