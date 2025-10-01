## If As Expression

How can an `if` expression be used to assign a value in Rust?

---

Because `if` is an expression, it can return a value.
Both branches must return the same type.

```rust
let condition = true;
let number = if condition { 5 } else { 6 };
```

