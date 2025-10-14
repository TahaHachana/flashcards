## Semicolon Impact on Returns

What does adding a semicolon do to an expression?

---

It turns an expression into a statement, changing the return value to unit ().

```rust
fn returns_five() -> i32 {
    5  // Expression: returns 5
}
fn returns_nothing() {
    5;  // Statement: returns ()
}
```

