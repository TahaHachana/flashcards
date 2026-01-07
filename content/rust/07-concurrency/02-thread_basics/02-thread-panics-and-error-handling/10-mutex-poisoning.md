## Mutex Poisoning

What is mutex poisoning, when does it occur, and what does it indicate?

---

A Mutex becomes "poisoned" when a thread panics while holding its lock. This indicates the protected data might be in an inconsistent state because the panicking thread may have left it partially modified. Subsequent lock() calls return Err(PoisonError) instead of Ok(MutexGuard). Poisoning is a warning, not a hard error - you can still access the data via into_inner() if you determine it's safe.

