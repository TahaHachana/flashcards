## Result<T, E> Enum

What is Result<T, E>, when do you use it, and how does the ? operator work with it?

---

**Definition**:
```rust
enum Result<T, E> {
    Ok(T),     // Success value
    Err(E),    // Error value
}
```

**Use for**: Functions that can fail, returning either success or error.

```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}
```

**The ? operator**: Early returns on error
```rust
fn might_fail() -> Result<i32, String> {
    let value = divide(10.0, 2.0)?;  // Returns Err if error
    Ok(value as i32)  // Continues if Ok
}
```

The `?` operator unwraps `Ok` or returns the `Err` early.

