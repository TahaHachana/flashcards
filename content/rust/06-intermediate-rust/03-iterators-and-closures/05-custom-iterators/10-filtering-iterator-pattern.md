## Filtering Iterator Pattern

How do you create a filtering iterator that skips elements based on a condition?

---

Filtering iterators use a loop in `next()` to skip unwanted elements.

**Pattern:**
```rust
struct EvensOnly<I> {
    inner: I,
}

impl<I> Iterator for EvensOnly<I>
where
    I: Iterator<Item = i32>,
{
    type Item = i32;
    
    fn next(&mut self) -> Option<i32> {
        // Loop until we find an even number
        loop {
            match self.inner.next() {
                Some(n) if n % 2 == 0 => return Some(n),  // Found even
                Some(_) => continue,  // Skip odd
                None => return None,  // Exhausted
            }
        }
    }
}

// Usage
let evens = EvensOnly {
    inner: 1..=10,
};
let result: Vec<_> = evens.collect();
// [2, 4, 6, 8, 10]
```

**Why loop is needed:**
```rust
// ❌ Wrong - only checks one element
fn next(&mut self) -> Option<i32> {
    match self.inner.next() {
        Some(n) if n % 2 == 0 => Some(n),
        _ => None,  // Returns None after first odd!
    }
}

// ✅ Correct - keeps trying
fn next(&mut self) -> Option<i32> {
    loop {
        match self.inner.next() {
            Some(n) if n % 2 == 0 => return Some(n),
            Some(_) => continue,  // Try next
            None => return None,
        }
    }
}
```

**Complex filtering:**
```rust
struct ValidOnly<I, F> {
    inner: I,
    predicate: F,
}

impl<I, F> Iterator for ValidOnly<I, F>
where
    I: Iterator,
    F: FnMut(&I::Item) -> bool,
{
    type Item = I::Item;
    
    fn next(&mut self) -> Option<I::Item> {
        loop {
            match self.inner.next() {
                Some(item) if (self.predicate)(&item) => {
                    return Some(item)
                }
                Some(_) => continue,
                None => return None,
            }
        }
    }
}

// Usage
let validator = |x: &i32| x > &0 && x < &100;
let filtered = ValidOnly {
    inner: vec![-5, 10, 150, 42, -3, 99].into_iter(),
    predicate: validator,
};
let result: Vec<_> = filtered.collect();
// [10, 42, 99]
```

**Alternative: while let pattern:**
```rust
fn next(&mut self) -> Option<i32> {
    while let Some(n) = self.inner.next() {
        if n % 2 == 0 {
            return Some(n);
        }
    }
    None  // Exhausted
}
```

**Key technique:**
- Loop to skip unwanted elements
- Continue until match found or exhausted
- Essential for filtering iterators

This is how `.filter()` is implemented in standard library!

