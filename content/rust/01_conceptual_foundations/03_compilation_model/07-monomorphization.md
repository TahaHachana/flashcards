## Monomorphization

What is monomorphization and why does it slow compilation?

---

Monomorphization generates specialized code for each concrete type used with generics. This creates fast code with no runtime overhead, but means more code to compile.

```rust
fn largest<T>(list: &[T]) -> &T { ... }
largest(&[1, 2, 3]);    // Generates code for i32
largest(&[1.0, 2.0]);   // Generates code for f64
```

