## Generic Enums

How do generic enums work? Give an example.

---

Enums can be generic over types, with different variants holding different instances of the generic type:

```rust
enum MyResult<T, E> {
    Ok(T),
    Err(E),
}

fn divide(a: f64, b: f64) -> MyResult<f64, String> {
    if b == 0.0 {
        MyResult::Err(String::from("Division by zero"))
    } else {
        MyResult::Ok(a / b)
    }
}
```

Standard library examples: `Option<T>`, `Result<T, E>`, `Vec<T>`.

Each variant can contain the generic type in different ways.

