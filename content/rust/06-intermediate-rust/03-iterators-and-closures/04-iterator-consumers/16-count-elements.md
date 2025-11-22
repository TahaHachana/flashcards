## Count Elements

What does `.count()` do? When is it more efficient than `.len()`?

---

`.count()` returns the number of elements in an iterator.

**Signature:**
```rust
fn count(self) -> usize
```

**Basic usage:**
```rust
let count = vec![1, 2, 3, 4, 5].iter().count();
// 5

let even_count = (1..=100)
    .filter(|x| x % 2 == 0)
    .count();
// 50
```

**After transformations:**
```rust
let valid_count = data.iter()
    .filter(|x| x.is_valid())
    .map(|x| x.process())
    .count();
```

**Performance: O(n) - must iterate through everything**
```rust
// This processes every element
huge_data.iter()
    .filter(predicate)
    .map(transform)
    .count();
```

**When to use `.count()` vs `.len()`:**

**Use `.len()` when available (O(1)):**
```rust
let count = vec.len();  // Instant - stored in Vec
```

**Use `.count()` when:**
- Working with iterator chain
- After filtering/mapping
- Don't have direct collection access
- Iterator doesn't implement ExactSizeIterator

**Comparison:**
```rust
// Efficient
vec![1, 2, 3, 4, 5].len()  // O(1)

// Less efficient but necessary
vec![1, 2, 3, 4, 5].iter()
    .filter(|&&x| x % 2 == 0)
    .count()  // O(n) - must check each element
```

**Checking emptiness:**
```rust
// Less efficient
if data.iter().count() > 0 { }

// More efficient
if !data.is_empty() { }

// Or for iterators
if data.iter().next().is_some() { }
```

`.count()` is necessary for iterators but prefer `.len()` when available.

