## System Programming Connection

How does Rust's thread API relate to system programming and OS threads?

---

Rust's thread API is a safe wrapper around platform-specific OS threading primitives (pthreads on Unix, Windows threads on Windows). Threads are OS-level constructs that represent actual execution contexts scheduled by the kernel. Rust provides a safe, cross-platform abstraction while maintaining zero-cost: the overhead is just the OS thread overhead, not Rust's abstraction. This connects Rust to systems programming by safely exposing low-level OS capabilities.

