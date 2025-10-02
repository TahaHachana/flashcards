## Defining Methods

How are methods defined for structs in Rust?

---

Inside an `impl` block.
The first parameter is `self` (owned, `&self`, or `&mut self`).

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}
```

