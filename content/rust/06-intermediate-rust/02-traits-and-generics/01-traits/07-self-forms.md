## Three Forms of Self in Traits

What are the three forms of `self` in trait methods, and what does each mean?

---

1. `&self` - Immutable borrow (read-only access)
2. `&mut self` - Mutable borrow (can modify)
3. `self` - Takes ownership (consumes the value)

Example:
```rust
trait Example {
    fn read(&self);           // Borrows
    fn modify(&mut self);     // Borrows mutably
    fn consume(self);         // Takes ownership
}
```

