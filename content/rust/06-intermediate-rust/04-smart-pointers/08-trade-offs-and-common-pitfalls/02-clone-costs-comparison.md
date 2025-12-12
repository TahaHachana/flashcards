## Clone Costs Comparison

Compare the cost of cloning Rc, Arc, and actual data. What makes smart pointer clones cheap?

---

**Clone costs (1 million clones):**

```markdown
| Operation  | Cost    | What happens          |
|------------|---------|------------------------|
| Rc clone   | ~10ms   | Increment counter (~2-3 CPU cycles) |
| Arc clone  | ~15ms   | Atomic increment (~5-10 CPU cycles) |
| Vec clone  | ~100ms  | Deep copy all data     |
```

**Benchmark:**
```rust
// Rc clone: ~10ms
let rc = Rc::new(vec![1, 2, 3]);
let start = Instant::now();
for _ in 0..1_000_000 {
    let _clone = Rc::clone(&rc);
}
println!("Rc: {:?}", start.elapsed());

// Arc clone: ~15ms (atomic overhead)
let arc = Arc::new(vec![1, 2, 3]);
let start = Instant::now();
for _ in 0..1_000_000 {
    let _clone = Arc::clone(&arc);
}
println!("Arc: {:?}", start.elapsed());

// Actual data: ~100ms (deep copy)
let vec = vec![1, 2, 3];
let start = Instant::now();
for _ in 0..1_000_000 {
    let _clone = vec.clone();
}
println!("Vec: {:?}", start.elapsed());
```

**Why smart pointer clones are cheap:**
- Only increment reference counter
- Don't copy actual data
- Rc: simple counter (2-3 CPU cycles)
- Arc: atomic counter (5-10 CPU cycles)

**Key insight:** Smart pointer clones are 10-100x faster than cloning data.

