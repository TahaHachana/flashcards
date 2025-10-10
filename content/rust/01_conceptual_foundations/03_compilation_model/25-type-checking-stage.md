## Type Checking Stage

What does the type checking stage verify during compilation?

---

It verifies all types are used correctly and catches type mismatches at compile time. This prevents type confusion and ensures type safety before the program runs.

```rust
let x: i32 = "hello";  // ❌ Compile error
```

