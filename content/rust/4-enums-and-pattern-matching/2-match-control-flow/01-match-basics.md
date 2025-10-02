## Match Basics

What is the structure of a `match` expression in Rust?

---

A `match` compares a value against patterns. Each arm has a pattern and an expression, and the first matching arm runs:

```rust
match value {
    Pattern1 => expr1,
    Pattern2 => expr2,
    _ => fallback,
}
```

