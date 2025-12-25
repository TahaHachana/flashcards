## Thread Creation Overhead

What are the costs associated with creating threads, and why shouldn't you create thousands of threads?

---

Each thread consumes significant resources: typically 1-2 MB of memory for its stack, creation and destruction overhead, and OS resources (file descriptors, kernel structures). Creating thousands of threads wastes memory, thrashes the scheduler, and can actually slow down your program. The solution is to use thread pools that reuse a fixed number of threads for many tasks.

