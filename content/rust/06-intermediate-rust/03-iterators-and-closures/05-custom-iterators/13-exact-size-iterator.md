## Exact Size Iterator

What is ExactSizeIterator and when should you implement it?

---

`ExactSizeIterator` indicates the iterator knows its exact remaining length at all times.

**Trait definition:**
```rust
pub trait ExactSizeIterator: Iterator {
    fn len(&self) -> usize {
        let (lower, upper) = self.size_hint();
        // Default: assumes size_hint is exact
        upper.unwrap()
    }
}
```

**When to implement:**
- Exact remaining count always known
- `size_hint()` returns `(n, Some(n))`
- Length doesn't change during iteration

**Implementation:**
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
        (remaining, Some(remaining))
    }
}

// Mark as exact size
impl ExactSizeIterator for Counter {
    fn len(&self) -> usize {
        (self.max - self.current) as usize
    }
}
```

**Benefits:**
```rust
let counter = Counter { current: 0, max: 100 };

// O(1) length check
assert_eq!(counter.len(), 100);

// Efficient size-based operations
if counter.len() > 50 {
    // Can make decisions without iterating
}

// collect() can pre-allocate exact size
let vec: Vec<_> = counter.collect();
```

**When NOT to implement:**
```rust
// ❌ Don't implement for filtering iterators
struct Filtered<I, F> {
    inner: I,
    predicate: F,
}
// Can't know how many will pass filter!

// ❌ Don't implement if size can change
struct MutatingIter {
    data: Vec<i32>,
}
// If someone else can modify data, size not guaranteed

// ✅ DO implement for fixed-size ranges
impl ExactSizeIterator for Range<i32> {}

// ✅ DO implement for known-size wrappers
impl<I: ExactSizeIterator> ExactSizeIterator for Enumerate<I> {
    fn len(&self) -> usize {
        self.iter.len()  // Same as inner
    }
}
```

**Contract:**
- `len()` must always be accurate
- Must equal number of remaining items
- Should be O(1) or very fast

**Compiler doesn't enforce accuracy** - implementing ExactSizeIterator with wrong len() causes undefined behavior!

**Standard library examples:**
```rust
// Vec iterators are ExactSizeIterator
let v = vec![1, 2, 3, 4, 5];
assert_eq!(v.iter().len(), 5);

// Ranges are ExactSizeIterator
assert_eq!((0..10).len(), 10);

// But filter is NOT
// (0..10).filter(|x| x % 2 == 0).len() // Won't compile
```

Only implement when you can guarantee exact remaining count at all times.

