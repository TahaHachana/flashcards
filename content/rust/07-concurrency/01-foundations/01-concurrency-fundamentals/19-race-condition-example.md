## Race Condition Example

Explain how code using `Arc<Mutex<T>>` can have a race condition but not a data race.

---

With `Arc<Mutex<T>>`, the Mutex prevents data races by ensuring synchronized access - only one thread can access the data at a time. However, there's still a race condition: you don't know which thread will acquire the lock first, so the order of operations is unpredictable. For example, two threads incrementing a counter will always produce the correct final value (no data race), but the order of increments is non-deterministic (race condition).

