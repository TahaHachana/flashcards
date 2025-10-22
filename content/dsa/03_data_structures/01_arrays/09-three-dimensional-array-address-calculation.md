## Three-Dimensional Array Address Calculation

What is the formula for calculating the address of element A[i,j,k] in a three-dimensional array A[1:u₁, 1:u₂, 1:u₃] with base address α?

---

Address(A[i,j,k]) = α + (i-1)·u₂·u₃ + (j-1)·u₃ + (k-1)

Conceptual model (building-floor-room analogy):
- i buildings (skip i-1 complete buildings)
- j floors per building (skip j-1 floors)
- k rooms per floor (move to room k)

Each building has u₂×u₃ rooms total
Each floor has u₃ rooms

