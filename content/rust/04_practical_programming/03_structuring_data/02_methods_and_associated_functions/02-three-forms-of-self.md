## Three Forms of Self

What are the three forms of `self` in Rust methods, and when should you use each?

---

1. **`&self`** (immutable borrow) - Most common
   - Use for reading data, calculations
   - Doesn't modify the instance
   - Multiple calls allowed

2. **`&mut self`** (mutable borrow) - For modifications
   - Use when you need to change the instance
   - Only one mutable borrow at a time

3. **`self`** (takes ownership) - Consumes the value
   - Use for transforming or consuming the instance
   - Original value can't be used afterward
   - Common in builder patterns

```rust
impl Rectangle {
    fn area(&self) -> f64 { }           // Borrow
    fn scale(&mut self, f: f64) { }     // Mutate
    fn into_square(self) -> Square { }  // Consume
}
```

