## Short Circuiting Consumers

Which consumers short-circuit? Why is this important for performance?

---

Short-circuiting consumers stop processing as soon as the answer is known.

**Short-circuiting consumers:**

**1. `.find()` - stops at first match:**
```rust
let found = (0..1_000_000)
    .find(|&x| x == 500);
// Stops at 500, doesn't check remaining 999,500 elements
```

**2. `.any()` - stops at first true:**
```rust
let has_even = vec![1, 3, 5, 6, 9, 11, 13].iter()
    .any(|&x| x % 2 == 0);
// Stops at 6, doesn't check 9, 11, 13
```

**3. `.all()` - stops at first false:**
```rust
let all_positive = vec![1, 2, -3, 4, 5].iter()
    .all(|&x| x > 0);
// Stops at -3, doesn't check 4, 5
```

**4. `.position()` - stops at first match:**
```rust
let pos = (0..1_000_000)
    .position(|x| x > 1000);
// Stops at 1001
```

**Non-short-circuiting consumers (must check all):**
- `.collect()` - needs all elements
- `.sum()`, `.product()` - needs all for arithmetic
- `.count()` - must count everything
- `.last()` - must get to the end

**Performance impact:**

**With short-circuiting:**
```rust
// Only processes until condition met
huge_dataset.iter()
    .map(expensive_operation)
    .any(|x| x.is_target());
// Stops immediately when target found
```

**Without short-circuiting:**
```rust
// Processes EVERYTHING
huge_dataset.iter()
    .map(expensive_operation)
    .collect::<Vec<_>>();
// Must process all elements
```

**Critical for infinite iterators:**
```rust
// Works - short-circuits
(0..).find(|&x| x > 1000)  // Some(1001)

// Would hang forever
// (0..).collect::<Vec<_>>()  // INFINITE LOOP
```

**Optimization tip:** Use short-circuiting consumers when possible:
```rust
// Inefficient
if data.iter().filter(predicate).count() > 0 { }

// Efficient
if data.iter().any(predicate) { }
```

Short-circuiting is the difference between checking millions of elements and checking just a few.

