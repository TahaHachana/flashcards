## Reassignment vs Shadowing

What is the difference between reassigning a mutable variable and shadowing?

---

Reassignment modifies the same variable. Shadowing creates a new variable. Only shadowing allows type changes.

```rust
let mut x = 5;
x = 6;  // Reassignment: same variable, same type

let x = 5;
let x = "hi";  // Shadowing: new variable, can change type
```

