## Methods On Enums

How do you implement methods on an enum?

---

Use an `impl` block:

```rust
impl Message {
    fn call(&self) {
        println!("{:?}", self);
    }

    fn is_quit(&self) -> bool {
        matches!(self, Self::Quit)
    }
}
```

