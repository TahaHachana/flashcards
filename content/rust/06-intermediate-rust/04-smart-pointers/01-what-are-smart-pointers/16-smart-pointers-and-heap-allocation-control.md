## Smart Pointers and Heap Allocation Control

How do smart pointers help control heap vs stack allocation? When would you use this?

---

Smart pointers allow explicit control over where data lives in memory.

**Stack allocation (default):**
```rust
let large_array = [0; 1_000_000];  // Might overflow stack!
```

**Heap allocation with Box:**
```rust
let large_array = Box::new([0; 1_000_000]);  // Safe on heap
```

**When to use heap allocation:**
1. **Large data structures** - Prevent stack overflow
2. **Data that outlives the function** - Transfer ownership without copying
3. **Recursive structures** - Enable self-referential types
4. **Dynamic sizing** - When size isn't known at compile time

Benefits:
- Stack overflow prevention
- Efficient ownership transfer (move pointer, not data)
- Enables types that couldn't exist otherwise

