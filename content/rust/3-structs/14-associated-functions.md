## Associated Functions

What are associated functions in Rust?

---

Functions inside `impl` blocks that don’t take `self`.
Often used as constructors.

```rust
impl Rectangle {
    fn square(size: u32) -> Self {
        Self { width: size, height: size }
    }
}
```

