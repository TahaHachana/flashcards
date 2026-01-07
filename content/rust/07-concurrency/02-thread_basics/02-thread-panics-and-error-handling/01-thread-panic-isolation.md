## Thread Panic Isolation

What happens when a thread panics, and does it affect other threads?

---

When a thread panics, it unwinds its stack, runs all destructors, and terminates - but other threads continue running normally. The panic is isolated to that thread. Only if the main thread panics does the entire process exit. This isolation allows building fault-tolerant systems where individual component failures don't crash the entire application. The panic is captured in the JoinHandle and returned as an error via join().

