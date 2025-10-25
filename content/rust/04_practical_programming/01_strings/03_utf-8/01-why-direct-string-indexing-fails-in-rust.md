## Why Direct String Indexing Fails in Rust

Why doesn't direct string indexing work in Rust?
```rust
let s = String::from("hello");
let first = s[0];  // Error
```

---

UTF-8 characters can be 1-4 bytes, making s[0] ambiguous. Should it return the first byte (might be middle of a character) or the first character (requires scanning)? Neither option is clearly correct. Rust prevents this ambiguity by not allowing direct indexing.

