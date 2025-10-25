## Iterator Performance

Why are Rust iterators as fast as manual loops?

---

**Zero-cost abstractions**: Iterator chains are optimized at compile time to eliminate:
- Intermediate allocations
- Unnecessary copies
- Function call overhead

The high-level code compiles to same machine code as hand-written loops.

