## Compiler Checks for Threads

What checks does the Rust compiler perform when you spawn a thread, and when do these checks happen?

---

At compile time, the compiler checks: (1) Types moved into the thread are Send (safe to transfer ownership), (2) Types shared between threads are Sync (safe to share references), and (3) Borrowed data outlives the thread (lifetime checking). These checks happen at compile time with zero runtime overhead. If any check fails, compilation fails with a clear error explaining the thread safety violation.

