## Building-Floor-Room Analogy for 2D Arrays

Explain the building-floor-room analogy for understanding 2D array address calculation.

---

For 2D array A[i,j]:

Think of it as a building with:
- i floors (rows)
- j rooms per floor (columns)

To reach room A[i,j]:
1. Skip (i-1) complete floors to reach floor i
2. Each floor has u₂ rooms
3. So skip (i-1)×u₂ rooms total
4. Then move to room j on floor i (skip j-1 more rooms)

Formula: Address = α + (i-1)×u₂ + (j-1)

This mental model helps understand why we multiply the row index by the number of columns.

