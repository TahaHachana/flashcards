## Question Mark Basic Behavior

What exactly happens when you use `?` on a `Result<T, E>`?

---

When you use `?` on a Result:

1. **If `Ok(value)`**: Unwraps and returns the value, execution continues
2. **If `Err(e)`**: Converts the error (if needed) and immediately returns `Err(e)` from the function

```rust
// This:
let value = some_operation()?;

// Becomes:
let value = match some_operation() {
    Ok(v) => v,
    Err(e) => return Err(e.into()),
};
```

