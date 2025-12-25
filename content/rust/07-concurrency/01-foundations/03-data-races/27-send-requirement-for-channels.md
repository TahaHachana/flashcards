## Send Requirement for Channels

Why do channels require sent data to be Send, and what would go wrong without this requirement?

---

Channels transfer ownership from the sending thread to the receiving thread. The data crosses thread boundaries, so it must be Send (safe to transfer between threads). If you could send non-Send types like Rc, you could have multiple threads with Rc pointers, causing data races on the non-atomic reference count. The Send requirement ensures only thread-safe types can be sent through channels, preventing data races at compile time.

