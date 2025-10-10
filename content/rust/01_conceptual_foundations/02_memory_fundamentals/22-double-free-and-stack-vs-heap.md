## Double-Free and Stack vs Heap

Why is double-free only a problem for heap memory and not stack memory?

---

Stack memory is automatically managed by function scope - no explicit freeing occurs. Heap memory must be explicitly freed, so without ownership rules, two variables could try to free the same heap memory twice, causing corruption.

