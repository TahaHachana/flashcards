## Factorial Recurrence Analysis

For the factorial function where T(n) = c + T(n-1) for n > 1 and T(n) = d for n ≤ 1, what is the time complexity and how is it derived?

---

The recurrence T(n) = c + T(n-1) is solved by repeated substitution:
- T(n) = c + T(n-1)
- T(n) = 2c + T(n-2)
- T(n) = 3c + T(n-3)
- T(n) = kc + T(n-k)
- When k = n-1: T(n) = (n-1)c + T(1) = (n-1)c + d

Time complexity: O(n) - linear time

This represents algorithms that recurse once with problem size reduced by 1.

