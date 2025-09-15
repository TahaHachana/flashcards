# Multiple impl Blocks

Can you split methods for the same type across multiple impl blocks?

---

Yes. You can group related methods in separate impl blocks:

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```
