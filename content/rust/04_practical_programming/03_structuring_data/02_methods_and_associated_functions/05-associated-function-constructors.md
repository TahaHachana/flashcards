## Associated Function Constructors

What is the conventional naming pattern for constructor associated functions in Rust, and why use associated functions for construction?

---

**Convention**: Use `new` for the primary constructor:

```rust
impl Rectangle {
    fn new(width: f64, height: f64) -> Self {
        Rectangle { width, height }
    }
    
    // Alternative constructors
    fn square(size: f64) -> Self {
        Rectangle { width: size, height: size }
    }
    
    fn default() -> Self {
        Rectangle { width: 1.0, height: 1.0 }
    }
}
```

**Why use associated functions**:
- Provide a clear, ergonomic API
- Can validate inputs before construction
- Can have multiple constructors with different names
- Can return Result<Self, Error> for fallible construction
- Called with `Type::new()` syntax

