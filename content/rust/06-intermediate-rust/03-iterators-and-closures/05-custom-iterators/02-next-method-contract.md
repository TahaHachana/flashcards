## Next Method Contract

What is the contract for the `next()` method? Show the expected behavior pattern.

---

The `next()` method must follow a specific contract for correct iterator behavior.

**Contract:**
1. Return `Some(item)` while elements remain
2. Return `None` when exhausted
3. Continue returning `None` forever after first `None`
4. Take `&mut self` to track internal state

**Signature:**
```rust
fn next(&mut self) -> Option<Self::Item>
```

**Expected behavior:**
```rust
let mut iter = vec![1, 2, 3].into_iter();

assert_eq!(iter.next(), Some(1));  // First element
assert_eq!(iter.next(), Some(2));  // Second element
assert_eq!(iter.next(), Some(3));  // Third element
assert_eq!(iter.next(), None);     // Exhausted
assert_eq!(iter.next(), None);     // Still None
assert_eq!(iter.next(), None);     // Forever None
```

**Implementation pattern:**
```rust
struct MyIter {
    data: Vec<i32>,
    index: usize,
}

impl Iterator for MyIter {
    type Item = i32;
    
    fn next(&mut self) -> Option<i32> {
        if self.index < self.data.len() {
            let item = self.data[self.index];
            self.index += 1;  // Advance state
            Some(item)
        } else {
            None  // Exhausted
        }
    }
}
```

**Why `&mut self`:**
- Must track iteration position
- Modify internal state on each call
- Multiple calls advance through elements

**Common mistake - not mutating state:**
```rust
// ❌ Wrong - infinite loop returning same element
fn next(&self) -> Option<i32> {
    if self.index < self.data.len() {
        Some(self.data[self.index])  // Never advances!
    } else {
        None
    }
}
```

The contract ensures iterators behave predictably and work with all iterator methods.

