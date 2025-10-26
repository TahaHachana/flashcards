## Methods with Additional Parameters

How do you define methods that take additional parameters beyond self?

---

Add parameters after `self` like regular function parameters:

```rust
impl Rectangle {
    // One additional parameter
    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }
    
    // Multiple additional parameters
    fn resize(&mut self, width: f64, height: f64) {
        self.width = width;
        self.height = height;
    }
    
    // Reference parameter
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

// Usage
rect.scale(2.0);
rect.resize(30.0, 40.0);
if rect1.can_hold(&rect2) { }
```

`self` is always first, followed by any additional parameters.

