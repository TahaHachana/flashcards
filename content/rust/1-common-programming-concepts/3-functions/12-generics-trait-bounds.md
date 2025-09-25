## Generics and Trait Bounds

How do you define a generic function with trait bounds?

---

Use angle brackets with `T` and specify required traits after `:`.

Example:

```rust
fn show<T: std::fmt::Display>(x: T) {
    println!("{x}");
}
```

