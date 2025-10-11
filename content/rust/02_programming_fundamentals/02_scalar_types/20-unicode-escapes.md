## Unicode Escapes

How do you write Unicode characters using escape sequences?

---

Use \u{} with hex code or \x for ASCII hex.

```rust
let crab = '\u{1F980}';  // 🦀
let letter = '\x41';     // 'A'
```

