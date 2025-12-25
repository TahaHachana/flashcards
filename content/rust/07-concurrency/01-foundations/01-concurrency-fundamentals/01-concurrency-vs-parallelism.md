## Concurrency vs Parallelism

What is the difference between concurrency and parallelism?

---

Concurrency is about multiple tasks making progress over time, potentially by interleaving on a single core. Parallelism is about multiple tasks actually executing simultaneously on different cores at the same instant. Concurrency is about dealing with lots of things at once; parallelism is about doing lots of things at once. The same concurrent code works correctly whether it runs in parallel or interleaved.

