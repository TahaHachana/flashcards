## Rule of Products in Big O

State the Rule of Products for Big O notation and provide an example.

---

If T₁(n) = O(f(n)) and T₂(n) = O(g(n)), then:
T₁(n) × T₂(n) = O(f(n) × g(n))

When multiplying complexities, multiply the functions.

Example: O(n) × O(log n) = O(n log n), which commonly occurs in efficient sorting algorithms.

