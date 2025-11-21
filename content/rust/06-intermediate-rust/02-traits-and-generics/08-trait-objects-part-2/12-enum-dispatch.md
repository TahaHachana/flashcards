## Enum Dispatch Alternative

How can enums provide an alternative to trait objects, and when is this better?

---

Enums can achieve polymorphism without vtables:

```rust
enum Shape {
    Circle(Circle),
    Square(Square),
    Triangle(Triangle),
}

impl Shape {
    fn area(&self) -> f64 {
        match self {
            Shape::Circle(c) => c.area(),
            Shape::Square(s) => s.area(),
            Shape::Triangle(t) => t.area(),
        }
    }
}
```

**Advantages over trait objects**:
- No heap allocation needed
- No vtable lookup overhead
- Can exhaustively match on variants
- Better for small, closed sets of types
- Slightly faster (direct call, not indirect)

**Use when**: You have a fixed, known set of types and want maximum performance.

