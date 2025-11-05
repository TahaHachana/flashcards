## Multiple Trait Implementations

Can a single type implement multiple traits? Provide an example.

---

Yes! A type can implement as many traits as needed. Each implementation is separate.

```rust
struct Point { x: i32, y: i32 }

impl Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

impl Clone for Point {
    fn clone(&self) -> Self {
        Point { x: self.x, y: self.y }
    }
}
```

