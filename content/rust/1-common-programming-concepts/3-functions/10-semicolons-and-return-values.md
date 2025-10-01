## Semicolons And Return Values

How does a semicolon affect return values in Rust functions?

---

Adding a semicolon to an expression turns it into a statement, so it does not return a value.

```rust
fn plus_one(x: i32) -> i32 {
    x + 1   // returns x + 1
    // x + 1; // ❌ error: mismatched types
}
```

