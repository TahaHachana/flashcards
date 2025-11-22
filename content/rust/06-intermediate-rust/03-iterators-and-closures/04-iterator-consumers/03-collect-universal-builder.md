## Collect Universal Builder

What makes `.collect()` the "universal builder"? Show three different collection types it can build.

---

`.collect()` can build any type implementing `FromIterator`, making it extremely versatile.

**Signature:**
```rust
fn collect<B: FromIterator<Self::Item>>(self) -> B
```

**Building different collections:**

**1. Vec:**
```rust
let vec: Vec<i32> = (1..6).collect();
// [1, 2, 3, 4, 5]
```

**2. HashSet:**
```rust
use std::collections::HashSet;
let set: HashSet<i32> = vec![1, 2, 2, 3, 3].into_iter().collect();
// {1, 2, 3} - duplicates removed
```

**3. HashMap (from pairs):**
```rust
use std::collections::HashMap;
let map: HashMap<&str, i32> = 
    vec![("a", 1), ("b", 2)].into_iter().collect();
// {"a": 1, "b": 2}
```

**4. String (from chars):**
```rust
let string: String = vec!['H', 'i'].into_iter().collect();
// "Hi"
```

**5. Result/Option:**
```rust
let results: Result<Vec<i32>, _> = 
    strings.iter().map(|s| s.parse()).collect();
// Stops at first error
```

The same method builds vastly different types - that's why type annotations are required.

