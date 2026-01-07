## Thread Panic vs Result

When should a thread panic vs return Result<T, E>?

---

Use Result for: recoverable errors, expected failures, business logic errors - these let the caller decide how to handle. Use panic for: programming bugs, violated invariants, unrecoverable errors within the thread. In threads, panics are isolated and can be caught by join(), making them suitable for "this thread failed" scenarios. The caller (via join) treats the panic as an error to handle. Panic = unrecoverable within thread, Result = recoverable error.

