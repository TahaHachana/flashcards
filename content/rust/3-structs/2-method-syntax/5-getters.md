# Getters

How can you create a getter method named the same as a struct field?

---

Define a method with no extra parameters that returns the field or a derived value.

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}
```