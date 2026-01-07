## Arc with Mutex

How do Arc and Mutex work together for shared mutable state, and why do you need both?

---

Arc provides shared ownership (multiple threads can have Arc pointers to the same data). Mutex provides synchronized mutation (only one thread can access the data at a time). Pattern: Arc<Mutex<T>>. Each thread gets its own Arc (via clone and move), all pointing to the same Mutex. The Mutex ensures safe mutation despite shared access. You need Arc because each thread must own its Arc, and Mutex because Arc alone only allows shared immutable access.

