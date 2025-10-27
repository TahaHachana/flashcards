## Option<T> Definition

How is `Option<T>` defined in Rust's standard library?

---

```rust
enum Option<T> {
    Some(T),  // Contains a value of type T
    None,     // Contains no value
}
```

It's part of the prelude, so `Some` and `None` can be used directly without importing.

