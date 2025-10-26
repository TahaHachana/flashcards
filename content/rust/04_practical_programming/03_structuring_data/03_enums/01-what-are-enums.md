## What Are Enums and Why Do They Exist?

What is an enum in Rust and how is it more powerful than enums in languages like C or Java?

---

An enum (enumeration) is a type that can be one of several variants, representing data that can be one thing OR another.

**Rust's power**: Unlike C/Java enums, Rust enum variants can carry **different types and amounts of data**:

```rust
// Simple enum (like C/Java)
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

// Powerful Rust enum - variants hold data!
enum Message {
    Quit,                      // No data
    Move { x: i32, y: i32 },  // Named fields
    Write(String),             // Single value
    ChangeColor(u8, u8, u8),  // Multiple values
}
```

This makes Rust enums similar to "algebraic data types" or "tagged unions" in functional languages.

