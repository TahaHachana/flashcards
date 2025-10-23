## Multiple Readers Pattern

Why can multiple functions borrow data immutably at the same time?

---

Multiple immutable references are safe because all are read-only. No conflicts possible when everyone is just reading.

```rust
let words = word_count(&text);
let chars = char_count(&text);
// text still valid
```

