## Sync Trait Definition

What does the Sync trait mean in Rust?

---

Sync means a type can be safely shared (referenced) between multiple threads. Immutable references (&T) can cross thread boundaries. If a type is Sync, multiple threads can have immutable references to it simultaneously. Most immutable types are Sync, including primitives and types with thread-safe interior mutability like Mutex.

