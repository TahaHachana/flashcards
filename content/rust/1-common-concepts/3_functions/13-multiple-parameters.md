# Multiple Parameters

Can you have multiple parameters in a Rust function? How do you separate them?

---

Yes, separate multiple parameters with commas:
```rust
fn calculate(length: f64, width: f64, height: f64) -> f64 {
    length * width * height
}
```