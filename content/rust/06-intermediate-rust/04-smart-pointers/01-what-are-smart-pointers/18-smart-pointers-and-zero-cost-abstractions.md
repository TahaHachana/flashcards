## Smart Pointers and Zero-Cost Abstractions

Are smart pointers "zero-cost abstractions"? What does this mean and what are the actual costs?

---

Smart pointers are zero-cost abstractions, meaning you only pay for what you use.

**Zero-cost aspects:**
- No hidden overhead beyond what's necessary
- `Box<T>` is just a pointer (same cost as a pointer)
- Deref is compile-time optimization (no runtime cost)

**Actual costs (explicit, not hidden):**
- `Box`: One heap allocation
- `Rc`: Reference counting (increment/decrement operations)
- `Arc`: Atomic reference counting (more expensive than `Rc`)
- `RefCell`: Runtime borrow checking (small overhead)

**What zero-cost means:**
```rust
let boxed = Box::new(5);
let value = *boxed;  // Dereferencing has no runtime cost
```

The abstraction (treating Box like the value) is free. You only pay for the allocation you explicitly requested.

You can't implement this pattern more efficiently by hand - that's zero-cost.

