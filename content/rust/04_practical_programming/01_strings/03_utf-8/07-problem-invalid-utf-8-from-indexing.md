## Problem - Invalid UTF-8 from Indexing

Why would byte-based indexing break Rust's UTF-8 guarantee?

---

```rust
let s = String::from("你好");
// If s[0] returned first byte (0xE4)...
// That's not a complete character! Invalid UTF-8.
```
Returning a byte could produce invalid UTF-8 since multi-byte characters would be split. Rust guarantees strings are always valid UTF-8, so byte indexing would break this guarantee.

