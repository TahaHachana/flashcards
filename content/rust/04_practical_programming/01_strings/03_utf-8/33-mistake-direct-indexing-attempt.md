## Mistake - Direct Indexing Attempt

Why does this fail and what's the correct approach?
```rust
let s = String::from("hello");
let ch = s[0];
```

---

```rust
// ❌ Error: cannot index into a string
let ch = s[0];

// ✅ Correct: use chars()
let ch = s.chars().next();      // Some('h')
let ch = s.chars().nth(0);      // Some('h')
```
Strings don't support direct indexing due to UTF-8's variable-width encoding. Use chars() to access characters.

