## Practical Implications of Algorithm Choice

Using a concrete example, demonstrate the practical difference between O(n) and O(n²) algorithms for n = 1,000,000.

---

Example: Finding maximum element in an array

O(n) algorithm: Single pass through array
- Operations: ~1,000,000
- Time: milliseconds

O(n²) algorithm: Nested comparison approach
- Operations: ~1,000,000,000,000 (one trillion)
- Time: hours to days

Speedup: 1,000,000× faster

This demonstrates why algorithm analysis matters in practice - the right algorithm can make the difference between milliseconds and hours.

