## Result<T, E> Definition

How is `Result<T, E>` defined in Rust's standard library?

---

```rust
enum Result<T, E> {
    Ok(T),   // Success - contains the successful value
    Err(E),  // Failure - contains the error value
}
```

- `T` is the type of the success value
- `E` is the type of the error value
- It's part of the prelude, so `Ok` and `Err` can be used directly

