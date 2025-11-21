## Iterator Trait Definition

What is the Iterator trait in Rust? What are its required components?

---

The Iterator trait is Rust's foundation for working with sequences of values, providing a standardized way to traverse collections lazily.

**Required components:**
```rust
pub trait Iterator {
    type Item;  // Associated type
    fn next(&mut self) -> Option<Self::Item>; // Required method
    // ... 50+ provided methods
}
```

**Two requirements:**
1. **Associated type `Item`** - Specifies what type the iterator produces
2. **`next()` method** - Returns `Some(value)` or `None`

All other iterator methods (map, filter, collect, etc.) are provided by the trait and built on top of `next()`.

The trait enables unified iteration across all collection types with zero-cost abstractions.

