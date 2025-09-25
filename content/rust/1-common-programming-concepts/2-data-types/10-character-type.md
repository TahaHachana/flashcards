## Character Type

What is the size and range of Rust's `char` type?

---

* Size: 4 bytes
* Represents a Unicode scalar value (U+0000 to U+D7FF and U+E000 to U+10FFFF).

Example:

```rust
let c = 'z';
let z: char = 'ℤ';
let emoji = '😻';
```

