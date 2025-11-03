## Builder Pattern Fluent API

How does the lifetime work in builder/fluent API patterns where methods return `&mut self`?

```rust
impl<'a> Config<'a> {
    fn set(&mut self, key: String, value: String) -> &mut Self {
        self.settings.insert(key, value);
        self
    }
}
```

---

Methods return `&mut Self` to enable method chaining. The lifetime of the returned mutable reference is tied to the original borrow of `self`. This allows fluent method chains like `config.set(k1, v1).set(k2, v2)`. The borrow is held through the entire chain and released at the end.

