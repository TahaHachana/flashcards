## Thread Creation Overhead

What are the costs of creating threads, and what's the typical guideline for how many to create?

---

Each thread costs: (1) 1-2MB of memory for its stack, (2) OS resources (file descriptors, kernel structures), (3) Creation and destruction overhead, (4) Context switching overhead. Creating thousands of threads wastes resources. Guideline: create threads roughly equal to the number of CPU cores for CPU-bound work, or use a thread pool to reuse threads. For I/O-bound work, consider async instead.

