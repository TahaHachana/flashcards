## Multiple Traits on One Type

Can a single type implement multiple traits? Provide an example.

---

Yes! A type can implement as many traits as needed.

```rust
struct Button {
    label: String,
}

impl Drawable for Button {
    fn draw(&self) { /* ... */ }
}

impl Clickable for Button {
    fn on_click(&self) { /* ... */ }
}

impl Resizable for Button {
    fn resize(&mut self, size: u32) { /* ... */ }
}
```

This is more flexible than single inheritance in other languages.

