## Compile-Time vs Runtime Guarantees

What types of errors does Rust catch at compile time rather than runtime?

---

Memory errors (use-after-free, double-free, leaks), data races in concurrent code, and type errors. This shifts bug detection from runtime to compile time with zero runtime cost.

