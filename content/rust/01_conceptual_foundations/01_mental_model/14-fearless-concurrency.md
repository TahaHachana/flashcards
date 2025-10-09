## Fearless Concurrency

What does "fearless concurrency" mean in Rust?

---

The same ownership system that prevents memory bugs also prevents data races at compile time. If your concurrent code compiles, it is thread-safe. You can write parallel code without fear of subtle race conditions.

