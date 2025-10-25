## Problem - Performance Expectations

Why would allowing string indexing create false performance expectations?

---

In most languages, string indexing is O(1) constant time. In UTF-8, getting the Nth character requires scanning from the start - O(n) time:
```rust
let ch = s[100];  // Would need to scan first 100 characters!
```
Users might assume indexing is fast when it's actually slow. Rust makes the cost explicit by requiring chars().nth(n).

