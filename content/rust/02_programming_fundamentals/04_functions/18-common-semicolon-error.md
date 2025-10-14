## Common Semicolon Error

What's wrong with this function and how do you fix it?

```rust
fn add(x: i32, y: i32) -> i32 {
    x + y;
}
```

---

The semicolon makes it return () instead of i32. Remove the semicolon to return the value.

```rust
fn add(x: i32, y: i32) -> i32 {
    x + y  // ✅ Now returns i32
}
```

