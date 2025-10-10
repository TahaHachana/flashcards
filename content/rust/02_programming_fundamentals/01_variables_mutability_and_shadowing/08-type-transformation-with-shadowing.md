## Type Transformation with Shadowing

Why is shadowing useful for type transformations?

---

You can change a variable's type while keeping the same logical name, avoiding cluttered names.

```rust
let spaces = "   ";           // string
let spaces = spaces.len();    // number
// Instead of spaces_str and spaces_count
```

