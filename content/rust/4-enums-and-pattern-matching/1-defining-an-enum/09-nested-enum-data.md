## Nested Enum Data

How can enums contain complex types and be destructured?

---

```rust
struct Point { x: i32, y: i32 }

enum Shape {
    Circle(i32),
    Rectangle(Point, Point),
}

let s = Shape::Rectangle(Point { x: 0, y: 0 }, Point { x: 10, y: 5 });

match s {
    Shape::Circle(r) => println!("radius = {r}"),
    Shape::Rectangle(Point { x, .. }, Point { y, .. }) =>
        println!("corner at ({x}, {y})"),
}
```

