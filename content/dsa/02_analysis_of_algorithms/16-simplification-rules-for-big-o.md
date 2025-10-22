## Simplification Rules for Big O

What are the key simplification rules when expressing functions in Big O notation?

---

1. Drop constant factors: 3n = O(n), not O(3n)
2. Keep only the dominant term: 3n² + 5n + 7 = O(n²)
3. For polynomials A(n) = aₘnᵐ + ... + a₁n + a₀, keep only highest degree: O(nᵐ)
4. Constants become O(1)
5. Lower-order terms are dropped: n² dominates n, which dominates log n

Example: 6n log n + 110n + 9999 simplifies to O(n log n)

