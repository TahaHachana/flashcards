## Self vs self

What is the difference between `Self` (capital S) and `self` (lowercase s) in Rust?

---

**`Self`** (capital) = The type itself (alias for the type name)
```rust
impl Rectangle {
    fn new(width: f64, height: f64) -> Self {  // Returns Rectangle
        Self {  // Same as Rectangle {
            width,
            height,
        }
    }
}
```

**`self`** (lowercase) = The instance
```rust
impl Rectangle {
    fn double(&self) -> Self {  // Takes instance, returns Rectangle
        Self {
            width: self.width * 2.0,  // self = this instance
            height: self.height * 2.0,
        }
    }
}
```

`Self` is particularly useful in generic contexts where the type name is complex.

