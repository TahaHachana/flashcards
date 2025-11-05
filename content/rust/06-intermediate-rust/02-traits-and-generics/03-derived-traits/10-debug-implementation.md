## How Debug Derive Works

What does the compiler generate when you derive `Debug`?

---

The compiler generates a `fmt` method that prints the struct name and all fields:

```rust
// You write:
#[derive(Debug)]
struct Point { x: i32, y: i32 }

// Compiler generates (conceptually):
impl Debug for Point {
    fn fmt(&self, f: &mut Formatter) -> Result {
        f.debug_struct("Point")
            .field("x", &self.x)
            .field("y", &self.y)
            .finish()
    }
}

// Output: Point { x: 10, y: 20 }
```

