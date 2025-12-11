## Rc Performance Costs

What are the performance costs of using `Rc`, and when do they matter?

---

**Operations and costs:**

**Allocation (same as Box):**
```rust
let rc = Rc::new(data);  // One heap allocation
```

**Cloning (very cheap):**
```rust
let rc2 = Rc::clone(&rc);  // ~2-3 CPU instructions (counter++)
```

**Dropping (cheap):**
```rust
drop(rc);  // ~5-10 CPU instructions (counter--, check zero)
```

**Benchmark comparison:**
```rust
// Rc clone: ~10ms for 1M operations
let rc = Rc::new(vec![1, 2, 3]);
for _ in 0..1_000_000 {
    let _clone = Rc::clone(&rc);
}

// Vec clone: ~100ms for 1M operations  
let vec = vec![1, 2, 3];
for _ in 0..1_000_000 {
    let _clone = vec.clone();
}
```

**When costs matter:**
- Tight loops with millions of allocations/drops
- Performance-critical hot paths
- Real-time systems

**When costs don't matter:**
- Normal application code
- Data shared across program (allocated once)
- When avoiding clones is more important

**Takeaway:** `Rc` overhead is negligible compared to cloning actual data.

