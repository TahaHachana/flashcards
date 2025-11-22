## Consumer Best Practices

What are the key best practices when choosing and using iterator consumers?

---

Guidelines for effective and efficient consumer usage:

**1. Choose the right consumer for the job:**
```rust
// Bad - over-collecting
if data.iter().collect::<Vec<_>>().len() > 0 { }

// Good - use appropriate consumer
if data.iter().next().is_some() { }
```

**2. Prefer short-circuiting consumers:**
```rust
// Less efficient - checks everything
let has_valid = data.iter()
    .filter(|x| x.is_valid())
    .count() > 0;

// More efficient - stops early
let has_valid = data.iter().any(|x| x.is_valid());
```

**3. Avoid unnecessary allocation:**
```rust
// Bad - unnecessary Vec
let sum = data.iter()
    .filter(predicate)
    .collect::<Vec<_>>()
    .iter()
    .sum();

// Good - direct sum
let sum: i32 = data.iter()
    .filter(predicate)
    .sum();
```

**4. Use fold for multiple aggregations:**
```rust
// Bad - multiple passes
let sum: i32 = data.iter().sum();
let count = data.iter().count();

// Good - single pass
let (sum, count) = data.iter()
    .fold((0, 0), |(sum, count), &x| (sum + x, count + 1));
```

**5. Collect once, reuse if needed:**
```rust
// Bad - re-computing same iterator chain
let sum = expensive_chain().sum();
let max = expensive_chain().max();

// Good - compute once
let collected: Vec<_> = expensive_chain().collect();
let sum = collected.iter().sum();
let max = collected.iter().max();
```

**6. Provide type annotations clearly:**
```rust
// Bad - unclear turbofish in middle
data.iter().filter(p).collect::<Vec<_>>()

// Good - type at declaration
let result: Vec<_> = data.iter().filter(p).collect();
```

**7. Use specialized consumers over fold:**
```rust
// Verbose
let sum = data.iter().fold(0, |acc, &x| acc + x);

// Clear
let sum: i32 = data.iter().sum();
```

**8. Handle errors appropriately:**
```rust
// Consider if you want:
// - Stop at first error: use collect()
// - Separate errors: use partition()
// - Ignore errors: use filter_map()
```

**9. Don't forget the consumer:**
```rust
// BUG - nothing happens!
data.iter().map(expensive_op);

// Fixed
data.iter().map(expensive_op).for_each(process);
```

**10. Consider performance characteristics:**
```rust
// Slow on huge data
huge.iter().last();  // O(n)

// Fast
huge.last();  // O(1) if direct access available
```

Key principle: Match the consumer to what you actually need.

