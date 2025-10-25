## Common Mistake - Unnecessary Allocations

What's inefficient about this function and how can you improve it?
```rust
fn check(text: String) -> bool {
    text.len() > 5
}
```

---

Taking String requires ownership transfer, forcing callers to move or clone their strings unnecessarily. Better to borrow:
```rust
fn check(text: &str) -> bool {
    text.len() > 5
}
```
This version just borrows, avoiding ownership transfer and allowing the caller to keep using their string.

