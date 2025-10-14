## Guard Clauses

What are guard clauses and when should you use them?

---

Early returns that handle edge cases or invalid inputs before main logic.

```rust
fn divide(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 {
        return None;  // Guard clause
    }
    Some(a / b)
}
```

