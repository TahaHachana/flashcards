## Threads vs Async

When should you use threads vs async/await for concurrency?

---

Use threads for: (1) CPU-bound work that benefits from parallelism (utilizing multiple cores), (2) Blocking operations, (3) Simple concurrent work. Use async for: (1) I/O-bound work (network, disk), (2) Handling thousands of concurrent operations, (3) When blocking is expensive. Threads have ~2MB stack overhead per thread; async tasks have ~few KB overhead. Many programs use both: async for I/O, thread pools for parallel computation.

