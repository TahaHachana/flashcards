## Connection to Ownership

How do threads demonstrate the power of Rust's ownership system?

---

The move keyword transfers ownership into threads, ensuring only one thread owns data at a time. This prevents data races at compile time - you can't accidentally share mutable state without synchronization. If you want to share, you must explicitly use Arc (for ownership) and Mutex (for mutation), making the cost and synchronization visible. Ownership makes thread safety a compile-time property rather than runtime hope.

