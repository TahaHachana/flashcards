## Borrowing Structs

How can functions use structs without taking ownership?

---

By borrowing a reference:

```rust
fn area(rect: &Rectangle) -> u32 {
    rect.width * rect.height
}
```

