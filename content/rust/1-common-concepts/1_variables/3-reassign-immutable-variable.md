# Reassign Immutable Variable

What happens if you try to reassign an immutable variable?

---

You get a compile-time error. For example:
```rust
let x = 5;
x = 6; // Error: cannot assign twice to immutable variable
```