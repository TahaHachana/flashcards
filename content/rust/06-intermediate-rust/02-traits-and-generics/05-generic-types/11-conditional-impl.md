## Conditional Implementation Pattern

How can you provide different methods based on what traits a generic type implements?

---

Use multiple impl blocks with different trait bounds:

```rust
struct Wrapper<T>(T);

// Methods for ANY T
impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper(value)
    }
}

// Methods only when T implements Display
impl<T: Display> Wrapper<T> {
    fn print(&self) {
        println!("{}", self.0);
    }
}

// Methods only when T implements Clone
impl<T: Clone> Wrapper<T> {
    fn duplicate(&self) -> T {
        self.0.clone()
    }
}
```

Types get different methods depending on their capabilities.

