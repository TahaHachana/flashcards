## Common Recurrence Patterns

What are the time complexities for these three common recurrence patterns: (1) T(n) = T(n-1) + c, (2) T(n) = 2T(n/2) + c, (3) T(n) = 2T(n-1) + c?

---

1. **T(n) = T(n-1) + c** → O(n) - Linear recurrence
   (e.g., simple recursive countdown)

2. **T(n) = 2T(n/2) + c** → O(n log n) - Binary divide-and-conquer
   (e.g., merge sort, efficient sorting)

3. **T(n) = 2T(n-1) + c** → O(2ⁿ) - Exponential growth
   (e.g., Tower of Hanoi, inefficient)

