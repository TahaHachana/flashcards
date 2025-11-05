## PartialEq Derive Implementation

What does the compiler generate when you derive `PartialEq`?

---

The compiler generates an `eq` method that compares all fields:

```rust
// You write:
#[derive(PartialEq)]
struct Point { x: i32, y: i32 }

// Compiler generates:
impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

// Usage:
let p1 = Point { x: 1, y: 2 };
let p2 = Point { x: 1, y: 2 };
assert!(p1 == p2);  // true
```

