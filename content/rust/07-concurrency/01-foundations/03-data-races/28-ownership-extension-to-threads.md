## Ownership Extension to Threads

How does data race prevention prove that Rust's ownership system works?

---

The same ownership rules that prevent memory errors (use-after-free, double-free) also prevent data races. One owner means no shared access across threads. One mutable or many immutable borrows means no concurrent mutation. References must outlive their data means no dangling pointers in threads. These rules extend seamlessly to concurrent contexts through Send/Sync, proving that ownership is a fundamental safety mechanism that works for both memory safety and concurrency safety.

