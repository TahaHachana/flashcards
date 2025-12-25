## Async and Send Requirement

Why do many async functions require Future: Send bounds, and what issue does this solve?

---

Async runtimes can move tasks between threads for load balancing. If a Future isn't Send, it can't be moved to another thread, limiting scheduling flexibility. The Send bound ensures that all data held across await points can be safely transferred between threads. This is why types like MutexGuard (not Send) cause compilation errors if held across await points.

