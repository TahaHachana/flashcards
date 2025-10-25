## String Slice UTF-8 Boundaries

What requirement must string slices satisfy?

---

Must occur at valid UTF-8 character boundaries. Rust strings are UTF-8, so each character can be multiple bytes. Slicing mid-character causes panic.

```rust
let s = String::from("你好");
let slice = &s[0..3];  // ✅ One character
let slice = &s[0..1];  // ❌ Panics: not on boundary
```

