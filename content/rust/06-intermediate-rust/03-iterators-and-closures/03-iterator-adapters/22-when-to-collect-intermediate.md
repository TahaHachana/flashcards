## When to Collect Intermediate

When should you collect intermediate results in an iterator chain? Give examples of when it helps and when it hurts.

---

Generally avoid intermediate collections, but they're beneficial in specific scenarios.

**When to AVOID intermediate collection (most cases):**
```rust
// BAD - unnecessary intermediate allocation
let intermediate: Vec<_> = data.iter()
    .map(expensive_op)
    .collect();  // ❌ Materializes here

let result: Vec<_> = intermediate.iter()
    .map(another_op)
    .collect();

// GOOD - single pass, no allocation
let result: Vec<_> = data.iter()
    .map(|x| another_op(expensive_op(x)))
    .collect();
```

**When intermediate collection HELPS:**

**1. Multiple iterations needed:**
```rust
// GOOD - collect once, iterate multiple times
let intermediate: Vec<_> = data.iter()
    .map(expensive_op)
    .collect();

let sum1: i32 = intermediate.iter().sum();
let sum2: i32 = intermediate.iter().map(|x| x * 2).sum();
let max = intermediate.iter().max();
```

**2. Short-circuiting prevents recomputation:**
```rust
// GOOD - find() stops early, no recomputation
let processed: Vec<_> = data.iter()
    .map(expensive_op)
    .collect();

if let Some(first) = processed.iter().find(|x| x.is_valid()) {
    // Use first, might iterate again
    let others = processed.iter().filter(|x| x != first);
}
```

**3. Debugging complex chains:**
```rust
// GOOD for debugging - inspect intermediate state
let stage1: Vec<_> = data.iter().map(op1).collect();
println!("After stage 1: {:?}", stage1);

let stage2: Vec<_> = stage1.iter().map(op2).collect();
println!("After stage 2: {:?}", stage2);
```

**4. Working with non-Clone expensive types:**
```rust
// If expensive_op returns non-Clone type you need multiple times
let computed: Vec<_> = data.iter()
    .map(expensive_op)
    .collect();

process_a(&computed);
process_b(&computed);  // Can reuse
```

**Trade-off analysis:**
- **Cost**: Allocation + data copy
- **Benefit**: Reusability or simplified logic

**Rule of thumb:** Only collect intermediate when you need to iterate multiple times or genuinely need the materialized data. Otherwise, let adaptor fusion work its magic.

