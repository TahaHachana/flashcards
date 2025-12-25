## Thread Overhead vs Work

Why is spawning a thread for very small work items problematic? Give an example.

---

Thread creation has significant overhead (memory allocation, OS setup, context switching). If the work is too small, the overhead exceeds the actual computation time, making it slower than sequential execution. Example: spawning threads to multiply single numbers by 2 - the thread overhead (microseconds to milliseconds) far exceeds the multiplication (nanoseconds). Only use threads when work justifies the overhead.

