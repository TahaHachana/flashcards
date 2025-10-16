## Public API Documentation

When should you use documentation comments vs regular comments?

---

Use doc comments (///) for public APIs. Regular comments (//) are fine for internal/private code.

```rust
/// Public function - use doc comment
pub fn calculate_total(price: f64) -> f64 { }

// Internal helper - regular comment fine
fn helper() { }
```

