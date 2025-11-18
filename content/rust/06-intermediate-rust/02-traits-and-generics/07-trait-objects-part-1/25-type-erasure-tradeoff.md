## Type Erasure Trade-off

What are the trade-offs of type erasure with trait objects?

---

**Benefits**:
- Store different types in same collection
- Smaller binary (no monomorphization)
- Runtime flexibility

**Costs**:
- Can't access type-specific methods
- Can't downcast without extra work
- Small runtime overhead (virtual function call)
- Cannot call generic methods on the trait object
- Cannot return or use `Self` in methods

```rust
let animal: Box<dyn Animal> = Box::new(Dog { name: "Rover" });

animal.make_sound();  // ✅ Trait method works
// animal.name;       // ❌ Type-specific field inaccessible
// let dog: Dog = *animal;  // ❌ Can't get Dog back easily
```

You gain flexibility but lose type information.

