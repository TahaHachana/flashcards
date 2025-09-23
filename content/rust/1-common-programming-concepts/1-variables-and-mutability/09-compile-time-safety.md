## Compile-Time Safety

How does Rust enforce variable immutability at compile time?

---

The compiler produces an error if you try to reassign an immutable variable.
This check happens at **compile time**, preventing runtime bugs.

```rust
let x = 5;
x = 6; // ❌ error[E0384]: cannot assign twice to immutable variable
```

