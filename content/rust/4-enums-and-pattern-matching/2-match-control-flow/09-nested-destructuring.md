## Nested Destructuring

How does Rust handle nested destructuring in match patterns?

---

Patterns can destructure complex data directly:

```rust
enum Shape {
    Rectangle { width: i32, height: i32 },
}

match Shape::Rectangle { width: 3, height: 5 } {
    Shape::Rectangle { width, height } =>
        println!("{width} x {height}"),
}
```

