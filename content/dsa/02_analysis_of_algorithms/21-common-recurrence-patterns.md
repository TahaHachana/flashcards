## Common Recurrence Patterns

Match these common recurrence patterns to their Big O solutions: T(n) = T(n-1) + c, T(n) = T(n/2) + c, T(n) = 2T(n/2) + cn

---

- T(n) = T(n-1) + c → O(n) - Linear recursion (e.g., factorial)
- T(n) = T(n/2) + c → O(log n) - Logarithmic (e.g., binary search)
- T(n) = 2T(n/2) + cn → O(n log n) - Linearithmic (e.g., merge sort)

The pattern depends on: how many recursive calls are made, how much the problem size reduces, and what extra work is done per call.

