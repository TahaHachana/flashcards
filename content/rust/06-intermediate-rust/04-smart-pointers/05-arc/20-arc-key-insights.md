## Arc Key Insights

What are the seven key insights about `Arc<T>`?

---

**1. Arc is thread-safe Rc:** Same concept, atomic operations for thread safety

**2. Atomic operations have cost:** ~50% slower than Rc, but still very fast

**3. Use with Mutex for mutation:** `Arc<Mutex<T>>` is the standard pattern for shared mutable state

**4. Send and Sync matter:** These traits determine what can cross thread boundaries

**5. Prefer Rc in single-threaded:** Rc is faster when threads aren't needed

**6. Beware deadlocks:** Lock order matters with multiple mutexes

**7. Arc doesn't make T thread-safe:** T must implement Send/Sync itself

**Mental model:**
```
Arc = Thread-safe shared ownership
Arc<Mutex<T>> = Thread-safe shared mutable state
Arc<RwLock<T>> = Multiple readers, single writer
```

**Bottom line:** Arc is essential for safe multi-threaded programming in Rust. It provides shared ownership guarantees while maintaining thread safety through atomic operations.

