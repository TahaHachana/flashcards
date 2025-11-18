## Associated Types and Object Safety

Are traits with associated types object-safe?

---

Yes, traits with associated types CAN be object-safe:

```rust
trait Iterator {
    type Item;  // Associated type
    fn next(&mut self) -> Option<Self::Item>;
}

// This is object-safe! Iterator can be used as:
let iter: Box<dyn Iterator<Item = i32>> = Box::new(some_iterator);
```

**Key**: When using as a trait object, you must specify the associated type:
```rust
Box<dyn Iterator<Item = i32>>  // ✅ Specifies Item
Box<dyn Iterator>               // ❌ Item type unknown
```

Associated types are fine as long as they're specified when creating the trait object.

