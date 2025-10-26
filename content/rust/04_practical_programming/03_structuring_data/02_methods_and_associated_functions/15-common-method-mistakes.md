## Common Method Mistakes

What are three common mistakes when defining methods in Rust?

---

1. **Consuming when you meant to borrow**:
```rust
fn area(self) -> f64 { }  // WRONG - takes ownership
fn area(&self) -> f64 { } // RIGHT - just borrows
```

2. **Forgetting self parameter**:
```rust
// This is an associated function, not a method!
fn describe(width: f64) -> String { }
// Should be:
fn describe(&self) -> String { }
```

3. **Multiple mutable borrows through methods**:
```rust
let w = rect.width_mut();  // Borrows rect mutably
let h = rect.height_mut(); // ERROR: second mutable borrow
// Must not hold onto multiple mutable references
```

Use `&self` by default unless you specifically need mutation or consumption.

