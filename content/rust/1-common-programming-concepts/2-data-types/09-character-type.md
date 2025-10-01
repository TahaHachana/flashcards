## Character Type

What does the `char` type in Rust represent?

---

A `char` is 4 bytes and represents a Unicode scalar value.
It can hold ASCII, accented letters, CJK characters, emoji, etc.
It does not necessarily equal a grapheme cluster.

```rust
let heart = '❤';
let smile = '😻';
```

