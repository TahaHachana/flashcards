## Uninitialized Variables

Can you use a variable before initializing it in Rust?

---

No. Rust requires variables to be initialized before use, preventing undefined behavior.

```rust
let x: i32;
println!("{}", x);  // ❌ Error: possibly uninitialized

let y: i32;
y = 5;
println!("{}", y);  // ✅ OK: initialized before use
```

