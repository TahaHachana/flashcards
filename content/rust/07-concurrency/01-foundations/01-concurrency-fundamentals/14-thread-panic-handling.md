## Thread Panic Handling

What happens when a thread panics, and why must you handle join results?

---

When a thread panics, the panic is contained to that thread - it doesn't crash the whole program. The `join()` method returns a `Result` containing either the thread's return value (Ok) or the panic payload (Err). If you ignore the join result with `let _ = handle.join()`, you silently ignore panics. Always handle join results in production code to detect and respond to thread failures.

