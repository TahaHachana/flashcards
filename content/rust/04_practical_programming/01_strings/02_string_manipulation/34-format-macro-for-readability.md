## Format Macro for Readability

Why is format! more readable than chaining + operators?

---

```rust
// Harder to read, moves s1
let result = s1 + &s2 + &s3;

// Clearer, nothing moved
let result = format!("{}{}{}", s1, s2, s3);
```
format! shows intent clearly, doesn't require &, preserves all variables, and reads like a template. The + chain requires careful tracking of ownership and references.

