## Functions with Return Values

How do you specify and return a value from a function in Rust?

---

Declare the return type after `->` and use the final expression in the function body without a semicolon.

Example:
```rust
fn five() -> i32 {
    5
}
```

