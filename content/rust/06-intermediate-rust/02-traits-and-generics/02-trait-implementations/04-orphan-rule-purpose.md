## Why the Orphan Rule Exists

Why does Rust have the orphan rule? What problems does it prevent?

---

The orphan rule prevents **coherence problems**:

1. **Multiple conflicting implementations** - Two crates could implement the same trait for the same type differently
2. **Unpredictable behavior** - Which implementation gets used would depend on import order
3. **Breaking changes** - Adding a trait implementation could break downstream code

Without it, the same type could behave differently depending on which crate's implementation was imported.

