## Taking Ownership vs Borrowing

What's the difference between these two function signatures and their effects?
```rust
fn consume(s: String) { }
fn borrow(s: &str) { }
```

---

consume() takes ownership - it consumes the String and drops it at the end. The caller can't use the String afterwards.
borrow() borrows a reference - the String remains valid after the call.
```rust
let text = String::from("hello");
borrow(&text);   // text still valid
consume(text);   // text moved, no longer valid
```

