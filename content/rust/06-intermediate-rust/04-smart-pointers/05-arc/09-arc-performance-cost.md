## Arc Performance Cost

What is the performance cost of `Arc` compared to `Rc`, and when does it matter?

---

**Benchmark comparison:**
```rust
use std::sync::Arc;
use std::rc::Rc;

// Rc clone: ~10ms for 1M operations
let rc = Rc::new(5);
for _ in 0..1_000_000 {
    let _clone = Rc::clone(&rc);
}

// Arc clone: ~15ms for 1M operations  
let arc = Arc::new(5);
for _ in 0..1_000_000 {
    let _clone = Arc::clone(&arc);
}
```

**Cost:** Arc is ~50% slower than Rc due to atomic operations.

**When it matters:**
- Tight loops with millions of clones
- Low-latency real-time systems
- Single-threaded code (use Rc instead)

**When it doesn't matter:**
- Normal application code
- Data shared across threads (no alternative)
- Infrequent cloning/dropping

**Optimization:**
```rust
// ❌ Unnecessary clone in loop
for i in 0..1000 {
    let data_clone = Arc::clone(&data);
    // Use once
}

// ✅ Clone once, reuse
let data_clone = Arc::clone(&data);
for i in 0..1000 {
    // Use many times
}
```

**Takeaway:** Arc overhead is real but small. Use where needed for thread safety.

