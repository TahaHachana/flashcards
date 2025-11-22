## Take and Skip Positioning

How do `.take()` and `.skip()` work? Show a pagination pattern and explain their complexity.

---

`.take(n)` takes first n elements; `.skip(n)` skips first n elements.

**Basic usage:**
```rust
let first_five = (0..100).take(5).collect::<Vec<_>>();
// [0, 1, 2, 3, 4]

let after_ten = (0..100).skip(10).take(5).collect::<Vec<_>>();
// [10, 11, 12, 13, 14]
```

**Pagination pattern:**
```rust
fn get_page<T>(data: &[T], page: usize, size: usize) -> Vec<&T> {
    data.iter()
        .skip(page * size)
        .take(size)
        .collect()
}

// Page 0: skip 0, take 10 → [0..10)
// Page 1: skip 10, take 10 → [10..20)
// Page 2: skip 20, take 10 → [20..30)
```

**Essential with infinite iterators:**
```rust
let first_ten: Vec<i32> = (0..)  // Infinite!
    .take(10)  // MUST limit
    .collect();
```

**Complexity:**
- `.take(n)`: O(min(n, length)) - stops when limit reached
- `.skip(n)`: O(n) to skip + O(m) to consume rest
- Combined: Both operations fuse efficiently

**Slicing with both:**
```rust
let middle = data.iter()
    .skip(10)   // Skip first 10
    .take(20)   // Take next 20
    .collect(); // Elements [10..30)
```

Used for windowing, sampling, and subsequence extraction.

