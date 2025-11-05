## What Are Derived Traits?

What are derived traits and what is their purpose?

---

Derived traits are trait implementations that the Rust compiler can generate automatically using the `#[derive()]` attribute. Instead of manually writing implementation code, you ask the compiler to create the implementation for you.

**Purpose**: Reduce boilerplate code for common, predictable trait implementations like `Debug`, `Clone`, `PartialEq`, etc.

Example:
```rust
#[derive(Debug, Clone)]
struct Point { x: i32, y: i32 }
// Compiler generates Debug and Clone implementations
```

