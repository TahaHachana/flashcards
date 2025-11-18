## Trait Objects vs Generics

What's the fundamental difference between using trait objects and generics?

---

**Generics (static dispatch)**:
```rust
fn process<T: Display>(value: T) {
    println!("{}", value);
}
// Compiler generates specialized code for each type
// Type known at compile time
```

**Trait objects (dynamic dispatch)**:
```rust
fn process(value: &dyn Display) {
    println!("{}", value);
}
// One function handles all types
// Type determined at runtime
```

**Generics**: Faster (no indirection), larger code size (monomorphization)
**Trait objects**: Small runtime cost (virtual call), smaller code size, enables heterogeneous collections

