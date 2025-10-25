## What len Returns

What does the len() method return for strings and why is this important to remember?

---

```rust
let s = String::from("你好");
println!("{}", s.len());  // 6 (bytes, not characters)
```
len() returns the byte count, NOT the character count. This is crucial because multi-byte characters make byte count different from character count. Use chars().count() for character count.

