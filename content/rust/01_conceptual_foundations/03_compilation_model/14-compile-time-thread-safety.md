## Compile-Time Thread Safety

What thread safety guarantees does Rust enforce at compile time?

---

No data races (enforced by Send/Sync traits) and proper mutex usage enforced by types. If concurrent code compiles, it's thread-safe.

