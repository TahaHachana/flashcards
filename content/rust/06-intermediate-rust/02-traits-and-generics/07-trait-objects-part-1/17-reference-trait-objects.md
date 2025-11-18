## Reference Trait Objects

When should you use `&dyn Trait` instead of `Box<dyn Trait>`?

---

Use `&dyn Trait` when you don't need ownership:

```rust
// Function parameter - just borrowing
fn draw_shape(shape: &dyn Drawable) {
    shape.draw();
}

fn main() {
    let circle = Circle;
    let square = Square;
    
    draw_shape(&circle);  // Temporary trait object
    draw_shape(&square);
    // circle and square still owned by main
}
```

Use `Box<dyn Trait>` when you need:
- Ownership
- To store in collections
- To return from functions
- Data to outlive the current scope

