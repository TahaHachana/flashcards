## Problem - Slicing Dangers

Why is slicing at arbitrary byte positions dangerous?

---

```rust
let s = String::from("你好");
// If allowed: &s[0..1]
// Would slice in middle of '你' - invalid UTF-8!
```
Slicing could split multi-byte characters, creating invalid UTF-8. Rust only allows slicing at valid character boundaries to maintain UTF-8 validity.

