## Amortized Analysis Concept

What does "amortized" time complexity mean, and how does it differ from worst-case analysis?

---

**Amortized Analysis**: Average time per operation over a sequence of operations, even if individual operations vary in cost.

**Difference from worst-case**:
- **Worst-case**: Maximum time for any single operation
- **Amortized**: Average time per operation over sequence

**Example**: Dynamic array resizing
- Most insertions: O(1)
- Occasional resize: O(n)
- Amortized: O(1) per insertion

Useful when expensive operations are rare and "paid for" by many cheap operations.

