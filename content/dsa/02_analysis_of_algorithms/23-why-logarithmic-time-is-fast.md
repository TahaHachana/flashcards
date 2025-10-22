## Why Logarithmic Time is Fast

Why is O(log n) considered very fast, and what characteristic makes an algorithm logarithmic?

---

O(log n) is very fast because the growth is extremely slow - doubling the input size only adds a constant number of operations.

Example: For n = 1,000,000, log₂(n) ≈ 20 operations.

Algorithms achieve logarithmic time when they repeatedly divide the problem size by a constant factor (usually 2) at each step. Binary search is the classic example: each comparison eliminates half of the remaining elements.

Logarithmic algorithms can handle extremely large inputs efficiently.

