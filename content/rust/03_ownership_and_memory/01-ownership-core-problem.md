## Ownership Core Problem

What problem does Rust's ownership system solve?

---

Manual memory management leads to bugs (leaks, double-free, use-after-free). Garbage collection adds runtime overhead. Ownership enables memory safety without GC by tracking memory at compile time.

