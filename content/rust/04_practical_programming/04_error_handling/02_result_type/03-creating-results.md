## Creating Results

How do you create `Result` values for success and failure cases?

---

```rust
// Success case
let success: Result<i32, &str> = Ok(42);

// Error case
let failure: Result<i32, &str> = Err("something went wrong");

// In functions
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("division by zero"))
    } else {
        Ok(a / b)
    }
}
```

