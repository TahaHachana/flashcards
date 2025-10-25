## Chars vs Bytes for Multi-byte Characters

What's the difference in count between chars() and bytes() for multi-byte characters?

---

```rust
let s = String::from("hello");
s.chars().count()  // 5 characters
s.bytes().count()  // 5 bytes

let s = String::from("你好");  // Two Chinese characters
s.chars().count()  // 2 characters
s.bytes().count()  // 6 bytes (3 bytes per character)
```
chars() counts Unicode characters, bytes() counts raw bytes. Multi-byte UTF-8 characters have more bytes than characters.

