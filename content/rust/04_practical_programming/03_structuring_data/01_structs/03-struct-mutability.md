## Struct Mutability Rules

How does mutability work with structs in Rust? Can you make individual fields mutable?

---

The **entire instance** must be mutable to change any field. Rust does not allow marking individual fields as mutable.

```rust
// Immutable - can't change any field
let user = User { /* ... */ };
// user.age = 31;  // ERROR

// Mutable - can change any field
let mut user = User { /* ... */ };
user.age = 31;  // OK
user.active = false;  // OK
```

This is an all-or-nothing approach to mutability.

