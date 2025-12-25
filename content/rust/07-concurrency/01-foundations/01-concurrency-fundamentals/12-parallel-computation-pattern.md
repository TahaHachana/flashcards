## Parallel Computation Pattern

Describe the parallel computation pattern for independent tasks.

---

Spawn separate threads for independent computations that can run simultaneously, store the thread handles, and join them to collect results. Example: spawning two threads each performing expensive calculations, then joining both to get their results. This utilizes multiple cores for CPU-bound work where tasks don't need to communicate or share state.

