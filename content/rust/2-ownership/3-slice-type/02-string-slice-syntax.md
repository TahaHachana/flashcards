## String Slice Syntax

How do you create a slice of a `String` in Rust?

---

Use the range syntax with `&string[start..end]` (end exclusive).

```rust
let s = String::from("hello world");
let hello = &s[0..5]; // "hello"
let world = &s[6..11]; // "world"
```

