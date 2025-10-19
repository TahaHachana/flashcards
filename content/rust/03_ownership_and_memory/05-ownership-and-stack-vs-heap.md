## Ownership and Stack vs Heap

Why does ownership primarily concern heap-allocated data?

---

Stack data has fixed size and automatic cleanup when functions return. Heap data has dynamic size and needs explicit management. Ownership rules make heap management safe without manual tracking.

