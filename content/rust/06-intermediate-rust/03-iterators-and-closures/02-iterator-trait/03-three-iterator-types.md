## Three Iterator Types

What are the three types of iterators in Rust? Explain their differences in ownership semantics.

---

Collections provide three methods with different ownership semantics:

**1. `.iter()` - Immutable references:**
```rust
let vec = vec![1, 2, 3];
for item in vec.iter() {
    // item is &i32
}
// vec still available
```

**2. `.iter_mut()` - Mutable references:**
```rust
let mut vec = vec![1, 2, 3];
for item in vec.iter_mut() {
    *item *= 2; // item is &mut i32
}
// vec is [2, 4, 6]
```

**3. `.into_iter()` - Takes ownership:**
```rust
let vec = vec![1, 2, 3];
for item in vec.into_iter() {
    // item is i32 (owned)
}
// vec is no longer available
```

**Important:** A `for` loop automatically calls `.into_iter()`:
```rust
for item in collection { }
// Same as: for item in collection.into_iter() { }
```

