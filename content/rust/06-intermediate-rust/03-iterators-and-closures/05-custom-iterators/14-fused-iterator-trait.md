## Fused Iterator Trait

What is FusedIterator and why might you want to implement it?

---

`FusedIterator` guarantees the iterator continues returning `None` after the first `None`.

**Trait definition:**
```rust
pub trait FusedIterator: Iterator {}
```

**Purpose:**
- Marks iterator as "fused" (safe to call after exhaustion)
- No required methods - just a marker trait
- Enables optimizations in consuming code

**Default iterator behavior (should but not guaranteed):**
```rust
let mut iter = vec![1, 2].into_iter();

assert_eq!(iter.next(), Some(1));
assert_eq!(iter.next(), Some(2));
assert_eq!(iter.next(), None);
assert_eq!(iter.next(), None);  // Should keep returning None
```

**Problem - non-fused iterator:**
```rust
struct Buggy {
    state: bool,
}

impl Iterator for Buggy {
    type Item = i32;
    
    fn next(&mut self) -> Option<i32> {
        // ❌ Returns None, then Some, then None again!
        self.state = !self.state;
        if self.state {
            Some(42)
        } else {
            None
        }
    }
}
// This violates expected behavior but compiles
```

**Fused implementation:**
```rust
struct Counter {
    current: u32,
    max: u32,
    finished: bool,
}

impl Iterator for Counter {
    type Item = u32;
    
    fn next(&mut self) -> Option<u32> {
        // Once finished, always return None
        if self.finished {
            return None;
        }
        
        if self.current < self.max {
            self.current += 1;
            Some(self.current)
        } else {
            self.finished = true;  // Mark as finished
            None
        }
    }
}

// Mark as fused
impl FusedIterator for Counter {}
```

**Why it matters:**
```rust
// Some adaptors can optimize with FusedIterator
// Example: .fuse() does nothing if already fused
let iter = counter.fuse();  // No-op if FusedIterator

// flatten can optimize
let nested: Vec<Vec<i32>> = /* ... */;
nested.into_iter()
    .flatten()  // Can optimize if inner is fused
    .collect()
```

**When to implement:**
1. Iterator genuinely returns None forever after first None
2. Have explicit "finished" flag
3. Want to enable optimizations

**When NOT to implement:**
```rust
// ❌ Don't implement if behavior isn't guaranteed
struct MaybeFused {
    inner: SomeIter,
}

impl Iterator for MaybeFused {
    fn next(&mut self) -> Option<i32> {
        // If inner isn't fused, neither are we
        self.inner.next()
    }
}
// Don't mark as FusedIterator without checking inner
```

**Standard library:**
Most standard iterators are fused:
```rust
vec.iter()      // Fused
range           // Fused
map/filter      // Fused if input is fused
```

**Testing fusion:**
```rust
#[test]
fn test_fused() {
    let mut iter = Counter::new(3);
    
    assert_eq!(iter.next(), Some(1));
    assert_eq!(iter.next(), Some(2));
    assert_eq!(iter.next(), Some(3));
    assert_eq!(iter.next(), None);
    
    // Test it stays None
    for _ in 0..100 {
        assert_eq!(iter.next(), None);
    }
}
```

FusedIterator is a promise about behavior - implement only if you guarantee it.

