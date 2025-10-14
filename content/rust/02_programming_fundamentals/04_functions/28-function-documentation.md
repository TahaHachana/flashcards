## Function Documentation

How should you document complex functions?

---

Use doc comments (///) describing purpose, arguments, and behavior.

```rust
/// Calculates compound interest.
///
/// # Arguments
/// * `principal` - Initial amount
/// * `rate` - Annual rate (0.05 for 5%)
fn compound_interest(principal: f64, rate: f64) -> f64 {
    // ...
}
```

