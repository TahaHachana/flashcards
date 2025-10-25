## Case Conversion

How do you convert strings to uppercase or lowercase?

---

```rust
let s = "  hello world  ";
s.to_uppercase();  // "  HELLO WORLD  "
s.to_lowercase();  // "  hello world  "
```
Both return new Strings. The original is unchanged. Whitespace and punctuation are preserved.

