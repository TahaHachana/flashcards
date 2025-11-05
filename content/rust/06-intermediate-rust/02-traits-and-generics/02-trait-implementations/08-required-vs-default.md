## Required vs Default Methods in Implementation

When implementing a trait, how do you handle methods with default implementations vs required methods?

---

**Required methods** (no body in trait): MUST implement them

**Default methods** (have body in trait): Can either:
1. Use the default (don't write anything)
2. Override with your own implementation

```rust
trait Logger {
    fn log(&self) { println!("Log"); }  // Default
    fn error(&self);                    // Required
}

impl Logger for Simple {
    fn error(&self) { println!("Error!"); }
    // Uses default log()
}

impl Logger for Custom {
    fn log(&self) { println!("Custom log"); }  // Override
    fn error(&self) { println!("Error!"); }
}
```

