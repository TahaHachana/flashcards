## Performance Overhead Summary

Create a summary table of all smart pointer operations and their performance costs.

---

```markdown
| Operation           | Cost       | Notes                    |
|---------------------|------------|--------------------------|
| Allocation          |            |                          |
| Stack               | ~0ns       | Just stack pointer       |
| Box                 | ~50ns      | Heap allocator call      |
| Rc                  | ~60ns      | Heap + counter           |
| Arc                 | ~80ns      | Heap + atomic counter    |
| Clone               |            |                          |
| Rc clone            | ~2-3ns     | Counter increment        |
| Arc clone           | ~5-10ns    | Atomic increment         |
| Data clone          | Varies     | Deep copy                |
| Interior Mutability |            |                          |
| Regular &mut        | ~0ns       | Compile-time             |
| RefCell borrow      | ~5-10ns    | Runtime check            |
| Mutex lock          | ~100-200ns | OS lock + atomics        |
| RwLock read         | ~50-100ns  | Shared lock              |
| RwLock write        | ~100-200ns | Exclusive lock           |
```

**When overhead matters:**
- Tight loops (millions of iterations)
- Low-latency systems (audio, games)
- Performance-critical hot paths
- Real-time constraints

**When overhead doesn't matter:**
- Infrequent operations
- I/O-bound code
- Complex algorithms
- Normal application code

**Key insight:** Smart pointer overhead is usually negligible compared to actual work being done. Profile before optimizing.

