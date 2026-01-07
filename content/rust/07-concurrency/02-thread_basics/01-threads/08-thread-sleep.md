## Thread Sleep

What does thread::sleep do, and what's important to understand about it?

---

thread::sleep pauses the current thread for a specified Duration, yielding the CPU to other threads. Critically, it only blocks the current thread - other threads in the program continue running normally. It's not a precise timer (OS scheduler decides when to wake the thread), and sleeping is cooperative - the thread gives up its time slice. Use sleep to avoid busy-waiting and reduce CPU usage.

