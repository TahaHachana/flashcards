## The Next Method Mechanics

How does the `.next()` method work? What does it return and what happens when an iterator is exhausted?

---

The `.next()` method is the core of all iteration in Rust.

**Signature:**
```rust
fn next(&mut self) -> Option<Self::Item>
```

**Behavior:**
```rust
let mut iter = vec![1, 2, 3].into_iter();

assert_eq!(iter.next(), Some(1)); // Returns first item
assert_eq!(iter.next(), Some(2)); // Advances and returns second
assert_eq!(iter.next(), Some(3)); // Returns last item
assert_eq!(iter.next(), None);    // Exhausted - returns None
assert_eq!(iter.next(), None);    // Keeps returning None forever
```

**Key characteristics:**
- Takes `&mut self` (mutates iterator state)
- Returns `Option<Item>` - `Some` while items remain, `None` when exhausted
- Advances internal position each call
- Once exhausted, continues returning `None` indefinitely

Every other iterator method is built on repeated calls to `.next()`.

