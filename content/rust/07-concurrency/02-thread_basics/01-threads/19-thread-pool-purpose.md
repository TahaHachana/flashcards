## Thread Pool Purpose

What is a thread pool and why use it instead of spawning threads per task?

---

A thread pool is a fixed set of worker threads that process multiple tasks by reusing the same threads. Benefits: (1) Amortizes thread creation overhead across many tasks, (2) Bounds resource usage (fixed number of threads), (3) Better for many small tasks. Workers wait for tasks from a shared queue. Much more efficient than creating a new thread per task when you have many tasks. Production code often uses the threadpool or rayon crate.

