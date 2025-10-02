## Result Enum Usage

What does the `Result<T, E>` enum represent?

---

`Result<T, E>` represents:

* `Ok(T)` for success.
* `Err(E)` for failure.

```rust
fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err("division by zero".to_string())
    } else {
        Ok(a / b)
    }
}
```

