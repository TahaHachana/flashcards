## Generic Struct with Methods Pattern

Show the complete pattern for defining a generic struct with methods, including associated functions.

---

```rust
struct Container<T> {
    items: Vec<T>,
}

impl<T> Container<T> {
    // Associated function (constructor)
    fn new() -> Self {
        Container { items: Vec::new() }
    }
    
    // Method that borrows self
    fn len(&self) -> usize {
        self.items.len()
    }
    
    // Method that mutably borrows self
    fn add(&mut self, item: T) {
        self.items.push(item);
    }
    
    // Method that consumes self
    fn into_vec(self) -> Vec<T> {
        self.items
    }
}
```

Pattern: Declare `<T>` after both `struct` and `impl`.

