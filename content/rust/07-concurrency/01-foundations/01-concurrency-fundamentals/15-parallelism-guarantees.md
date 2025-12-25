## Parallelism Guarantees

Does spawning multiple threads guarantee they will run in parallel? Why or why not?

---

No. The OS scheduler decides whether threads run in parallel. On a single-core machine, threads will run concurrently (interleaved) but not in parallel (simultaneously). Even on multi-core machines, if all cores are busy or the scheduler decides otherwise, threads may interleave. You must write code that's correct whether threads run in parallel or interleaved - never rely on timing assumptions.

