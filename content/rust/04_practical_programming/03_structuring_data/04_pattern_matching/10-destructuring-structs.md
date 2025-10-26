## Destructuring Structs in Patterns

Show three different ways to destructure a struct in a match pattern.

---

```rust
struct Point { x: i32, y: i32 }
let p = Point { x: 0, y: 7 };

// 1. Match specific values
match p {
    Point { x: 0, y: 0 } => println!("origin"),
    Point { x: 0, y } => println!("on y-axis at {}", y),
    Point { x, y: 0 } => println!("on x-axis at {}", x),
    Point { x, y } => println!("({}, {})", x, y),
}

// 2. Shorthand when names match
let Point { x, y } = p;

// 3. Ignore some fields
match p {
    Point { x, .. } => println!("x is {}", x),
}
```

The pattern mirrors the struct's structure. Use `..` to ignore remaining fields.

