## Memory Leak Prevention

How does ownership prevent memory leaks?

---

When the owner goes out of scope, memory is automatically cleaned up (dropped). The compiler guarantees automatic cleanup without requiring manual `free` calls or garbage collection.

