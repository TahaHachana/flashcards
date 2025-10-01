## Implicit Return Values

How does a function return a value implicitly in Rust?

---

The final expression in the function body is returned automatically if it has no semicolon.

```rust
fn five() -> i32 {
    5
}
```

