## Move Semantics in Threads

Why does Rust require the `move` keyword when capturing variables in thread closures, and how does this prevent data races?

---

The `move` keyword transfers ownership of captured variables from the parent scope into the thread's closure. This prevents data races by ensuring only one thread owns the data - the parent thread can no longer access it after the move. Without `move`, both threads could potentially access the same data, creating a data race. The compiler enforces this to guarantee thread safety.

