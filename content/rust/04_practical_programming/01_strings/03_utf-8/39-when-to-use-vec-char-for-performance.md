## When to Use Vec char for Performance

When should you convert a String to Vec<char> and what's the trade-off?

---

```rust
let s = String::from("你好世界");
let chars: Vec<char> = s.chars().collect();

// Now O(1) random access
let ch = chars[2];  // '世'
```
Use when: You need frequent random character access (nth character multiple times)

Trade-off: 
- Pro: O(1) access instead of O(n)
- Con: Uses more memory (4 bytes per character in Vec vs variable 1-4 bytes in String)

