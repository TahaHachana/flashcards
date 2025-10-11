## Integer Type Categories

What are the categories of integer types in Rust?

---

Signed (i8, i16, i32, i64, i128, isize) and unsigned (u8, u16, u32, u64, u128, usize). Signed can be negative, unsigned can only be non-negative.

```rust
let signed: i32 = -42;    // Can be negative
let unsigned: u32 = 42;   // Must be non-negative
```

