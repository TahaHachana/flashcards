## Linearithmic Complexity

What does O(n log n) complexity represent, and why is it considered the optimal complexity for comparison-based sorting?

---

**O(n log n)** = "linearithmic" complexity, combining linear and logarithmic growth.

**Why optimal for sorting**: 
- Must examine all n elements (at least O(n))
- Comparison-based sorting has proven lower bound of Ω(n log n)
- Efficient sorts (merge sort, heap sort, quick sort average case) achieve this

**Growth rate**: Better than O(n²) but worse than O(n). For n=1000:
- n² = 1,000,000 operations
- n log n ≈ 10,000 operations
- Huge improvement over quadratic!

