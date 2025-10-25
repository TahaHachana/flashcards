## Slow Character Operations

Which string operations are O(n) linear time and why?

---

```rust
s.chars().count()    // O(n) - must scan entire string
s.chars().nth(10)    // O(n) - must scan first 10 chars
```
Character operations require validation and scanning because UTF-8 is variable-width. Each character must be decoded to find character boundaries.

