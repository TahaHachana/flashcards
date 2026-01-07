## Connection to Ownership System

How is move with threads the same as ownership transfer in other contexts?

---

It's exactly the same ownership transfer - passing data to functions, returning from functions, assigning to variables. The move keyword makes it explicit in closures. After moving, the original is inaccessible (same as after any move). The only difference is threads have the 'static requirement, but the ownership mechanics are identical. Understanding ownership in single-threaded code directly applies to threads.

