## Lock Poisoning

What is mutex poisoning, when does it occur, and how should you handle it?

---

A Mutex becomes "poisoned" when a thread panics while holding the lock. This indicates the data inside might be in an inconsistent state. Calling lock() on a poisoned mutex returns Err(PoisonError) instead of Ok(MutexGuard). You can: (1) Propagate the error with ?, (2) Unwrap if you're certain panics won't happen, or (3) Call into_inner() on the PoisonError to access the data anyway (if you know it's safe). Always handle poisoning in production code.

