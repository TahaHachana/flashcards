## Documentation Comments Syntax

How do documentation comments differ from regular comments?

---

Doc comments use /// (three slashes) and generate HTML documentation with cargo doc.

```rust
/// Calculates the area of a rectangle.
fn calculate_area(width: f64, height: f64) -> f64 {
    width * height
}
```

