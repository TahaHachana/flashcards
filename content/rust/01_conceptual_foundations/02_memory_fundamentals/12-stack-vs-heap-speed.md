## Stack vs Heap Speed

Why are stack operations faster than heap operations?

---

Stack: just adjust stack pointer (instant). Heap: must request allocation, allocator searches for space, returns pointer, then access through pointer (multiple steps, slower).

