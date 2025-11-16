## Associated Functions vs Methods

What's the difference between associated functions and methods in generic implementations?

---

**Associated functions**: Don't take `self`, called on the type
**Methods**: Take some form of `self`, called on instances

```rust
impl<T> Stack<T> {
    // Associated function (constructor)
    fn new() -> Self {
        Stack { items: Vec::new() }
    }
    
    // Method - borrows immutably
    fn len(&self) -> usize {
        self.items.len()
    }
    
    // Method - borrows mutably
    fn push(&mut self, item: T) {
        self.items.push(item);
    }
    
    // Method - takes ownership
    fn into_vec(self) -> Vec<T> {
        self.items
    }
}

// Usage:
let mut stack = Stack::new();  // Associated function
stack.push(5);                 // Method
```

