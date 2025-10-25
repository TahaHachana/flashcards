## Contains and Pattern Matching

How do you check if a string contains a substring or starts/ends with a pattern?

---

```rust
let s = "  hello world  ";
s.contains("world");  // true

s.starts_with("hello");  // false (has leading spaces)
s.trim().starts_with("hello");  // true

s.ends_with("world");  // false (has trailing spaces)
```
contains() checks anywhere, starts_with()/ends_with() check specific positions.

