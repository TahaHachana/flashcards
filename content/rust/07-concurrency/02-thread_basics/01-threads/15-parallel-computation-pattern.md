## Parallel Computation Pattern

Describe the parallel computation pattern for dividing work across threads.

---

Split data into chunks, spawn one thread per chunk to process it independently, collect results via join. Example: divide a vector into N chunks, spawn N threads each processing one chunk and returning a partial result, then combine all results. This utilizes multiple CPU cores for CPU-bound work. Key: ensure work per thread justifies thread overhead, and chunks should be independent (no shared state).

