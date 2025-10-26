## Destructuring Structs

How can you destructure a struct in Rust and where can destructuring be used?

---

Destructure using pattern syntax to extract fields:

```rust
struct Point { x: f64, y: f64 }
let p = Point { x: 1.0, y: 2.0 };

// In let statements
let Point { x, y } = p;

// In function parameters
fn print(&Point { x, y }: &Point) {
    println!("x: {}, y: {}", x, y);
}

// In match expressions
match p {
    Point { x: 0.0, y: 0.0 } => println!("origin"),
    Point { x, y } => println!("({}, {})", x, y),
}
```

Destructuring can happen in let, function parameters, match arms, if let, and while let.

