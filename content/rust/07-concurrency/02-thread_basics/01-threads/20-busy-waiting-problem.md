## Busy Waiting Problem

What is busy-waiting and why is it problematic in thread loops?

---

Busy-waiting is spinning in a tight loop checking a condition without yielding the CPU. Example: while running.load() {} with no sleep. Problems: (1) Wastes 100% CPU doing nothing useful, (2) Prevents other threads from getting CPU time, (3) Drains battery on mobile devices, (4) Doesn't scale. Fix: add thread::sleep in the loop to yield the CPU, or use blocking operations like channel recv() instead of polling.

