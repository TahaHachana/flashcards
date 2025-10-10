## What Is Shadowing

What is shadowing in Rust?

---

Shadowing is declaring a new variable with the same name as a previous variable. The new variable shadows the previous one, making it inaccessible.

```rust
let x = 5;
let x = x + 1;  // Shadows first x
let x = x * 2;  // Shadows second x (x is now 12)
```

