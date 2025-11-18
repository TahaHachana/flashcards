## Object Safety Rule 2 - No Generic Methods

Why can't object-safe traits have generic methods?

---

Generic methods are not object-safe because they need compile-time type information, but trait objects work at runtime:

```rust
// ❌ NOT object-safe
trait Processor {
    fn process<T>(&self, value: T);
}

// Error: cannot be made into an object
let obj: Box<dyn Processor> = /* ... */;
```

**Why**: With generics, the compiler generates specialized code for each type. With trait objects, the concrete type isn't known until runtime, so generic methods can't be specialized.

Object-safe traits can only have monomorphic methods (no type parameters).

