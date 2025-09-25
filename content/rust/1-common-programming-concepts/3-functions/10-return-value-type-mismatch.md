## Return Value Type Mismatch

What error occurs if a function's body ends with a statement but a return type is declared?

---

A mismatched types error occurs because statements return `()` (unit type), not the declared type.

Example:
```rust
fn plus_one(x: i32) -> i32 {
    x + 1; // error: expected i32, found ()
}
```

