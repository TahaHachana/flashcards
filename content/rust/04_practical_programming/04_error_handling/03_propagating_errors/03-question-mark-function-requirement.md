## Question Mark Function Requirement

What requirement must a function meet to use the `?` operator?

---

The function must return a compatible type - either `Result<T, E>` or `Option<T>`:

```rust
// ERROR: Can't use ? in non-Result function
fn broken() -> i32 {
    let value = some_result()?;  // Compile error!
    value
}

// CORRECT: Function returns Result
fn works() -> Result<i32, SomeError> {
    let value = some_result()?;
    Ok(value)
}
```

The `?` operator needs a way to return the error, which requires the function to return a compatible error type.

