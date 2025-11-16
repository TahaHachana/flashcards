## Implementing Traits for Generic Types

How do you implement a standard library trait for a generic type with conditional bounds?

---

Use trait bounds to conditionally implement the trait:

```rust
use std::fmt;

struct Wrapper<T> {
    value: T,
}

// Implement Display only when T implements Display
impl<T: fmt::Display> fmt::Display for Wrapper<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Wrapped: {}", self.value)
    }
}

fn main() {
    let w = Wrapper { value: 42 };
    println!("{}", w);  // Works: i32 implements Display
    
    // Wrapper<Vec<i32>> wouldn't implement Display
    // because Vec doesn't implement Display
}
```

