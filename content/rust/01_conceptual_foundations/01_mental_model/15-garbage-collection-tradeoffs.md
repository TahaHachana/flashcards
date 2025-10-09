## Garbage Collection Tradeoffs

What are the costs of garbage collection that Rust avoids?

---

Runtime overhead (GC must track and scan memory), unpredictable pauses (when GC runs), and lack of deterministic cleanup. Rust achieves safety through compile-time checks instead, with zero runtime cost.

