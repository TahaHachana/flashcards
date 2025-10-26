## Consuming Self for Transformations

When and why would you use `self` (taking ownership) instead of `&self` or `&mut self`?

---

Use `self` when:

1. **Transforming into another type**:
```rust
impl Rectangle {
    fn into_square(self) -> Square {
        Square { size: self.width.min(self.height) }
    }
}
```

2. **Builder pattern** (consume and return):
```rust
fn with_width(mut self, width: f64) -> Self {
    self.width = width;
    self
}
```

3. **Preventing further use** after consumption:
```rust
impl File {
    fn close(self) {
        // Release resources
        // File can't be used after this
    }
}
```

After calling a method that takes `self`, the original value is moved and can't be used anymore. This provides compile-time enforcement of usage patterns.

