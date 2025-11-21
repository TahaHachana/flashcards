## Forgetting to Consume Adapters

What's wrong with this code and how do you fix it?

```rust
vec![1, 2, 3].iter().map(|x| {
    println!("Processing {}", x);
    x * 2
});
```

---

**Problem:** The iterator chain is never consumed, so nothing executes. Adapters like `.map()` are lazy and don't run until consumed.

```rust
// BUG: Nothing prints!
vec![1, 2, 3].iter().map(|x| {
    println!("Processing {}", x);
    x * 2
});
// map() builds the iterator but never calls the closure
```

**Fix 1: Add a consumer:**
```rust
vec![1, 2, 3].iter()
    .map(|x| {
        println!("Processing {}", x);
        x * 2
    })
    .collect::<Vec<_>>();  // Now it executes
```

**Fix 2: Use `.for_each()` for side effects:**
```rust
vec![1, 2, 3].iter().for_each(|x| {
    println!("Processing {}", x);
    // No need to return anything
});
```

**Why this happens:**
- Rust's iterators are lazy for performance
- Adapters return iterator types, not values
- Without a consumer, the iterator is never polled
- Compiler may warn about "unused" iterator

**Rule:** Every iterator chain needs a terminal consumer like `.collect()`, `.sum()`, `.for_each()`, or a `for` loop.

