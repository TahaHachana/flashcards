## Trait Bounds and Static Dispatch

How do trait bounds relate to static dispatch and performance?

---

Trait bounds enable **static dispatch** (compile-time polymorphism), which has zero runtime cost:

```rust
fn area<T: Shape>(shape: T) -> f64 {
    shape.area()  // Compiler knows exact type at compile time
}
```

The compiler generates specialized code for each concrete type that calls the function. At runtime, there's no indirection or lookup—the exact method is called directly.

This is different from trait objects (`dyn Trait`) which use dynamic dispatch with a small runtime cost.

