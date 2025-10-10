## Immutability by Default

Are Rust variables mutable or immutable by default?

---

Immutable by default. Once you bind a value to a variable, you cannot change it unless explicitly marked as mutable with `mut`.

```rust
let x = 5;
x = 6;  // ❌ Error: cannot assign twice to immutable variable
```

