## Row-Major Address Calculation Pattern

What is the general pattern for address calculation in row-major order for multidimensional arrays?

---

General pattern for n-dimensional array:

Address(A[i₁, i₂, ..., iₙ]) = α + Σ(iⱼ - lⱼ)·aⱼ

Where aⱼ represents the "stride" for dimension j:
- aⱼ = product of all dimension sizes after j
- Last dimension: aₙ = 1

The pattern: For each dimension, multiply the offset (iⱼ - lⱼ) by the number of elements in all remaining dimensions.

This ensures elements are stored row by row, with rightmost indices varying fastest.

