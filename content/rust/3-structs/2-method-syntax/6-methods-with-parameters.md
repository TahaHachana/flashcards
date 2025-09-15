# Methods with Parameters

How do you define a method that checks if one Rectangle can hold another?

---

```rust
impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```
