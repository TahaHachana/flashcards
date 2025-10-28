## Pattern Matching With Result

How do you safely extract values from a `Result<T, E>` using pattern matching?

---

Use a `match` expression to handle both cases:

```rust
match result {
    Ok(value) => {
        // Use the success value
    }
    Err(error) => {
        // Handle the error
    }
}
```

The compiler enforces exhaustive matching, ensuring both `Ok` and `Err` cases are handled.

