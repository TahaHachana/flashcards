## Iterator Testing Strategy

What are the essential tests for a custom iterator implementation?

---

Comprehensive iterator testing covers basic behavior, edge cases, and integration.

**Essential test categories:**

**1. Basic iteration:**
```rust
#[test]
fn test_basic_iteration() {
    let mut iter = Counter::new(3);
    
    assert_eq!(iter.next(), Some(1));
    assert_eq!(iter.next(), Some(2));
    assert_eq!(iter.next(), Some(3));
    assert_eq!(iter.next(), None);
}
```

**2. Exhaustion behavior:**
```rust
#[test]
fn test_stays_none() {
    let mut iter = Counter::new(2);
    
    iter.next();
    iter.next();
    assert_eq!(iter.next(), None);
    
    // Verify stays None
    assert_eq!(iter.next(), None);
    assert_eq!(iter.next(), None);
}
```

**3. Empty iterator:**
```rust
#[test]
fn test_empty() {
    let mut iter = Counter::new(0);
    assert_eq!(iter.next(), None);
}
```

**4. Collect integration:**
```rust
#[test]
fn test_collect() {
    let result: Vec<_> = Counter::new(5).collect();
    assert_eq!(result, vec![1, 2, 3, 4, 5]);
}
```

**5. Chaining with adaptors:**
```rust
#[test]
fn test_chaining() {
    let result: Vec<_> = Counter::new(10)
        .filter(|x| x % 2 == 0)
        .map(|x| x * x)
        .take(3)
        .collect();
    assert_eq!(result, vec![4, 16, 36]);
}
```

**6. Consumer methods:**
```rust
#[test]
fn test_consumers() {
    // sum
    let sum: u32 = Counter::new(5).sum();
    assert_eq!(sum, 15);
    
    // count
    let count = Counter::new(10).count();
    assert_eq!(count, 10);
    
    // find
    let found = Counter::new(20).find(|&x| x > 15);
    assert_eq!(found, Some(16));
    
    // any
    assert!(Counter::new(10).any(|x| x == 5));
    assert!(!Counter::new(10).any(|x| x > 10));
}
```

**7. size_hint accuracy:**
```rust
#[test]
fn test_size_hint() {
    let iter = Counter::new(10);
    assert_eq!(iter.size_hint(), (10, Some(10)));
    
    let iter = Counter { current: 7, max: 10 };
    assert_eq!(iter.size_hint(), (3, Some(3)));
    
    let mut iter = Counter::new(5);
    iter.next();
    iter.next();
    assert_eq!(iter.size_hint(), (3, Some(3)));
}
```

**8. For loop compatibility:**
```rust
#[test]
fn test_for_loop() {
    let mut sum = 0;
    for num in Counter::new(5) {
        sum += num;
    }
    assert_eq!(sum, 15);
}
```

**9. DoubleEndedIterator (if implemented):**
```rust
#[test]
fn test_bidirectional() {
    let mut iter = BiDirRange { start: 0, end: 5 };
    
    assert_eq!(iter.next(), Some(0));
    assert_eq!(iter.next_back(), Some(4));
    assert_eq!(iter.next(), Some(1));
    assert_eq!(iter.next_back(), Some(3));
    assert_eq!(iter.next(), Some(2));
    assert_eq!(iter.next(), None);
    assert_eq!(iter.next_back(), None);
}
```

**10. Clone behavior (if clonable):**
```rust
#[test]
fn test_clone() {
    let iter1 = Counter::new(5);
    let iter2 = iter1.clone();
    
    assert_eq!(iter1.collect::<Vec<_>>(), iter2.collect::<Vec<_>>());
}
```

**11. Large iterations:**
```rust
#[test]
fn test_large_count() {
    let count = Counter::new(10_000).count();
    assert_eq!(count, 10_000);
}
```

**12. State mutation:**
```rust
#[test]
fn test_state_advances() {
    let mut iter = Counter::new(3);
    
    assert_eq!(iter.current, 0);
    iter.next();
    assert_eq!(iter.current, 1);
    iter.next();
    assert_eq!(iter.current, 2);
}
```

**Test organization:**
```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    mod basic_behavior {
        // Basic tests
    }
    
    mod edge_cases {
        // Empty, exhaustion, etc.
    }
    
    mod integration {
        // Chaining, consumers, etc.
    }
}
```

Thorough testing ensures your iterator works correctly with the entire ecosystem.

