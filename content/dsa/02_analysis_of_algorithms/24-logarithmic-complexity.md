## Logarithmic Complexity

Why is O(log n) considered very efficient, and what type of algorithms typically achieve logarithmic time complexity?

---

**Why efficient**: Logarithmic growth is extremely slow. Doubling input size only adds one operation. For n=1,000,000, log₂(n) ≈ 20.

**Typical algorithms**:
- **Binary search**: Halve search space each step
- **Balanced tree operations**: Height proportional to log n
- **Algorithms that divide problem size**: Each step reduces problem by constant factor

**Key pattern**: Any algorithm that repeatedly divides the problem by a constant factor (usually 2) achieves O(log n) time.

