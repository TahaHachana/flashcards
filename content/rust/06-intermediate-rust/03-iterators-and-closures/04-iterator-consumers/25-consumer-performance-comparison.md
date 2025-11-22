## Consumer Performance Comparison

Compare the performance characteristics of different consumers. Which are O(n) and which can short-circuit?

---

Consumer performance varies significantly based on whether they can stop early.

**O(n) - Must check every element:**

**Collection builders:**
```rust
.collect()        // O(n) - must get all elements
.partition()      // O(n) - must check each for both sides
.unzip()         // O(n) - must separate all pairs
```

**Full reducers:**
```rust
.fold()          // O(n) - processes all elements
.sum()           // O(n) - must add everything
.product()       // O(n) - must multiply everything
.count()         // O(n) - must count all
```

**Extractors requiring full iteration:**
```rust
.last()          // O(n) - must get to end
.max()           // O(n) - must check each
.min()           // O(n) - must check each
```

**O(1) to O(n) - Can short-circuit:**

**Searchers:**
```rust
.find()          // O(n) worst, O(1) best - stops at match
.position()      // O(n) worst, O(1) best - stops at match
.any()           // O(n) worst, O(1) best - stops at first true
.all()           // O(n) worst, O(1) best - stops at first false
```

**Element extractors:**
```rust
.nth(0)          // O(1) - just first element
.nth(n)          // O(n) - must skip n elements
```

**Performance comparison example:**
```rust
let huge_data: Vec<_> = (0..1_000_000).collect();

// Fast - short-circuits at element 101
huge_data.iter().any(|&x| x > 100);  
// Checks: 101 elements

// Slow - must check everything
huge_data.iter().count();
// Checks: 1,000,000 elements

// Medium - stops when found
huge_data.iter().find(|&&x| x == 50000);
// Checks: ~50,001 elements
```

**Critical for infinite iterators:**
```rust
// Works - short-circuits
(0..).any(|x| x > 1000);  // Some(1001)

// Works - short-circuits  
(0..).find(|&x| x == 5000);  // Some(5000)

// Hangs forever - no short-circuit
// (0..).count();  // INFINITE LOOP
// (0..).sum();    // INFINITE LOOP
```

**Optimization strategy:**
1. Use short-circuiting consumers when possible
2. Filter/limit before non-short-circuiting consumers
3. Consider order in complex chains

```rust
// Better - limits then counts
huge_data.iter()
    .filter(predicate)
    .take(1000)  // Limit first
    .count();

// vs. counting first (can't limit)
```

