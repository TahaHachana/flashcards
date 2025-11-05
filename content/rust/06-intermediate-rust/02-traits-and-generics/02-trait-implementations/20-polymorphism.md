## Trait Implementation Enables Polymorphism

How do trait implementations enable polymorphism in Rust?

---

Multiple different types can implement the same trait, allowing them to be used interchangeably where that trait is required.

```rust
trait Shape {
    fn area(&self) -> f64;
}

struct Circle { radius: f64 }
struct Square { side: f64 }

impl Shape for Circle {
    fn area(&self) -> f64 {
        3.14 * self.radius * self.radius
    }
}

impl Shape for Square {
    fn area(&self) -> f64 {
        self.side * self.side
    }
}

// Generic function works with ANY Shape
fn print_area<T: Shape>(shape: T) {
    println!("Area: {}", shape.area());
}
```

Different types, same interface!

