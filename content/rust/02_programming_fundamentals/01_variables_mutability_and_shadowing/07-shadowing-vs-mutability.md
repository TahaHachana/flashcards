## Shadowing vs Mutability

What is the difference between shadowing and mutability?

---

Shadowing creates a new variable (can change type), mutability modifies an existing variable (same type).

```rust
let x = 5;
let x = "hello";  // ✅ Shadowing: new variable, different type

let mut x = 5;
x = "hello";  // ❌ Mutability: can't change type
```

