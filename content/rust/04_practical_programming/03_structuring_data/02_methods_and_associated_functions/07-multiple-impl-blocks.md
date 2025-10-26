## Multiple impl Blocks

Can you have multiple impl blocks for the same type in Rust? When might this be useful?

---

**Yes**, you can have multiple impl blocks:

```rust
impl Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

impl Rectangle {
    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }
}
```

**Useful for**:
- Organizing related methods into logical groups
- Separating trait implementations from inherent methods
- Adding methods conditionally with `#[cfg]` attributes
- Keeping impl blocks focused and readable
- Generic implementations for specific type parameters

All methods are equally accessible regardless of which impl block they're in.

