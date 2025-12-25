## False Sense of Security

What concurrency bugs can still occur in Rust despite the data race guarantee?

---

Rust prevents data races but not: (1) Race conditions - logic depending on thread timing, (2) Deadlocks - threads waiting for each other in cycles, (3) Livelocks - threads actively preventing each other from progressing, (4) Logic errors in concurrent algorithms, and (5) Performance issues from excessive locking. Data race prevention is a memory safety guarantee, not a correctness guarantee for all concurrent behavior.

