## Trait Implementation Must Be Complete

What happens if you implement a trait but forget to provide one of its required methods?

---

The code will not compile. You will get a compiler error stating "not all trait items implemented."

```rust
trait Complete {
    fn method_one(&self);
    fn method_two(&self);
}

impl Complete for MyType {
    fn method_one(&self) { }
    // Error: missing method_two
}
```

You must implement ALL required methods (those without default implementations).

