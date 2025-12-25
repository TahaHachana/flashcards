## Atomic Operations Pattern

How do atomic operations like fetch_add provide lock-free shared mutation without data races?

---

Each atomic operation is indivisible at the hardware level - it happens completely or not at all, with no intermediate state visible to other threads. Memory ordering semantics (like SeqCst) ensure operations are properly synchronized and visible across threads in the right order. This prevents data races even without locks because the hardware guarantees atomicity and proper synchronization. Multiple threads can safely modify the same atomic variable concurrently.

