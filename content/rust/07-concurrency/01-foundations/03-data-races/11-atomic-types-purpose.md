## Atomic Types Purpose

What are atomic types, and how do they prevent data races in lock-free programming?

---

Atomic types (AtomicUsize, AtomicBool, etc.) provide thread-safe operations without locks. Each atomic operation is indivisible - it completes entirely or not at all, guaranteed by hardware. Operations have memory ordering semantics that ensure proper synchronization between threads. This prevents data races even though multiple threads access the same memory concurrently, because the hardware ensures each operation is atomic and properly synchronized.

