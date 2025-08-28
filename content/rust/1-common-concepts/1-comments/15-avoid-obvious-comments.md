# Avoid Obvious Comments

Should you comment obvious code in Rust?

---

No. Avoid commenting obvious code. Focus on why rather than what:
```rust
// Bad
let x = 5; // Assign 5 to x

// Good
let max_retries = 5; // Limit to prevent infinite loops
```