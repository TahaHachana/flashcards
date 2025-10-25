## Character Boundaries Example

For the string "café", what are the valid slice boundaries and why?

---

```rust
let s = String::from("café");
// Byte positions: 0  1  2  3  4  5
// Characters:     c  a  f  é (2 bytes)
// Valid slices:   ^  ^  ^  ^     ^

&s[0..1]  // ✅ "c"
&s[0..3]  // ✅ "caf"
&s[0..4]  // ❌ Panics: middle of 'é'
&s[0..5]  // ✅ "café"
```
Position 4 is invalid because it's in the middle of the 2-byte character 'é'.

