## Rule of Sums in Big O

State the Rule of Sums for Big O notation and provide an example.

---

If T₁(n) = O(f(n)) and T₂(n) = O(g(n)), then:
T₁(n) + T₂(n) = O(max(f(n), g(n)))

When adding complexities, keep only the dominant (fastest-growing) term.

Example: O(n²) + O(n) = O(n²) because n² dominates n for large values of n.

