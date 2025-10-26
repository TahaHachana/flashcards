## Method Call vs Associated Function Call Syntax

What syntax error occurs if you confuse method calls and associated function calls?

---

**Error**: Using `.` for associated functions or `::` for methods

```rust
impl Rectangle {
    fn new(w: f64, h: f64) -> Self { }  // Associated function
    fn area(&self) -> f64 { }            // Method
}

// WRONG
let rect = Rectangle.new(10.0, 20.0);  // ERROR
let area = Rectangle::area();           // ERROR

// CORRECT
let rect = Rectangle::new(10.0, 20.0); // :: for associated functions
let area = rect.area();                 // . for methods
```

**Rule**:
- `::` for associated functions (called on the type)
- `.` for methods (called on instances)

