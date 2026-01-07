## Scoped Threads

What are scoped threads (thread::scope), and how do they differ from regular threads?

---

Scoped threads can borrow data from the enclosing scope without move because the scope guarantees all threads complete before it ends. thread::scope takes a closure and automatically joins all spawned threads before returning. This allows multiple threads to safely borrow the same data, is more efficient than Arc, and requires no manual joining. Use scoped threads for short-lived threads that need to access local data.

