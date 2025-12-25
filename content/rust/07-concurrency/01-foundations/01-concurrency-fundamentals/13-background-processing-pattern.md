## Background Processing Pattern

What is the background processing pattern and what is important to remember about it?

---

The background processing pattern spawns a long-running thread (often with a loop) to handle tasks while the main thread continues other work. Important: background threads keep running until the process exits unless explicitly signaled to stop. In real code, you should use channels or other mechanisms to signal shutdown rather than letting the thread run indefinitely or relying on process termination.

