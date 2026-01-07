## Thread Panic Isolation

What happens when a thread panics, and how does it affect other threads?

---

When a thread panics, the panic is isolated to that thread - it doesn't crash the entire program or affect other threads. The panicking thread unwinds its stack and terminates. The panic is captured in the JoinHandle, and join() returns Err containing the panic payload. Other threads, including main, continue running normally. Only if the main thread panics does the entire process exit.

