## Compile-Time Memory Safety

What memory safety guarantees does Rust provide at compile time?

---

No use-after-free, no double-free, no dangling references, no buffer overflows on arrays, and no null pointer dereferences (no null pointers exist in safe Rust).

