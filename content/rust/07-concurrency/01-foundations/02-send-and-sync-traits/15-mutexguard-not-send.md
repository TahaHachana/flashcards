## MutexGuard Not Send

Why is MutexGuard<T> not Send, and what problems does this prevent?

---

MutexGuard is tied to the thread that acquired the lock - it must be dropped on the same thread that created it. If you could send a MutexGuard to another thread, thread A could acquire a lock but thread B could release it, violating the mutex's invariants and potentially causing deadlocks or data races. This is especially important in async code where tasks can move between threads.

