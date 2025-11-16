## Two Fundamental Patterns

What are the two fundamental patterns for generic implementations?

---

**Pattern 1: Unconditional** - Methods for ALL types T
```rust
impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
}
// Available for Container<i32>, Container<String>, etc.
```

**Pattern 2: Conditional** - Methods only when T meets requirements
```rust
impl<T: Display> Container<T> {
    fn print(&self) {
        println!("{}", self.value);
    }
}
// Only available when T implements Display
```

These patterns let you create flexible APIs that provide functionality exactly when it makes sense.

