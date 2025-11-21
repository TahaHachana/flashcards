## Implementing Iterator

How do you implement the Iterator trait for a custom type? Show the basic structure.

---

Implementing Iterator requires defining the associated type `Item` and the `next()` method.

**Basic structure:**
```rust
struct Counter {
    count: u32,
    max: u32,
}

impl Iterator for Counter {
    type Item = u32;  // What we produce
    
    fn next(&mut self) -> Option<Self::Item> {
        if self.count < self.max {
            self.count += 1;
            Some(self.count)
        } else {
            None  // Exhausted
        }
    }
}

// Now usable in for loops and with iterator methods
let counter = Counter { count: 0, max: 5 };
for num in counter {
    println!("{}", num); // 1, 2, 3, 4, 5
}
```

**Requirements:**
1. Define `type Item` - the type yielded by the iterator
2. Implement `next()` - return `Some(value)` or `None`
3. Track internal state to know when to stop

Once implemented, you get all iterator methods for free.

