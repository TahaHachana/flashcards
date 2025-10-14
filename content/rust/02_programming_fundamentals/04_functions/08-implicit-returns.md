## Implicit Returns

What is an implicit return in Rust?

---

The last expression in a function (without a semicolon) is automatically returned.

```rust
fn square(x: i32) -> i32 {
    x * x  // No semicolon, no return keyword needed
}
```

