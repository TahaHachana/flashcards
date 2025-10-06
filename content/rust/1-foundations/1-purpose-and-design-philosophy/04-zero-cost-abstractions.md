## Zero-Cost Abstractions

What does “zero-cost abstractions” mean in Rust?

---

High-level features (iterators, traits, pattern matching) are optimized away at compile time.
They add **no runtime overhead** compared to equivalent low-level code.

```rust
let sum: i32 = vec![1,2,3].iter().map(|x| x * 2).sum();
```

Compiles to a tight loop equivalent to manual iteration but with safer, more expressive syntax.

