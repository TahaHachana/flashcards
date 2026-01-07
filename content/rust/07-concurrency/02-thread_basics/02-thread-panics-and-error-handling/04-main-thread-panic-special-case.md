## Main Thread Panic Special Case

What happens when the main thread panics, and how does this differ from other threads?

---

When the main thread panics, the entire process terminates immediately, killing all spawned threads regardless of their state. This is the only exception to panic isolation. Spawned threads panic in isolation and don't affect the process, but the main thread's panic is fatal. Worker threads won't complete their work if main panics - they're forcibly terminated without cleanup.

