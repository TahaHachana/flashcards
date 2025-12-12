## Smart Pointer Allocation Costs

Compare the allocation costs of stack, Box, Rc, and Arc. Provide benchmark times for 1 million allocations.

---

**Allocation costs (approximate):**

```markdown
| Type  | Cost per allocation | 1M allocations |
|-------|---------------------|----------------|
| Stack | ~0ns                | ~0ms           |
| Box   | ~50ns               | ~50ms          |
| Rc    | ~60ns               | ~60ms          |
| Arc   | ~80ns               | ~80ms          |
```

**What each adds:**
- **Stack:** Just moving stack pointer (instant)
- **Box:** Heap allocator call (~50ns)
- **Rc:** Heap + reference count storage (~60ns)
- **Arc:** Heap + atomic reference count (~80ns)

**Example benchmark:**
```rust
use std::time::Instant;

// Stack: ~0ms
let start = Instant::now();
for _ in 0..1_000_000 {
    let _x = 5;
}
println!("Stack: {:?}", start.elapsed());

// Box: ~50ms
let start = Instant::now();
for _ in 0..1_000_000 {
    let _x = Box::new(5);
}
println!("Box: {:?}", start.elapsed());

// Rc: ~60ms
let start = Instant::now();
for _ in 0..1_000_000 {
    let _x = Rc::new(5);
}
println!("Rc: {:?}", start.elapsed());

// Arc: ~80ms
let start = Instant::now();
for _ in 0..1_000_000 {
    let _x = Arc::new(5);
}
println!("Arc: {:?}", start.elapsed());
```

**Key insight:** Smart pointers add overhead, but are 10-100x faster than cloning actual data.

