## Double-Free Prevention

How does ownership prevent double-free bugs?

---

Only the owner can free memory, and there is only one owner at any time. When the owner goes out of scope, memory is freed exactly once. The compiler ensures you cannot free the same memory twice.

