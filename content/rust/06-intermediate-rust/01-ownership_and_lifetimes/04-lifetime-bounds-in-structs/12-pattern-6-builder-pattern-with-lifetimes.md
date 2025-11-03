## Pattern 6 Builder Pattern with Lifetimes

How does the builder pattern work with borrowed data and lifetime parameters?

---

The builder holds references with lifetime `'a`, uses fluent API (consuming `self` and returning `Self`), and produces a final struct with the same lifetime. Example:
```rust
struct Builder<'a> {
    url: &'a str,
}

impl<'a> Builder<'a> {
    fn method(mut self, m: &'a str) -> Self { ... }
    fn build(self) -> Request<'a> { ... }
}
```
All borrowed data must outlive both builder and final struct.

