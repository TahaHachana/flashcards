## Size Hint Optimization

What is `size_hint()` and why should you implement it? Show the performance benefit.

---

`size_hint()` provides bounds on remaining elements, enabling important optimizations.

**Signature:**
```rust
fn size_hint(&self) -> (usize, Option<usize>) {
    (lower_bound, upper_bound)
}
```

**Returns:**
- Lower bound: minimum remaining elements (must be accurate)
- Upper bound: maximum remaining elements (None = unknown)

**Default implementation (suboptimal):**
```rust
fn size_hint(&self) -> (usize, Option<usize>) {
    (0, None)  // "Don't know"
}
```

**Custom implementation:**
```rust
struct Counter {
    current: u32,
    max: u32,
}

impl Iterator for Counter {
    type Item = u32;
    
    fn next(&mut self) -> Option<u32> {
        if self.current < self.max {
            self.current += 1;
            Some(self.current)
        } else {
            None
        }
    }
    
    fn size_hint(&self) -> (usize, Option<usize>) {
        let remaining = (self.max - self.current) as usize;
        (remaining, Some(remaining))  // Exact size known
    }
}
```

**Performance benefit - pre-allocation:**
```rust
// Without size_hint: multiple allocations
let vec: Vec<_> = counter.collect();
// Vec grows: 0 → 4 → 8 → 16 → 32 → ...
// Multiple reallocations and copies!

// With size_hint: single allocation
let counter = Counter { current: 0, max: 100 };
let vec: Vec<_> = counter.collect();
// Allocates 100 slots immediately
// No reallocations needed!
```

**Other optimizations enabled:**
```rust
// O(1) count instead of O(n)
let counter = Counter { current: 0, max: 1000 };
let count = counter.count();
// Uses size_hint to return immediately without iterating!

// Efficient zip
let a = Counter::new(100);
let b = Counter::new(50);
let zipped: Vec<_> = a.zip(b).collect();
// Knows result will be 50 pairs, allocates once
```

**Different scenarios:**
```rust
// Exact size known
fn size_hint(&self) -> (usize, Option<usize>) {
    let size = self.remaining();
    (size, Some(size))
}

// Only lower bound known (filtered iterator)
fn size_hint(&self) -> (usize, Option<usize>) {
    (0, self.inner.size_hint().1)  // Could be 0, at most inner's max
}

// Range known
fn size_hint(&self) -> (usize, Option<usize>) {
    (self.min_remaining(), Some(self.max_possible()))
}
```

**Accuracy is critical:**
```rust
// ❌ Wrong - returning incorrect size
fn size_hint(&self) -> (usize, Option<usize>) {
    (10, Some(10))  // But we have 5! Undefined behavior!
}

// ✅ Correct - conservative estimate
fn size_hint(&self) -> (usize, Option<usize>) {
    (0, Some(10))  // Safe - lower bound conservative
}
```

Implementing size_hint() can make collect() 2-10x faster for large collections.

