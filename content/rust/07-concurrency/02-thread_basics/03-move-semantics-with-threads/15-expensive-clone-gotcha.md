## Expensive Clone Gotcha

What's wrong with cloning large data structures for each thread, and what's the fix?

---

Cloning large structures (Vec of millions of elements) for each thread wastes memory and time - if you have 10 threads and 1GB data, you use 10GB. Fix: use Arc to share the data instead. Arc::clone is cheap (just increments counter), all threads access the same data. Only clone if threads need independent copies. For read-only sharing, Arc is almost always better than clone.

