## Documentation for Arguments

How do you document function arguments in doc comments?

---

Use # Arguments section with bullet points.

```rust
/// Calculates area.
///
/// # Arguments
/// * `width` - The width
/// * `height` - The height
fn area(width: f64, height: f64) -> f64 { }
```

