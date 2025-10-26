## Methods vs Associated Functions

What is the difference between methods and associated functions in Rust?

---

**Methods**: Functions defined in an impl block that take some form of `self` as the first parameter. Called on instances using dot notation.

```rust
impl Rectangle {
    fn area(&self) -> f64 {  // Method
        self.width * self.height
    }
}
rect.area();  // Called with .
```

**Associated functions**: Functions in impl blocks that don't take `self`. Called on the type itself using `::` notation.

```rust
impl Rectangle {
    fn new(width: f64, height: f64) -> Self {  // Associated function
        Rectangle { width, height }
    }
}
Rectangle::new(10.0, 20.0);  // Called with ::
```

