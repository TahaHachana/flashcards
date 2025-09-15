# Associated Functions

What is an associated function and how do you call one?

---

An associated function is defined in an impl block without a self parameter and is called with the :: syntax.

```rust
impl Rectangle {
    fn square(size: u32) -> Self {
        Self { width: size, height: size }
    }
}

let sq = Rectangle::square(3);
```
