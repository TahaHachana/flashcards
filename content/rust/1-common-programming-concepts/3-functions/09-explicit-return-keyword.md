## Explicit Return Keyword

When would you use the `return` keyword in Rust functions?

---

Use `return expr;` to exit early or make returns explicit.

```rust
fn abs(x: i32) -> i32 {
    if x < 0 {
        return -x;
    }
    x
}
```

