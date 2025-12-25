## Compile-time vs Runtime Safety

What concurrency safety does Rust provide at compile time vs runtime?

---

At compile time: Rust prevents data races by checking Send/Sync traits and ownership rules - code with data races won't compile. At runtime: Rust handles thread panics safely (contained to that thread), and synchronization primitives like Mutex prevent actual data races during execution. The compile-time checks eliminate entire bug classes before the program even runs, while runtime mechanisms handle dynamic scenarios like lock acquisition.

