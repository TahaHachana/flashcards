## Manual Memory Management Problems

What problems does manual memory management (C/C++) introduce that Rust solves?

---

Use-after-free (accessing freed memory), double-free (freeing memory twice), memory leaks (forgetting to free), and dangling pointers (references to freed memory). Rust's ownership system prevents all of these at compile time.

