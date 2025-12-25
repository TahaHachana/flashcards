## When Concurrency Helps Performance

When does concurrency actually improve performance, and when doesn't it?

---

Concurrency helps when: (1) CPU-bound work can utilize multiple cores (parallelism), or (2) I/O-bound work allows doing other work while waiting. It doesn't help when: (1) The work is too small to justify thread overhead, (2) You're already maxing out available cores, or (3) The work is inherently sequential. Only use concurrency when the work being done justifies the overhead.

