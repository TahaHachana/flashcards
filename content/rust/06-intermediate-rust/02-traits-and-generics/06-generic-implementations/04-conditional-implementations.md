## Conditional Implementation Pattern

How do you provide different methods based on what traits a generic type implements?

---

Use multiple impl blocks with different trait bounds:

```rust
struct Container<T> {
    value: T,
}

// Methods for ANY T
impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
}

// Methods only when T: Display
impl<T: Display> Container<T> {
    fn print(&self) {
        println!("{}", self.value);
    }
}

// Methods only when T: Clone
impl<T: Clone> Container<T> {
    fn duplicate(&self) -> T {
        self.value.clone()
    }
}
```

Types get different methods depending on their capabilities.

