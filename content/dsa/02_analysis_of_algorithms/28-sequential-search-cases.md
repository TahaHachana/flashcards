## Sequential Search Case Analysis

For sequential search in an array of n elements, what are the best, worst, and average case time complexities? Explain each scenario.

---

**Best Case**: O(1)
- Element found at first position
- Only 1 comparison needed

**Worst Case**: O(n)
- Element at last position OR not present
- Must check all n elements

**Average Case**: O(n)
- Element equally likely at any position
- Average position: n/2
- O(n/2) = O(n)

Note: Even average case is O(n) because we still examine roughly half the array on average.

