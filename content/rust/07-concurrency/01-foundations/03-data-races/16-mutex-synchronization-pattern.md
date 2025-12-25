## Mutex Synchronization Pattern

How does Arc<Mutex<T>> enable safe shared mutable state, and what prevents data races?

---

Arc provides shared ownership across threads, while Mutex provides synchronized access. The type system ensures you can't access T without first locking the Mutex, which returns a MutexGuard. Only one thread can hold the lock at a time, guaranteeing exclusive access. This breaks the "no synchronization" condition of data races - all accesses are synchronized through the lock, preventing concurrent unsynchronized access.

