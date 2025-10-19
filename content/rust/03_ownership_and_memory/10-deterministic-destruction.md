## Deterministic Destruction

How does Drop differ from garbage collection?

---

Drop runs deterministically when the owner goes out of scope (you know exactly when). GC runs unpredictably. This makes Rust's resource management predictable.

