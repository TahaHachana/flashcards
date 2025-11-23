## When to Implement Custom Iterator

When should you implement a custom iterator vs using standard library methods?

---

Decision framework for custom iterators vs built-in functionality.

**Implement custom iterator when:**

**1. Complex iteration logic:**
```rust
// Custom: Generate Fibonacci sequence
struct Fibonacci { current: u64, next: u64 }

// Built-in approach would be convoluted
```

**2. Need custom state tracking:**
```rust
// Custom: Track position and running statistics
struct StatsIterator {
    data: Vec<i32>,
    index: usize,
    running_sum: i32,
    running_avg: f64,
}
```

**3. Infinite or lazy generation:**
```rust
// Custom: Generate values on demand
struct RandomNumbers { seed: u64 }

// Can't create infinite Vec
```

**4. Performance-critical iteration:**
```rust
// Custom: Specialized algorithm
struct OptimizedBitIterator {
    bits: u64,
    position: u8,
}

// More efficient than generic approach
```

**5. Wrapping external types:**
```rust
// Custom: Iterate over tree structure
struct TreeIterator<'a, T> {
    stack: Vec<&'a Node<T>>,
}
```

**Don't implement when:**

**1. Simple collection iteration:**
```rust
// ❌ Don't implement - use built-in
// struct MyVecIter { ... }

// ✅ Use built-in
vec.iter()
vec.iter_mut()
vec.into_iter()
```

**2. Can achieve with adaptors:**
```rust
// ❌ Don't implement custom EvensOnly
// struct EvensOnly { ... }

// ✅ Use filter
iter.filter(|x| x % 2 == 0)
```

**3. One-time use:**
```rust
// ❌ Don't implement iterator
// struct OneTimeProcess { ... }

// ✅ Use for loop or iterator methods directly
for item in data {
    process(item);
}
```

**4. Simple transformations:**
```rust
// ❌ Don't implement custom Doubler
// struct Doubler { ... }

// ✅ Use map
iter.map(|x| x * 2)
```

**Decision tree:**
```
Need to iterate?
├─ Over standard collection?
│  └─ Use .iter()/.iter_mut()/.into_iter()
├─ Simple transformation?
│  └─ Use .map()/.filter()/.flat_map()
├─ Combining iterators?
│  └─ Use .zip()/.chain()/.flatten()
├─ Complex logic or state?
│  └─ Implement custom Iterator ✓
├─ Infinite sequence?
│  └─ Implement custom Iterator ✓
└─ Unique iteration pattern?
   └─ Implement custom Iterator ✓
```

**Examples of good use cases:**
```rust
// ✅ Good: Fibonacci (infinite, stateful)
struct Fibonacci { /* ... */ }

// ✅ Good: Tree traversal (complex structure)
struct TreeIter<T> { /* ... */ }

// ✅ Good: Batching (custom grouping)
struct Batcher<I> { /* ... */ }

// ✅ Good: Running statistics (stateful)
struct RunningStats<I> { /* ... */ }

// ❌ Bad: Doubling values
// struct Doubler { /* ... */ }
// Use: iter.map(|x| x * 2)

// ❌ Bad: Filtering evens
// struct Evens { /* ... */ }
// Use: iter.filter(|x| x % 2 == 0)
```

**Guidelines:**
1. Try standard library first
2. Combine adaptors before custom implementation
3. Custom iterators for domain-specific logic
4. Consider maintenance cost
5. Document why custom iterator is needed

**Rule of thumb:**
If you can express it clearly with 1-3 adaptor chains, don't implement custom iterator. If logic is complex, stateful, or performance-critical, custom iterator makes sense.

Custom iterators are powerful but add complexity - use when the benefits outweigh the cost.

