## Pattern 6 Struct Methods With Lifetime Parameters

How do methods work on structs that already have lifetime parameters?

```rust
struct Parser<'a> {
    input: &'a str,
    position: usize,
}

impl<'a> Parser<'a> {
    fn current_token(&self) -> &'a str {
        &self.input[self.position..self.position+5]
    }
}
```

---

The struct has lifetime parameter `'a`, and methods can return references with that lifetime. Methods can also introduce additional lifetimes (`'b`) for method-specific references. Methods inherit the struct's lifetime for returning references to internal data. Mental shortcut: "Struct owns the lifetime" → methods inherit it.

