## Nth Element Extraction

How does `.nth()` work? What's the critical gotcha about its index parameter?

---

`.nth(n)` returns element at index n, but the index is **relative to current position**, not absolute from start.

**Signature:**
```rust
fn nth(&mut self, n: usize) -> Option<Self::Item>
```

**Critical gotcha - relative indexing:**
```rust
let mut iter = vec![10, 20, 30, 40, 50].into_iter();

let third = iter.nth(2);  // Gets index 2 from START
// Some(30)

let next = iter.nth(0);   // Gets index 0 from CURRENT position
// Some(40) - NOT 10!

// iter.nth(3) would be WRONG here - it would skip ahead
```

**What's happening:**
```rust
let mut iter = (0..10);

iter.nth(5);  // Consumes 0,1,2,3,4,5 → returns 5
              // Now at position after 5

iter.nth(0);  // Next element → returns 6
iter.nth(2);  // Skips 7,8 → returns 9
```

**Mental model:** `.nth(n)` means "skip n elements, return the next one"

**Consuming behavior:**
```rust
// Each call consumes elements
let mut iter = (0..10);
iter.nth(2);   // Consumes 0,1,2
iter.nth(2);   // Consumes 3,4,5 (not 2 from start!)
iter.nth(2);   // Consumes 6,7,8
iter.nth(0);   // Returns 9
iter.nth(0);   // None - exhausted
```

**Using for skipping:**
```rust
let mut iter = large_dataset.into_iter();
iter.nth(99);  // Skip first 100 elements (discard result)
// Now at element 100
```

**Better alternative for absolute indexing:**
```rust
let third = vec[2];  // Direct indexing if you have slice
// or
let third = vec.iter().skip(2).next();
```

