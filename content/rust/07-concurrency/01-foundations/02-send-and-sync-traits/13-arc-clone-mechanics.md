## Arc Clone Mechanics

When you call Arc::clone(&arc), what gets cloned and what doesn't?

---

Arc::clone clones the Arc pointer itself (incrementing the atomic reference count), not the underlying data. Multiple Arc pointers can point to the same heap-allocated data. This is efficient because the data isn't copied - only the pointer and reference count are involved. Each thread gets its own Arc handle to the same shared data.

