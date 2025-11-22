## Expensive Closure Placement

Does the placement of expensive operations in iterator chains matter for performance? Explain with an example.

---

Yes! Due to lazy evaluation and short-circuiting, operation order significantly affects performance.

**Bad order - expensive operation runs unnecessarily:**
```rust
let result: Vec<_> = huge_data.iter()
    .map(|x| expensive_computation(x))  // Runs on ALL data
    .take(10)  // Only need 10
    .collect();
```

**Good order - expensive operation runs only when needed:**
```rust
let result: Vec<_> = huge_data.iter()
    .take(10)  // Limit first
    .map(|x| expensive_computation(x))  // Only runs 10 times
    .collect();
```

**With filtering:**
```rust
// Bad - expensive operation before filter
huge_data.iter()
    .map(|x| expensive_process(x))  // Runs on everything
    .filter(|x| x.is_valid())       // Then filters
    .take(100)
    .collect()

// Good - filter first to reduce work
huge_data.iter()
    .filter(|x| x.is_valid())       // Cheap check first
    .take(100)                       // Limit early
    .map(|x| expensive_process(x))  // Only on valid, limited set
    .collect()
```

**Why lazy evaluation makes this work:**
```rust
huge_data.iter()
    .filter(cheap_check)    // Quick filter
    .map(expensive_op)      // Expensive only on passed items
    .find(|x| x.matches())  // Stops when found
// expensive_op only runs until find() succeeds!
```

**Actual execution flow:**
```
1. Get next item from huge_data
2. Apply cheap_check filter
3. If passes, apply expensive_op
4. Check if matches
5. If matches, STOP (short-circuit)
6. Otherwise, go to step 1
```

**Guidelines:**

1. **Cheap operations first** (filters, predicates)
2. **Limit early** (take, take_while) if possible
3. **Expensive operations last** (complex transformations)
4. **Short-circuiting operations benefit most** (find, any, take)

**Exception - when you need all results:**
```rust
// When collecting all, order matters less
// (but still good practice to filter first)
data.iter()
    .filter(cheap)
    .map(expensive)
    .collect()  // Need all results anyway
```

The lazy evaluation model means: **operations only run on items that actually flow through the pipeline**.

