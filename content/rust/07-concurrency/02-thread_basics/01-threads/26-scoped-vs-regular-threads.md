## Scoped vs Regular Threads

Compare scoped threads (thread::scope) with regular threads (thread::spawn). When should you use each?

---

Regular threads: require 'static or move, manual join needed, can outlive parent scope, more flexible but verbose. Scoped threads: can borrow from parent scope, automatic join at scope end, simpler and more efficient for short-lived threads. Use scoped when: (1) Threads need to borrow local data, (2) Threads are short-lived, (3) You want automatic cleanup. Use regular when: (1) Threads need to outlive parent scope, (2) Background/long-running threads.

