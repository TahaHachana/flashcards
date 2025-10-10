## Multiple Shadowing

Can you shadow a variable multiple times?

---

Yes. Each `let` creates a new variable that shadows the previous one.

```rust
let x = 5;
let x = x + 1;   // x is now 6
let x = x * 2;   // x is now 12
let x = "text";  // x is now a string
```

