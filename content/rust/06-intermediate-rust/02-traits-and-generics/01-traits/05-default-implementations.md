## Default Trait Implementations

What is a default implementation in a trait, and how do types use it?

---

A default implementation is a method in a trait that has a body (actual code). Types that implement the trait can either:
1. Use the default implementation (no code needed)
2. Override it with their own implementation

Example:
```rust
trait Greet {
    fn greet(&self) {
        println!("Hello!");  // Default implementation
    }
}

impl Greet for Person {}  // Uses default

impl Greet for Robot {
    fn greet(&self) {
        println!("BEEP BOOP");  // Overrides default
    }
}
```

