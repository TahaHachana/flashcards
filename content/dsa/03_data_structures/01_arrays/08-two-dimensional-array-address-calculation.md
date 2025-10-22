## Two-Dimensional Array Address Calculation

What is the formula for calculating the address of element A[i,j] in a two-dimensional array A[l₁:u₁, l₂:u₂] with base address α using row-major order?

---

Address(A[i,j]) = α + (i - l₁)(u₂ - l₂ + 1) + (j - l₂)

For simplified case A[1:u₁, 1:u₂]:
Address(A[i,j]) = α + (i - 1)·u₂ + (j - 1)

Intuition: To reach row i, skip (i-1) complete rows, each containing u₂ elements, then move to column j within that row.

Example: A[1:10, 1:5] with α = 220
Address of A[8,3] = 220 + (8-1)×5 + (3-1) = 257

