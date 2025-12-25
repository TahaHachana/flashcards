## Concurrent I/O Pattern

How does the concurrent I/O pattern work, and when is it beneficial?

---

Spawn threads for multiple I/O operations (network requests, file reads) that can happen simultaneously, collect their handles, then join them to gather results. This is beneficial for I/O-bound work because while one thread waits for slow I/O, other threads can make progress. The total time is roughly the time of the slowest operation rather than the sum of all operations.

