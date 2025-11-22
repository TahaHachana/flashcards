## Last Element Extraction

What does `.last()` do? What's its performance characteristic?

---

`.last()` returns the last element by consuming the entire iterator.

**Signature:**
```rust
fn last(self) -> Option<Self::Item>
```

**Basic usage:**
```rust
let last = vec![1, 2, 3, 4, 5].into_iter().last();
// Some(5)

let empty: Vec<i32> = vec![];
let none = empty.into_iter().last();
// None
```

**With filtering:**
```rust
let last_even = (1..=100)
    .filter(|x| x % 2 == 0)
    .last();
// Some(100)
```

**Performance: O(n) - must iterate through everything**
```rust
// This iterates through ALL elements to get last
huge_vec.iter().last()

// More efficient if you have direct access
let last = huge_vec.last()  // O(1) for Vec
```

**When to use:**
- Don't have direct access to underlying collection
- Working with iterator chain
- After filtering/mapping

**When NOT to use:**
- Have a Vec/slice: use `vec.last()` directly
- Need index too: use `vec.len() - 1`

**Doesn't short-circuit:**
```rust
// Processes ENTIRE range even though we only want last
(0..1_000_000)
    .map(expensive_operation)
    .last();  // Performs 1 million operations!
```

Unlike `.find()` or `.any()`, `.last()` must consume everything.

