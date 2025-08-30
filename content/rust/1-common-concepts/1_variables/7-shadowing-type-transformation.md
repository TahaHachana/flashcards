# Shadowing Type Transformation

Give an example of shadowing with type transformation.

---

```rust
let spaces = "   ";           // &str type
let spaces = spaces.len();    // usize type
```