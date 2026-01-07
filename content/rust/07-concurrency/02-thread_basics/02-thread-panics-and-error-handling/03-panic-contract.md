## Panic Contract

What guarantees does Rust provide when a thread panics?

---

Rust guarantees: (1) The thread's stack is properly unwound, (2) All destructors (Drop implementations) are called in reverse order, (3) The panic is captured and retrievable via join(), (4) Other threads are unaffected (unless it's main thread), and (5) Resources are properly cleaned up. These guarantees maintain memory safety and resource cleanup even during failures.

