## Main Thread Coordination

How do you keep the main thread alive while background workers run, and signal them to stop?

---

Use Arc<AtomicBool> shared between main and worker threads. Workers loop while the flag is true. Main thread sleeps or does other work, then sets the flag to false to signal stop, then joins the workers. The atomic ensures thread-safe access to the flag. Alternative: use channels where workers wait for messages and main sends a stop message. Critical: main must not exit before workers or they'll be killed.

