## Algorithm Scalability

What does it mean for an algorithm to be "scalable," and how does time complexity relate to scalability?

---

**Scalability**: Algorithm's ability to handle growing input sizes efficiently without proportional increase in resource requirements.

**Relationship to complexity**:
- **Highly scalable**: O(1), O(log n), O(n) - handle large inputs well
- **Moderately scalable**: O(n log n), O(n²) - acceptable for moderate sizes
- **Not scalable**: O(2ⁿ), O(n!) - break down quickly as input grows

**Critical insight**: A scalable algorithm maintains reasonable performance as data grows. This is why complexity analysis focuses on large n - it predicts whether the algorithm will work at scale.

Choosing right complexity class determines if solution works in production.

