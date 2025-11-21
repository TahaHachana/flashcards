## Iterator Short Circuiting

Which iterator methods short-circuit (stop early)? Why is this important for performance?

---

Short-circuiting methods stop processing as soon as the answer is known, without checking remaining elements.

**Methods that short-circuit:**

**`.find()` - Stops at first match:**
```rust
let first_big = (0..1_000_000)
    .find(|&x| x > 100);
// Only checks 0-101, not all million
```

**`.any()` - Stops at first true:**
```rust
let has_even = vec![1, 3, 5, 6, 9, 11].iter()
    .any(|&x| x % 2 == 0);
// Stops at 6, doesn't check 9 or 11
```

**`.all()` - Stops at first false:**
```rust
let all_positive = vec![1, 2, -3, 4, 5].iter()
    .all(|&x| x > 0);
// Stops at -3, doesn't check 4 or 5
```

**`.position()` - Stops at first match:**
```rust
let pos = (0..1_000_000)
    .position(|x| x == 500);
// Only checks 0-500
```

**`.take()` - Stops after n elements:**
```rust
(0..).take(10).sum()  // Only processes 10 items from infinite iterator
```

**Why it matters:**

1. **Infinite iterators:** Can safely use with unbounded sequences
```rust
(0..).find(|&x| x > 1000)  // Would hang without short-circuiting
```

2. **Expensive operations:** Avoid unnecessary work
```rust
data.iter()
    .map(|x| expensive_computation(x))
    .find(|x| x.is_good())  // Stops when found
```

3. **Large datasets:** Better performance
```rust
huge_vec.iter().any(|x| x.matches_condition())
// vs
huge_vec.iter().all(|x| !x.matches_condition())  // Opposite logic
```

**Non-short-circuiting methods:**
- `.map()`, `.filter()` - Process everything (lazy but need consumer)
- `.collect()`, `.sum()` - Must process all elements
- `.count()`, `.last()` - Must traverse to end

**Optimization tip:** Use `.rev()` if target is likely near the end:
```rust
data.iter().rev().find(...)  // Search from end
```

