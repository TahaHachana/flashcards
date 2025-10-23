## Common Mistake Borrowing After Move

Can you borrow a value after it's been moved?

---

No. Once moved, the original is invalid.

```rust
let s = String::from("hello");
let s2 = s;  // Moved
let r = &s;  // ❌ Error: s invalid
```

