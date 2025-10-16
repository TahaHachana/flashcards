## Documenting Panics

How should you document when a function can panic?

---

Use a # Panics section in doc comments.

```rust
/// Divides two numbers.
///
/// # Panics
/// Panics if denominator is zero
fn divide(a: f64, b: f64) -> f64 {
    if b == 0.0 { panic!("Division by zero"); }
    a / b
}
```

