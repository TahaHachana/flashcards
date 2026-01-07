## Threading Model

What threading model does Rust use, and what does this mean?

---

Rust uses a 1:1 threading model where each Rust thread corresponds to one native OS thread (pthread on Unix, Windows thread on Windows). This means threads have real overhead (memory for stack, OS resources) but provide true parallelism and are scheduled by the OS. There's no green threading or M:N model - Rust threads are direct wrappers around OS threads.

