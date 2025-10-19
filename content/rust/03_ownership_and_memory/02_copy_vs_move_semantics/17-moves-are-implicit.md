## Moves Are Implicit

Do you need special syntax to move ownership?

---

No. Moves happen automatically on assignment and function calls. The compiler tracks that moved variables are invalid.

```rust
let s1 = String::from("hello");
let s2 = s1;  // Implicit move
```

