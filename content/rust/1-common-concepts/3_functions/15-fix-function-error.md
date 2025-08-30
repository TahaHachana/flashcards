# Fix Function Error

What's wrong with this function?
```rust
fn double(x: i32) -> i32 {
    let result = x * 2;
    result;
}
```

---

The semicolon after `result` makes it a statement, so the function returns `()` instead of `i32`. Fix by removing the semicolon:
```rust
fn double(x: i32) -> i32 {
    let result = x * 2;
    result  // No semicolon
}
```