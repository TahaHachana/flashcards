## Slicing at Valid UTF-8 Boundaries

Why do these slices succeed or fail?
```rust
let s = String::from("你好");
let slice1 = &s[0..3];
let slice2 = &s[0..1];
```

---

&s[0..3] succeeds: Creates "你" (one complete 3-byte character)
&s[0..1] panics: Not on character boundary - would split the character '你'

Slice points must be at character boundaries (the start of a character), never in the middle of a multi-byte character.

