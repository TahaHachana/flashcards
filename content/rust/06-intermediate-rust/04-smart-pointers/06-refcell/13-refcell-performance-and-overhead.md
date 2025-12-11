## RefCell Performance and Overhead

What is the performance overhead of `RefCell` compared to regular mutation?

---

**Runtime overhead components:**

**1. Borrow state storage (1-2 bytes):**
```rust
// RefCell stores whether it's borrowed
// and how many immutable borrows exist
```

**2. Borrow checking (~5-10 CPU cycles):**
```rust
let x = RefCell::new(5);
*x.borrow_mut() += 1;  // Checks borrow state at runtime
```

**3. Guard object creation (stack allocation):**
```rust
let guard = x.borrow_mut();  // Creates RefMut guard
```

**Comparison:**
```rust
// Zero runtime cost
let mut x = 5;
x += 1;

// Small runtime cost
let x = RefCell::new(5);
*x.borrow_mut() += 1;
```

**Trade-off: Flexibility vs Performance**
- RefCell: More flexible, small runtime cost
- Regular mut: Less flexible, zero cost

**When it matters:**
- Tight loops (millions of operations)
- Performance-critical hot paths

**When it doesn't matter:**
- Normal application code
- Infrequent updates
- When flexibility is worth the cost

**Bottom line:** Overhead is small but real. Use when architecture demands it, not by default.

