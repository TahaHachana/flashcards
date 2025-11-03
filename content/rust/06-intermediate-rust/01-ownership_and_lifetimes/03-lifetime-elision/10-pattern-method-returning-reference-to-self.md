## Pattern Method Returning Reference to Self

Which elision rule applies to methods that return references?

```rust
impl Container {
    fn get_data(&self) -> &str {
        &self.data
    }
}
```

---

Rule 3 applies. With multiple inputs (including `&self`), the lifetime of `self` is assigned to output lifetimes. Expanded:
```rust
impl Container {
    fn get_data<'a>(&'a self) -> &'a str {
        &self.data
    }
}
```
This works because methods returning references almost always return data from `self`.

