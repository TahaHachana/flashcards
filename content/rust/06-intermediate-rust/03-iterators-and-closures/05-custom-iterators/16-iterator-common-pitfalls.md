## Iterator Common Pitfalls

What are the most common mistakes when implementing custom iterators?

---

Common pitfalls that break iterator behavior or cause bugs.

**Pitfall 1: Not mutating state**
```rust
// ❌ Wrong - infinite loop!
fn next(&self) -> Option<u32> {  // Should be &mut self
    if self.count < self.max {
        Some(self.count)  // Never advances!
    } else {
        None
    }
}

// ✅ Correct
fn next(&mut self) -> Option<u32> {
    if self.count < self.max {
        self.count += 1;  // Advance state
        Some(self.count)
    } else {
        None
    }
}
```

**Pitfall 2: Not handling exhaustion**
```rust
// ❌ Wrong - panics after exhausted
fn next(&mut self) -> Option<i32> {
    self.index += 1;
    Some(self.data[self.index])  // Panic when out of bounds!
}

// ✅ Correct
fn next(&mut self) -> Option<i32> {
    if self.index < self.data.len() {
        let item = self.data[self.index];
        self.index += 1;
        Some(item)
    } else {
        None
    }
}
```

**Pitfall 3: Incorrect size_hint**
```rust
// ❌ Wrong - hardcoded size
fn size_hint(&self) -> (usize, Option<usize>) {
    (10, Some(10))  // Doesn't reflect current state!
}

// ✅ Correct
fn size_hint(&self) -> (usize, Option<usize>) {
    let remaining = self.max - self.current;
    (remaining, Some(remaining))
}
```

**Pitfall 4: Returning Some after None**
```rust
// ❌ Wrong - violates contract
fn next(&mut self) -> Option<i32> {
    self.toggle = !self.toggle;
    if self.toggle {
        Some(42)  // Returns Some after None!
    } else {
        None
    }
}

// ✅ Correct - use finished flag
fn next(&mut self) -> Option<i32> {
    if self.finished {
        return None;  // Once done, always None
    }
    // ... normal logic
    if exhausted {
        self.finished = true;
        None
    } else {
        Some(value)
    }
}
```

**Pitfall 5: Consuming owned collection**
```rust
// ❌ Wrong - collection unusable after
impl Iterator for MyCollection {
    fn next(&mut self) -> Option<Item> {
        self.items.pop()  // Destroys collection!
    }
}

// ✅ Correct - separate iterator type
struct MyIter<'a> {
    items: &'a [Item],
    index: usize,
}

impl<'a> Iterator for MyIter<'a> {
    fn next(&mut self) -> Option<&'a Item> {
        // Doesn't consume collection
    }
}
```

**Pitfall 6: Incorrect DoubleEndedIterator**
```rust
// ❌ Wrong - front and back don't coordinate
impl DoubleEndedIterator for MyIter {
    fn next_back(&mut self) -> Option<i32> {
        // Doesn't check if overlaps with front!
        self.back -= 1;
        Some(self.data[self.back])
    }
}

// ✅ Correct - check boundaries
fn next_back(&mut self) -> Option<i32> {
    if self.front < self.back {  // Ensure no overlap
        self.back -= 1;
        Some(self.data[self.back])
    } else {
        None
    }
}
```

**Pitfall 7: Off-by-one errors**
```rust
// ❌ Wrong - skips first element
fn next(&mut self) -> Option<i32> {
    self.index += 1;  // Increments before use!
    if self.index < self.len {
        Some(self.data[self.index])
    } else {
        None
    }
}

// ✅ Correct - use then increment
fn next(&mut self) -> Option<i32> {
    if self.index < self.len {
        let item = self.data[self.index];
        self.index += 1;  // Increment after
        Some(item)
    } else {
        None
    }
}
```

**Pitfall 8: Forgetting IntoIterator**
```rust
// ❌ Can't use in for loop
struct MyCollection { /* ... */ }

impl Iterator for MyCollection { /* ... */ }

// for item in collection { }  // Doesn't work!

// ✅ Implement IntoIterator
impl IntoIterator for MyCollection {
    type Item = /* ... */;
    type IntoIter = /* ... */;
    fn into_iter(self) -> Self::IntoIter { /* ... */ }
}
```

**Pitfall 9: Claiming ExactSizeIterator without guarantee**
```rust
// ❌ Wrong - filtered size not exact
impl ExactSizeIterator for Filtered<I> {
    // Can't know filtered count ahead of time!
}

// ✅ Only for genuinely exact sizes
impl ExactSizeIterator for Range<i32> {
    fn len(&self) -> usize {
        (self.end - self.start) as usize  // Always exact
    }
}
```

**Pitfall 10: Complex state causing bugs**
```rust
// ❌ Wrong - too much state, error-prone
struct Complex {
    index: usize,
    sub_index: usize,
    phase: Phase,
    temp: Option<Item>,
    // ...
}

// ✅ Better - simplify or use wrapper
// Keep state minimal and clear
```

**Best practices to avoid pitfalls:**
1. Always test exhaustion behavior
2. Verify size_hint matches actual count
3. Check state advances correctly
4. Test with empty inputs
5. Use separate iterator types for collections
6. Keep state minimal and obvious
7. Test integration with adaptors

