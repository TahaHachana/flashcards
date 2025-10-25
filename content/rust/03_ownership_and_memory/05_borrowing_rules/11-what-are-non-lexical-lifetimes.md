## What Are Non-Lexical Lifetimes

What are Non-Lexical Lifetimes (NLL)?

---

Modern Rust feature where references are valid from creation until last use, not the entire scope. Makes borrowing more flexible and intuitive.

```rust
let r = &s;
println!("{}", r);  // Last use
s.push_str("!");  // ✅ OK: r no longer active
```

