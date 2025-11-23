## Double Ended Iterator

What is DoubleEndedIterator? Show how to implement bidirectional iteration.

---

`DoubleEndedIterator` allows iteration from both ends simultaneously.

**Trait definition:**
```rust
pub trait DoubleEndedIterator: Iterator {
    fn next_back(&mut self) -> Option<Self::Item>;
}
```

**Implementation example:**
```rust
struct BiDirRange {
    start: i32,
    end: i32,
}

// First implement Iterator (forward)
impl Iterator for BiDirRange {
    type Item = i32;
    
    fn next(&mut self) -> Option<i32> {
        if self.start < self.end {
            let val = self.start;
            self.start += 1;
            Some(val)
        } else {
            None
        }
    }
}

// Then implement DoubleEndedIterator (backward)
impl DoubleEndedIterator for BiDirRange {
    fn next_back(&mut self) -> Option<i32> {
        if self.start < self.end {
            self.end -= 1;
            Some(self.end)
        } else {
            None
        }
    }
}
```

**Usage:**
```rust
let mut bi = BiDirRange { start: 0, end: 5 };

// From front
assert_eq!(bi.next(), Some(0));

// From back
assert_eq!(bi.next_back(), Some(4));

// From front again
assert_eq!(bi.next(), Some(1));

// From back again
assert_eq!(bi.next_back(), Some(3));

// From front
assert_eq!(bi.next(), Some(2));

// Exhausted
assert_eq!(bi.next(), None);
assert_eq!(bi.next_back(), None);
```

**Enables .rev():**
```rust
let reversed: Vec<_> = BiDirRange { start: 0, end: 5 }
    .rev()  // Only works if DoubleEndedIterator
    .collect();
// [4, 3, 2, 1, 0]
```

**Complex example - Vec wrapper:**
```rust
struct VecIter<T> {
    data: Vec<T>,
    front: usize,
    back: usize,
}

impl<T> Iterator for VecIter<T>
where
    T: Clone,
{
    type Item = T;
    
    fn next(&mut self) -> Option<T> {
        if self.front < self.back {
            let item = self.data[self.front].clone();
            self.front += 1;
            Some(item)
        } else {
            None
        }
    }
}

impl<T> DoubleEndedIterator for VecIter<T>
where
    T: Clone,
{
    fn next_back(&mut self) -> Option<T> {
        if self.front < self.back {
            self.back -= 1;
            let item = self.data[self.back].clone();
            Some(item)
        } else {
            None
        }
    }
}
```

**Important invariant:**
Both `next()` and `next_back()` must maintain same remaining elements - they consume from opposite ends of the same sequence.

**Use cases:**
- Reversing iteration
- Processing from both ends
- Palindrome checking
- Window operations

DoubleEndedIterator provides more flexibility than forward-only iteration.

