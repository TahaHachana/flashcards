## Character Type

What is the char type in Rust, its size, and what can it represent?

---

A Unicode Scalar Value, four bytes in size. Can represent any Unicode character including ASCII, emojis, and symbols.

```rust
let letter = 'A';
let emoji = '🦀';
let chinese = '中';
```

