## Send Trait Connection

How does the Send trait relate to move semantics in threads?

---

When you move data into a thread, the compiler checks if the type is Send. Only Send types can be moved across thread boundaries. The move keyword transfers ownership, and Send ensures that transfer is thread-safe. Non-Send types (like Rc) can't be moved to threads - compilation fails. Send is automatically implemented for types safe to transfer, and checked automatically when using move with threads. Type system enforces thread safety.

