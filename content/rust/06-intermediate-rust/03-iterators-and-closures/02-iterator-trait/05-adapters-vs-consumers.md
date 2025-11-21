## Adapters vs Consumers

What's the difference between iterator adapters and iterator consumers? Give examples of each.

---

Iterator methods fall into two categories:

**Adapters (lazy) - Return new iterators:**
- Transform the iterator without executing
- Can be chained indefinitely
- Zero allocation until consumed
- Examples: `.map()`, `.filter()`, `.skip()`, `.take()`, `.enumerate()`

```rust
// Nothing executes yet - just builds the chain
let chain = vec![1, 2, 3, 4, 5].iter()
    .filter(|&&x| x % 2 == 0)  // Adapter
    .map(|&x| x * x);           // Adapter
```

**Consumers (eager) - Return final values:**
- Execute the entire chain
- Produce concrete results
- Terminal operations
- Examples: `.collect()`, `.sum()`, `.for_each()`, `.fold()`, `.find()`

```rust
// Consumer executes the chain
let result: Vec<i32> = chain.collect(); // [4, 16]
```

**Rule:** Adapters are lazy and stack up; consumers trigger execution of the entire chain.

