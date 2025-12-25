## Why Concurrency Is Hard

What are the main reasons concurrency is traditionally difficult in programming?

---

Concurrency is hard due to: (1) Data races - unsynchronized concurrent access with at least one write, (2) Race conditions - behavior depending on unpredictable timing, (3) Deadlocks - threads waiting for each other in cycles, (4) Memory corruption from unsafe shared access, and (5) Non-deterministic bugs that are extremely difficult to debug and reproduce.

