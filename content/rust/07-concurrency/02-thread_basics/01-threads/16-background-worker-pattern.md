## Background Worker Pattern

What is the background worker pattern and how is it typically implemented?

---

A long-running thread that processes tasks in a loop, usually receiving work through a channel. Pattern: spawn a thread with a loop that receives messages, processes each message, and breaks on a "stop" signal. Often uses recv_timeout to do periodic work while waiting. Useful for background tasks like logging, monitoring, or processing queues. Clean shutdown requires signaling the thread to stop before joining.

