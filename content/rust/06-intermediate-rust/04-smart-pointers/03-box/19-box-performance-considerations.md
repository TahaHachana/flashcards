## Box Performance Considerations

What are the performance costs of using `Box`, and when do they matter?

---

**Two main costs:**

**1. Allocation cost:**
```rust
// Heap allocation (slower: ~50ms for 1M allocations)
let boxed = Box::new(42);

// Stack allocation (faster: ~1ms for 1M allocations)
let value = 42;
```

**2. Indirection cost:**
```rust
let value = 42;
let result = value + 1;  // Direct access

let boxed = Box::new(42);
let result = *boxed + 1;  // One pointer dereference
```

**When costs matter:**
- Tight loops with millions of iterations
- Performance-critical hot paths
- Small data that fits easily on stack
- Allocating/deallocating frequently

**When costs don't matter:**
- Data only allocated once or infrequently
- Large data (heap allocation unavoidable)
- Recursive structures (Box is necessary)
- Trait objects (Box enables pattern)

**Rule:** Don't optimize prematurely. Use Box where it makes sense conceptually, profile if performance matters.

