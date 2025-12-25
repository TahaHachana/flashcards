## Why Both Models Are Safe

Why are both message passing and shared state concurrency models safe in Rust, unlike in other languages?

---

Both models are safe because Rust enforces safety at compile time through the type system. For message passing, ownership transfer through channels ensures only one thread owns data at a time. For shared state, types like `Arc` and `Mutex` have built-in synchronization that the type system enforces. The compiler won't let you share mutable state without proper synchronization or send non-thread-safe types between threads.

