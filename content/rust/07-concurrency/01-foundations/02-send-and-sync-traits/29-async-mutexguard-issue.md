## Async MutexGuard Issue

Why does holding a MutexGuard across an await point cause compilation errors, and how do you fix it?

---

MutexGuard is not Send because it's tied to the thread that acquired the lock. In async code, await points can cause the task to move to a different thread. If you hold the guard across an await, the compiler can't guarantee it will be dropped on the same thread. Fix: drop the guard before the await point by limiting its scope with braces, or use async-aware primitives like tokio::sync::Mutex.

