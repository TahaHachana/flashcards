## Infinite Iterators

How do you create and safely use infinite iterators? Show examples with ranges and custom iterators.

---

Infinite iterators never return `None` from `.next()`. They're useful with lazy evaluation but require limiting.

**Creating infinite iterators:**

**1. Unbounded range:**
```rust
let infinite = 0..;  // 0, 1, 2, 3, ... forever
```

**2. `.cycle()` - Repeat sequence:**
```rust
let infinite = vec![1, 2, 3].iter().cycle();
```

**3. Custom implementation:**
```rust
struct Fibonacci {
    a: u64,
    b: u64,
}

impl Iterator for Fibonacci {
    type Item = u64;
    
    fn next(&mut self) -> Option<u64> {
        let current = self.a;
        self.a = self.b;
        self.b = current + self.b;
        Some(current)  // Never returns None!
    }
}
```

**Safe usage - MUST limit:**

**Using `.take()`:**
```rust
let first_ten: Vec<i32> = (0..).take(10).collect();
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Using `.take_while()`:**
```rust
let under_100: Vec<i32> = (0..)
    .take_while(|&x| x < 100)
    .collect();
```

**Short-circuiting methods:**
```rust
let first_even = (1..).find(|x| x % 2 == 0);
// Some(2) - stops searching after finding
```

**⚠️ DANGER - Never do this:**
```rust
// INFINITE LOOP - program hangs!
// (0..).for_each(|x| println!("{}", x));

// INFINITE LOOP - never finishes!
// let all: Vec<i32> = (0..).collect();
```

**Rule:** Always use `.take()`, `.take_while()`, or short-circuiting methods (`.find()`, `.any()`) with infinite iterators.

