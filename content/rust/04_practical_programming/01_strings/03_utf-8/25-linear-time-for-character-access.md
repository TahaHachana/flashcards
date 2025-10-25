## Linear Time for Character Access

What is the time complexity of getting the nth character and what's the workaround for faster access?

---

```rust
// O(n) - must scan 999 characters
let ch = s.chars().nth(999);

// Workaround: collect into Vec for O(1) access
let s = String::from("你好世界");
let chars: Vec<char> = s.chars().collect();
let ch = chars[2];  // O(1) access: '世'
```
Trade-off: Vec<char> uses more memory (4 bytes per character) but provides O(1) random access.

