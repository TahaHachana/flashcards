# Nested Comments

What happens if you try to nest comments in Rust?

---

Regular `//` comments can't be nested since they go to end of line. Block comments `/* */` can be nested:
```rust
/* This /* nested */ comment works */
```
But `//` style is preferred.