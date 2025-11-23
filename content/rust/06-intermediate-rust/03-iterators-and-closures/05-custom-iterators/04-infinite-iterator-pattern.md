## Infinite Iterator Pattern

Show how to implement an infinite iterator. Why is this valid, and how must users consume it?

---

Infinite iterators never return `None` from `next()` - this is valid and useful.

**Fibonacci infinite iterator:**
```rust
struct Fibonacci {
    current: u64,
    next: u64,
}

impl Fibonacci {
    fn new() -> Self {
        Fibonacci { current: 0, next: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;
    
    fn next(&mut self) -> Option<u64> {
        let current = self.current;
        
        // Calculate next Fibonacci number
        self.current = self.next;
        self.next = current + self.next;
        
        // Never returns None!
        Some(current)
    }
}
```

**Why this is valid:**
- Iterator contract allows infinite sequences
- Useful for generators, streams, sequences
- Common pattern in Rust

**Must use limiting operations:**
```rust
// ✅ Take limited number
let first_ten: Vec<u64> = Fibonacci::new()
    .take(10)
    .collect();
// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

// ✅ Take while condition
let small: Vec<u64> = Fibonacci::new()
    .take_while(|&x| x < 100)
    .collect();

// ✅ Find stops when found
let big = Fibonacci::new()
    .find(|&x| x > 1000);
// Some(1597)

// ❌ Would run forever!
// for n in Fibonacci::new() {
//     println!("{}", n);
// }

// ❌ Would hang forever!
// let all: Vec<_> = Fibonacci::new().collect();
```

**Other infinite iterator examples:**
```rust
// Always returns 1
struct Ones;

impl Iterator for Ones {
    type Item = i32;
    fn next(&mut self) -> Option<i32> {
        Some(1)
    }
}

// Infinite counter
struct InfiniteCounter { n: u64 }

impl Iterator for InfiniteCounter {
    type Item = u64;
    fn next(&mut self) -> Option<u64> {
        let current = self.n;
        self.n += 1;
        Some(current)
    }
}
```

**Use cases:**
- Mathematical sequences
- Random number generators
- Event streams
- Retry mechanisms

Infinite iterators are powerful when combined with limiting adaptors.

