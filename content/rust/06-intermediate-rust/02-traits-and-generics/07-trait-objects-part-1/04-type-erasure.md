## Type Erasure

What is type erasure in the context of trait objects?

---

Type erasure means losing knowledge of the concrete type, retaining only the trait interface:

```rust
struct Dog;
impl Animal for Dog { /* ... */ }

let animal: Box<dyn Animal> = Box::new(Dog);
// The concrete type (Dog) is erased
// We only know it implements Animal
// Can only call Animal trait methods
```

The concrete type still exists at runtime, but the compiler no longer tracks it. You cannot call Dog-specific methods, only Animal methods.

