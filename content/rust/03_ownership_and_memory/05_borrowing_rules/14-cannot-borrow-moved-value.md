## Cannot Borrow Moved Value

Can you borrow a value after it's been moved?

---

No. The original variable no longer owns anything, so there's nothing to borrow.

```rust
let s = String::from("hello");
let s2 = s;  // Move
let r = &s;  // ❌ Error: borrowed after move
```

