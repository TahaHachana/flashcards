## Try Trait Behind Question Mark

What trait powers the `?` operator and why does it work with both `Result` and `Option`?

---

The `?` operator is powered by the `Try` trait (currently unstable):

```rust
trait Try {
    type Output;
    type Residual;
    
    fn branch(self) -> ControlFlow<Self::Residual, Self::Output>;
}
```

Both `Result<T, E>` and `Option<T>` implement `Try`, which is why `?` works with both. The `Try` trait abstracts over "types that represent success or early return."

This is why `?` has consistent behavior across both types - it's using the same underlying mechanism.

