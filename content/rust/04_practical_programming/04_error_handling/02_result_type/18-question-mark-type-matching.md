## Question Mark Type Matching

What constraint does the `?` operator place on error types?

---

The error type must be convertible to the function's error type via the `From` trait:

**Won't compile:**
```rust
fn broken() -> Result<i32, String> {
    std::fs::read_to_string("file")?  // io::Error != String
}
```

**Fixed with conversion:**
```rust
fn fixed() -> Result<i32, String> {
    std::fs::read_to_string("file")
        .map_err(|e| e.to_string())?  // Convert to String
}
```

Or use a compatible error type like `Box<dyn Error>`.

