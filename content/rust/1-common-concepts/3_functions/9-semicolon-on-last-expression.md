# Semicolon on Last Expression

What happens if you add a semicolon to the last expression in a function that should return a value?

---

It becomes a statement and returns `()` (unit type) instead, causing a compile-time type mismatch error. For example:
```rust
fn plus_one(x: i32) -> i32 {
    x + 1;  // Error! This returns (), not i32
}
```