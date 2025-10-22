## Multidimensional Array Size

What is the formula for calculating the number of elements in a two-dimensional array A[l₁:u₁, l₂:u₂] and a general n-dimensional array?

---

Two-dimensional array A[l₁:u₁, l₂:u₂]:
Number of elements = (u₁ - l₁ + 1) × (u₂ - l₂ + 1)

N-dimensional array A[l₁:u₁, l₂:u₂, ..., lₙ:uₙ]:
Number of elements = ∏(uᵢ - lᵢ + 1) for i = 1 to n

Example: A[1:3, 1:4] has 3 × 4 = 12 elements

