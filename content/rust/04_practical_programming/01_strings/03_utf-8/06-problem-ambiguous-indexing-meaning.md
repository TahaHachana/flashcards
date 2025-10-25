## Problem - Ambiguous Indexing Meaning

What would s[0] mean for this string and why is it ambiguous?
```rust
let s = String::from("你好");  // 2 chars, 6 bytes
```

---

Option A: First byte? Would be 0xE4 (part of '你', invalid on its own)
Option B: First character? Would be '你' (requires scanning all previous bytes)

Neither option is clearly correct. Users might expect different things, so Rust doesn't allow this ambiguous operation.

