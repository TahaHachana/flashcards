## The Drop Trait

What is the Drop trait?

---

A trait with one method that defines cleanup behavior. When a value goes out of scope, Rust automatically calls its drop method.

```rust
pub trait Drop {
    fn drop(&mut self);
}
```

