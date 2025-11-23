## Basic Counter Iterator

Implement a simple Counter iterator that counts from 1 to max. Show how it integrates with iterator methods.

---

A Counter demonstrates the simplest custom iterator pattern.

**Implementation:**
```rust
struct Counter {
    count: u32,
    max: u32,
}

impl Counter {
    fn new(max: u32) -> Self {
        Counter { count: 0, max }
    }
}

impl Iterator for Counter {
    type Item = u32;
    
    fn next(&mut self) -> Option<u32> {
        if self.count < self.max {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}
```

**Usage with for loop:**
```rust
let counter = Counter::new(5);

for num in counter {
    println!("{}", num);
}
// Prints: 1, 2, 3, 4, 5
```

**Free iterator methods:**
```rust
// Sum
let sum: u32 = Counter::new(5).sum();
// 15 (1+2+3+4+5)

// Map and collect
let doubled: Vec<u32> = Counter::new(3)
    .map(|x| x * 2)
    .collect();
// [2, 4, 6]

// Filter and count
let count = Counter::new(10)
    .filter(|x| x % 2 == 0)
    .count();
// 5 (even numbers)

// Chain operations
let result: Vec<_> = Counter::new(10)
    .filter(|x| x % 2 == 0)
    .map(|x| x * x)
    .take(3)
    .collect();
// [4, 16, 36]
```

**Key points:**
- State stored in struct fields (`count`, `max`)
- `next()` mutates state to advance
- Returns `Some` while valid, then `None`
- Automatically works with all iterator methods
- Can be chained with other iterators

This simple implementation demonstrates the power of the Iterator trait - implement two things, get entire ecosystem.

