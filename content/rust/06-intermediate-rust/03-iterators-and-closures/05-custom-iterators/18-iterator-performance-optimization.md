## Iterator Performance Optimization

What are the key performance optimizations for custom iterators?

---

Optimization strategies for efficient custom iterators.

**1. Implement size_hint():**
```rust
impl Iterator for Counter {
    // ...
    
    fn size_hint(&self) -> (usize, Option<usize>) {
        let remaining = (self.max - self.current) as usize;
        (remaining, Some(remaining))
        // Enables pre-allocation in collect()
    }
}

// Performance impact:
let vec: Vec<_> = Counter::new(10000).collect();
// Without size_hint: ~10 allocations
// With size_hint: 1 allocation
```

**2. Mark as FusedIterator:**
```rust
impl FusedIterator for Counter {}

// Enables optimization in chaining:
iter.fuse().flatten()  // .fuse() is no-op
```

**3. Implement ExactSizeIterator:**
```rust
impl ExactSizeIterator for Counter {
    fn len(&self) -> usize {
        (self.max - self.current) as usize
    }
}

// O(1) count instead of O(n):
let count = counter.count();  // Instant!
```

**4. Use #[inline]:**
```rust
impl Iterator for Counter {
    type Item = u32;
    
    #[inline]  // Hot path - inline for performance
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

**5. Minimize state size:**
```rust
// ❌ Wasteful
struct Wasteful {
    index: usize,      // 8 bytes
    max: usize,        // 8 bytes
    data: Vec<u64>,    // 24 bytes
    temp: Option<u64>, // 16 bytes
}  // Total: 56 bytes

// ✅ Compact
struct Compact {
    index: u32,     // 4 bytes
    max: u32,       // 4 bytes  
    data: &[u64],   // 16 bytes (slice)
}  // Total: 24 bytes - much better cache usage
```

**6. Avoid allocations in next():**
```rust
// ❌ Slow - allocates each iteration
fn next(&mut self) -> Option<String> {
    Some(format!("Item {}", self.index))  // Allocation!
}

// ✅ Fast - return reference or Copy type
fn next(&mut self) -> Option<&str> {
    Some(&self.data[self.index])  // No allocation
}
```

**7. Implement DoubleEndedIterator when possible:**
```rust
impl DoubleEndedIterator for BiDir {
    fn next_back(&mut self) -> Option<i32> {
        // Enables .rev() and reverse iteration
    }
}

// Enables optimizations:
iter.rev().find(predicate)  // Search from end
```

**8. Specialize hot methods:**
```rust
impl Iterator for MyIter {
    // ...
    
    // Override default implementation for performance
    fn count(self) -> usize {
        // Specialized O(1) version
        self.remaining_count()
    }
    
    fn nth(&mut self, n: usize) -> Option<Self::Item> {
        // Specialized version that skips efficiently
        self.index += n;
        self.next()
    }
}
```

**9. Use unchecked operations (carefully):**
```rust
fn next(&mut self) -> Option<i32> {
    if self.index < self.len {
        // Safe: we checked bounds
        let item = unsafe {
            *self.data.get_unchecked(self.index)
        };
        self.index += 1;
        Some(item)
    } else {
        None
    }
}
// Only if profiling shows bounds checks are bottleneck!
```

**10. Batch operations:**
```rust
struct BatchIter<I> {
    inner: I,
    batch_size: usize,
}

impl<I> Iterator for BatchIter<I>
where
    I: Iterator,
{
    type Item = Vec<I::Item>;
    
    fn next(&mut self) -> Option<Vec<I::Item>> {
        // Pre-allocate batch
        let mut batch = Vec::with_capacity(self.batch_size);
        
        for _ in 0..self.batch_size {
            match self.inner.next() {
                Some(item) => batch.push(item),
                None => break,
            }
        }
        
        if batch.is_empty() {
            None
        } else {
            Some(batch)
        }
    }
}
```

**Performance comparison:**
```rust
// Unoptimized
struct Slow {
    data: Vec<BigStruct>,  // Heap allocation
    index: usize,
}
// No size_hint, no inline, large state

// Optimized  
struct Fast {
    data: &'a [SmallStruct],  // Borrowed
    index: u32,  // Smaller type
}

impl Fast {
    #[inline]
    fn next(&mut self) -> Option<&SmallStruct> {
        // ...
    }
    
    fn size_hint(&self) -> (usize, Option<usize>) {
        let remaining = (self.data.len() - self.index as usize);
        (remaining, Some(remaining))
    }
}

impl ExactSizeIterator for Fast {}
impl FusedIterator for Fast {}
```

**Measurement:**
```rust
// Always benchmark!
#[bench]
fn bench_iterator(b: &mut Bencher) {
    b.iter(|| {
        let sum: i32 = MyIter::new().take(10000).sum();
        black_box(sum)
    });
}
```

**Priority:**
1. Implement size_hint (biggest win)
2. Mark traits (FusedIterator, ExactSizeIterator)
3. Inline hot paths
4. Minimize state size
5. Specialize when beneficial
6. Profile before unsafe

Most important: measure before and after optimizations!

