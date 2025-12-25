## Two Concurrency Models

What are the two primary concurrency models supported by Rust, and how do they differ?

---

The two models are: (1) Message Passing - threads communicate by sending data through channels with no shared memory and ownership transferred between threads, and (2) Shared State - threads share memory protected by synchronization primitives like Mutex. Message passing is often clearer and avoids shared state complexity, while shared state can be more efficient for frequently-accessed data. Both are safe in Rust.

