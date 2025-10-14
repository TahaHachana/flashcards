## Explicit Returns

When and how do you use explicit returns?

---

Use the return keyword for early returns from a function.

```rust
fn absolute_value(x: i32) -> i32 {
    if x < 0 {
        return -x;  // Early return
    }
    x  // Implicit return
}
```

