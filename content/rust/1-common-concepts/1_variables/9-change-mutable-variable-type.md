# Change Mutable Variable Type

Can you change the type of a mutable variable?

---

No! This will cause a compile error:
```rust
let mut spaces = "   ";
spaces = spaces.len(); // Error: mismatched types
```